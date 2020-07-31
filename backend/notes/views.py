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

    @classmethod
    def get_extra_actions(cls):
        return []

class ListSchools(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        schools = list(School.objects.all())
        return Response(schools)
    
    @classmethod
    def get_extra_actions(cls):
        return []

class CoursesFromSchool(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        courses = list(Course.objects
            .filter(school=request.query_params['school'])
            .order_by('-date_started')
        )
        return Response(courses)

    @classmethod
    def get_extra_actions(cls):
        return []

class LectureFromCourse(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        lectures = list(Lecture.objects
            .filter(course=request.query_params['course'])
            .order_by('-date_given')
        )
        return Response(lectures)

    @classmethod
    def get_extra_actions(cls):
        return []

class LectureVersionFromLecture(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        lv = list(LectureVersion.objects
            .filter(predec=request.query_params['predec'])
            .order_by('-date_changed')
        )
        return Response(lv)

    @classmethod
    def get_extra_actions(cls):
        return []

class LectureVersionID(APIView):
    permisison_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response(
            list(LectureVersion.objects
            .filter(pk=request.query_params['pk']))[0]
        )

    @classmethod
    def get_extra_actions(cls):
        return []

class SchoolID(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response(
            list(School.objects
            .filter(pk=request.query_params['pk']))[0]
        )

    @classmethod
    def get_extra_actions(cls):
        return []

class CourseID(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response(
            list(Course.objects
            .filter(pk=request.query_params['pk']))[0]
        )

    @classmethod
    def get_extra_actions(cls):
        return []

class LectureID(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response(
            list(Lecture.objects
            .filter(pk=request.query_params['pk']))[0]
        )

    @classmethod
    def get_extra_actions(cls):
        return []