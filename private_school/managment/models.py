from django.db import models
from django.db.models.deletion import SET_NULL


# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=30)
    course_language = models.CharField(max_length=30)
    course_descreption = models.TextField()
    course_type = models.CharField(max_length=30)

    def __str__(self):
        return self.course_title

class Trainers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30, null=True)
    courses = models.ManyToManyField(Course, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name