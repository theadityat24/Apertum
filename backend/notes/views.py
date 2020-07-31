from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import (
    School,
    Course,
    Lecture,
    LectureVersion,
)

class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class ListSchools(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        schools = [s.name for s in School.objects.all()]
        return Response(schools)

