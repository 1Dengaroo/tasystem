from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    class UserType(models.TextChoices):
        STUDENT = 'STUDENT'
        INSTRUCTOR = 'INSTRUCTOR'
        ADMIN = 'ADMIN'

    user_type = models.CharField(max_length=20, choices=UserType.choices)

class Course(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    description = models.TextField()
    section = models.CharField(max_length=10)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_tas_needed = models.IntegerField()
    extra_info = models.TextField()