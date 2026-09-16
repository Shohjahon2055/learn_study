from accounts.forms import CustomUserForm,LoginForm,StudentProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate


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
                login(request, user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')