from django.contrib import admin
from django.urls import path
from narmativ.views import base_html
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', base_html,name="home"),
]