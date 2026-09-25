from django.urls import path

from courses.views.room import list_rooms, create_room,room_update,room_delete
from courses.views.course import list_courses,create_course,courses_update,courses_delete
from courses.views.group import list_group,create_group,group_update,group_delete,group_students_manage

urlpatterns=[
    path('list/',list_rooms,name='list-rooms'),
    path('create/',create_room,name='create-room'),
    path('update/<int:pk>/', room_update, name='update-room'),
    path('delete/<int:pk>/', room_delete, name='delete-room'),

    # courses Crud
    path('courses/list/',list_courses,name='list-courses'),
    path('courses/create/',create_course,name='create-courses'),
    path('courses/update/<int:pk>/', courses_update, name='update-courses'),
    path('courses/delete/<int:pk>/', courses_delete, name='delete-courses'),

    # Group crud
    path('groups/list/',list_group,name='list-groups'),
    path('groups/create/',create_group,name='create-group'),
    path('groups/update/<int:pk>/', group_update,name='update-group'),
    path('groups/delete/<int:pk>/', group_delete,name='delete-group'),
    path('<int:group_id>/students/', group_students_manage, name='group-students-manage'),

]