from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    name = models.CharField(max_length=400)
    description = models.TextField(max_length=1000)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True)

class Lecture(models.Model):
    date_given = models.DateField()
    date_added = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    note_file = models.FileField(upload_to='notes')

class LectureVersion(models.Model):
    predec = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    date_changed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    note_file = models.FileField(upload_to='notes')
