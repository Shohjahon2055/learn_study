from courses.forms.course import CourseForm
from courses.models import Course
from django.shortcuts import render,redirect

def list_courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/course/list.html', context)


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-courses')

    else:
        form=CourseForm()
    return render(request, 'courses/course/create.html', {'form': form})

def courses_update(request,pk):
    courses = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form=CourseForm(request.POST,instance=courses)
        if form.is_valid():
            form.save()
            return redirect('list-courses')
    else:
        form = CourseForm(instance=courses)
    return render(request, 'courses/course/update.html', {'form': form, 'courses': courses})


def courses_delete(request,pk):
    courses = Course.objects.get(pk=pk)
    if request.method == 'POST':
        courses.delete()
        return redirect('list-courses')
    else:
        return render(request, 'courses/course/delete.html', {'courses': courses})

