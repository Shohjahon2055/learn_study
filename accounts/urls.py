from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.create_user,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]