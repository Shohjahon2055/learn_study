from email.policy import default
from django import forms
from accounts.models import CustomUser,TeacherProfile,StudentProfile

class CustomUserForm(forms.ModelForm):
    is_teacher = forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields=[
            'username',
            'phone',
            'password',
            'is_teacher',
        ]
    def save(self,commit=True):
        username=self.cleaned_data.get('username')
        phone=self.cleaned_data.get('phone')
        password=self.cleaned_data.get('password')
        is_teacher=self.cleaned_data.get('is_teacher')
        user=CustomUser.objects.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        if is_teacher:
            TeacherProfile.objects.create(user=user)
            user.role='teacher'
            user.save()
        else:
            StudentProfile.objects.create(user=user)
            user.role='student'
            user.save()

        return user

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)