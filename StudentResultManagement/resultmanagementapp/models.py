from django.db import models

# Create your models here.
class SixResultModel(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default=None)
    english = models.IntegerField(default=None)
    maths = models.IntegerField(default=None)
    science = models.IntegerField(default=None)

class SevenResultModel(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default=None)
    english = models.IntegerField(default=None)
    maths = models.IntegerField(default=None)
    science = models.IntegerField(default=None)

class EightResultModel(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default=None)
    english = models.IntegerField(default=None)
    maths = models.IntegerField(default=None)
    science = models.IntegerField(default=None)

class FacultyModel(models.Model):
     name = models.CharField(max_length = 100)
     image = models.ImageField(upload_to = "faculty/")
     qualifications = models.CharField(max_length = 250)
     introduction = models.TextField()

class CoursesModel(models.Model):
     image = models.ImageField(upload_to = "courses/")
     title = models.CharField(max_length = 250)
     introduction = models.TextField()
