from django.urls import path

from courses.views.room import list_rooms, create_room,room_update,room_delete


urlpatterns=[
    path('list/',list_rooms,name='list-rooms'),
    path('create/',create_room,name='create-room'),
    path('update/<int:pk>/', room_update, name='update-room'),
    path('delete/<int:pk>/', room_delete, name='delete-room'),
]