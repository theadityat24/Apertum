from django.db import models

class School(models.Model):
    name = models.CharField(max_length=400)

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    description = models.TextField(max_length=1000)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True)

class Lecture(models.Model):
    date_given = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

# TODO: Add User field to all of the models.