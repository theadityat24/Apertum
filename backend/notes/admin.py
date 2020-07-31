from django.contrib import admin
from .models import (
    School,
    Course,
    Lecture,
    LectureVersion
)

admin.site.register(School)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(LectureVersion)
