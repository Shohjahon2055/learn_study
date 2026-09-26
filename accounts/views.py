
from accounts.forms import CustomUserForm,LoginForm,StudentProfile,TeacherForm,TeacherEditForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .models import TeacherProfile,CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from courses.models import Group


def create_user(request):
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save()

            if user:
                login(request, user)
                return redirect('home')
    else:
        form=CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user:
                teacher=user

                login(request, user)
                if teacher.role==CustomUser.Role.TEACHER:
                    return redirect('teacher_dashboard')
                return redirect('home')
    else:
        form=LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


# TEACHER

def teacher_list(request):
    teachers = TeacherProfile.objects.all()
    return render(request, 'accounts/teacher_list.html', {'teachers': teachers})


# TEACHER
def teacher_dashboard(request):
    return render(request,"accounts/teacher/teacher.html")

@login_required
def get_profile(request):
    user=request.user
    if user:
        teacher=TeacherProfile.objects.get(user=user)
    else:
        return redirect('home')

    return render(request,"accounts/teacher/profile.html",{'teacher':teacher})

@login_required
def edit_teacher_view(request):
    profile = get_object_or_404(TeacherProfile.objects.select_related("user"), user=request.user)
    user = profile.user

    if request.method == "POST":
        form = TeacherEditForm(request.POST, user=user)
        if form.is_valid():
            form.save(profile=profile)
            if form.cleaned_data.get("password"):
                update_session_auth_hash(request, user)
            return redirect("teacher_profile")
    else:
        form = TeacherEditForm(user=user, initial={
            "username": user.username,
            "specialization": profile.specialization,
            "bio": profile.bio,
        })

    return render(request, "accounts/teacher/edit_teacher.html", {"form": form})



def get_my_groups(request):
    user=request.user
    teacher=TeacherProfile.objects.get(user=user)
    groups=Group.objects.filter(teacher=teacher)
    context={
        "groups":groups,
        "teacher":teacher
    }
    return render(request,"accounts/teacher/teacher_group.html",context)