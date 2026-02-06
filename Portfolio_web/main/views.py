from django.shortcuts import render, redirect
from .models import Project, Skill, Internship,Education,Hobby

def home(request):
    projects = Project.objects.all()[:3]  # show 3 latest
    skills = Skill.objects.all()
    return render(request, "home.html", {"projects": projects, "skills": skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

def skills(request):
    skills = Skill.objects.all()
    return render(request, "skills.html", {"skills": skills})


def internships(request):
    internships = Internship.objects.all()
    return render(request, "internships.html", {"internships": internships})

def education(request):
    educations = Education.objects.all()
    return render(request, "education.html", {"educations": educations})

def hobbies(request):
    hobbies = Hobby.objects.all()
    return render(request, "hobbies.html", {"hobbies": hobbies})
