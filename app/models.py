from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    roll_number = models.IntegerField()
    section = models.CharField(max_length = 3)
