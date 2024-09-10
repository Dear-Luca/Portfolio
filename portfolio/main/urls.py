from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("projects/", views.projects, name="contact"),
    path("project/<int:id>", views.project, name="project"),
    
]