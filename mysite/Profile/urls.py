from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='Profile-home'),
    path("about/", views.about, name="Profile-about"),
]