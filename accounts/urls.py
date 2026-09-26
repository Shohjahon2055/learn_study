from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.create_user,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('teacher_dashboard/', views.teacher_dashboard,name="teacher_dashboard"),

    #TEACHER
    path('teacher/',views.teacher_list,name='teacher'),
    path("teacher/profile/", views.get_profile, name="teacher_profile"),
    path("teacher/profile/edit/", views.edit_teacher_view, name="edit_teacher"),
    path("teacher/profile/edit/", views.edit_teacher_view, name="edit_teacher"),
    path("teacher/profile/group/", views.get_my_groups, name="get_my_groups"),

    #     path('', views.get_teacher, name="teacher"),
#     path("teacher/profile/", views.get_profile, name="teacher_profile"),
#     path("teacher/profile/edit/", views.edit_teacher_view, name="edit_teacher"),
#     path("teacher/profile/group/", views.get_my_groups, name="get_my_groups"),
]