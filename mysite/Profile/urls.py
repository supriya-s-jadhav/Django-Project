from django.urls import path
from . import views

urlpatterns = [
    path("Blog/", views.blog, name="Profile-blog"),
    path("about/", views.about, name="Profile-about"),
    path("home/", views.home, name='Profile-home'),
]