from django.shortcuts import render,redirect
from courses.models import Group,GroupStudent
from courses.forms.group import GroupForm,GroupStudentAddForm,GroupStudentRemoveForm
from datetime import date
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-groups')
    else:
        form = GroupForm()
    return render(request, 'courses/group/create.html', {'form': form})

def list_group(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'courses/group/list.html', context)

def group_update(request,pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        form=GroupForm(request.POST,instance=group)
        if form.is_valid():
            form.save()
            return redirect('list-groups')
    else:
        form = GroupForm(instance=group)
    return render(request, 'courses/group/update.html', {'form': form,})


def group_delete(request,pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('list-groups')
    else:
        return render(request, 'courses/group/delete.html', {'group': group})


def group_students_manage(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    add_form = GroupStudentAddForm(group=group)
    remove_form = GroupStudentRemoveForm(group=group)

    if request.method == 'POST':
        if 'add_submit' in request.POST:
            add_form = GroupStudentAddForm(request.POST, group=group)
            if add_form.is_valid():
                students = add_form.cleaned_data['students']
                with transaction.atomic():
                    for s in students:
                        obj, created = GroupStudent.objects.update_or_create(
                            group=group,
                            student=s,
                            defaults={
                                'is_active': True,
                                'joined_at': date.today(),
                                'left_at': None,
                            },
                        )
                messages.success(request, f'{students.count()} ta student qo\'shildi')
                return redirect('group-students-manage', group_id=group.id)

        elif 'remove_submit' in request.POST:
            remove_form = GroupStudentRemoveForm(request.POST, group=group)
            if remove_form.is_valid():
                students = remove_form.cleaned_data['students']
                with transaction.atomic():
                    GroupStudent.objects.filter(
                        group=group, student__in=students, is_active=True
                    ).update(is_active=False, left_at=date.today())
                messages.success(request, f'{students.count()} ta student chiqarildi')
                return redirect('group-students-manage', group_id=group.id)

    return render(request, 'courses/group/group_students_manage.html', {
        'group': group,
        'add_form': add_form,
        'remove_form': remove_form,
    })
