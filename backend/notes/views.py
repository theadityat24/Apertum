from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import (
    School,
    Course,
    Lecture,
    LectureVersion,
)
from .serializers import (
    UserSerializer,
    SchoolSerializer,
    CourseSerializer,
    LectureSerializer,
    LectureVersionSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAdminUser]

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permissions_classes = [permissions.AllowAny]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-date_started')
    serializer_class = CourseSerializer
    permissions_classes = [permissions.AllowAny]

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all().order_by('-date_given')
    serializer_class = LectureSerializer
    permissions_classes = [permissions.AllowAny]

class LectureVersionViewSet(viewsets.ModelViewSet):
    queryset = LectureVersion.objects.all().order_by('-date_changed')
    serializer_class = LectureVersionSerializer
    permissions_classes = [permissions.AllowAny]

