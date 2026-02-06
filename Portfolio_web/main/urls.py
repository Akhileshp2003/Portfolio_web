from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("skills/", views.skills, name="skills"),
    path("internships/", views.internships, name="internships"), 
    path("education/", views.education, name="education"),
    path("hobbies/", views.hobbies, name="hobbies"),  
]
