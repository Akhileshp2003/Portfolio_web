from django.contrib import admin
from .models import Project, Skill,Internship,Education,Hobby

admin.site.register(Project)
admin.site.register(Skill)

admin.site.register(Internship)
admin.site.register(Education)
admin.site.register(Hobby)