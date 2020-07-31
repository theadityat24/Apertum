from django.contrib import admin
from .models import (
    School,
    Course,
    Lecture,
)

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Lecture)
