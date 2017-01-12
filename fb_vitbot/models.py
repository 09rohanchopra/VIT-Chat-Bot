from django.db import models

# Create your models here.

class Student(models.Model):
	regno = models.CharField(max_length=9)
	password = models.CharField(max_length=20)
	data = models.CharField(max_length=1024)
