from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/")

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()  # 0 to 100

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Internship(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)   # Example: "Jan 2024 - Mar 2024"
    technologies = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)          
    institution = models.CharField(max_length=200)     
    year = models.CharField(max_length=100)            
    score = models.CharField(max_length=50)            


    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Hobby(models.Model):
    title = models.CharField(max_length=100)    
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
