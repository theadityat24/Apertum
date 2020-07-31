from django.contrib.auth.models import User
from .models import (
    School,
    Course,
    Lecture,
    LectureVersion,
)
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'user']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = [
            'school', 'user', 'name',
            'description', 'date_started',
            'date_ended'
        ]

class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            'date_given', 'date_added', 'course',
            'user', 'name', 'note_file'
        ]

class LectureVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LectureVersion
        fields = [
            'predec', 'date_changed',
            'user', 'note_file',
        ]