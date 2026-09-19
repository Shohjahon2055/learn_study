from django.urls import path

from courses.views.room import list_rooms, create_room,room_update,room_delete
from courses.views.course import list_courses,create_course,courses_update,courses_delete


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

]