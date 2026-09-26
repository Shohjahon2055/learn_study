from email.policy import default
from django import forms
from accounts.models import CustomUser,TeacherProfile,StudentProfile
from django.db import transaction

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

# TEACHER

class TeacherForm(forms.Form):
    phone=forms.CharField()
    username=forms.CharField()
    password=forms.CharField()
    specialization=forms.CharField()
    bio=forms.CharField()
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class TeacherEditForm(forms.Form):
    username = forms.CharField(max_length=150)
    specialization = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False,
                               help_text="O'zgartirmasangiz bo'sh qoldiring")

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("Bu username band.")
        return username

    @transaction.atomic
    def save(self, profile):
        user = profile.user
        user.username = self.cleaned_data["username"]
        if self.cleaned_data.get("password"):
            user.set_password(self.cleaned_data["password"])
        user.save()

        profile.specialization = self.cleaned_data["specialization"]
        profile.bio = self.cleaned_data["bio"]
        profile.save()
        return profile

# class TeacherEditForm(forms.Form):
#     username=forms.CharField()
#     specialization=forms.CharField()
#     bio=forms.CharField()
#     password=forms.CharField()
#
#
#     def save(self):
#         specialization=self.cleaned_data.get('specialization')
#         bio=self.cleaned_data.get('bio')
#         return
#
#
# from django import forms
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# class TeacherEditForm(forms.Form):
#     username = forms.CharField()
#     specialization = forms.CharField()
#     bio = forms.CharField(widget=forms.Textarea)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def save(self, profile):
#         """
#         Mavjud TeacherProfile va unga bog'liq CustomUser'ni yangilash
#         """
#         # 1. CustomUser ma'lumotlarini yangilash
#         user = profile.user  # TeacherProfile modelida user maydoni bor deb hisoblaymiz
#         user.username = self.cleaned_data['username']
#         user.set_password(self.cleaned_data['password']) # Parolni xavfsiz xesh qilish
#         user.save()
#
#         # 2. TeacherProfile ma'lumotlarini yangilash
#         profile.specialization = self.cleaned_data['specialization']
#         profile.bio = self.cleaned_data['bio']
#         profile.save()
#
#         return profile