from django.db import models

# Create your models here.

class Student(models.Model):
	regno = models.CharField(max_length=9)
	dob = models.CharField(max_length=8)
	number = models.CharField(max_length=10)
	fb_id = models.CharField(max_length=50)
	data = models.CharField(max_length=1024)
