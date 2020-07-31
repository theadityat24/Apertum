"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from notes import views

router = routers.DefaultRouter()
router.register(r'^users/$', views.ListUsers)
router.register(r'^schools/$', views.ListSchools)
router.register(r'^schools/courses/{school}/$', views.CoursesFromSchool)
router.register(r'^courses/lectures/{course}/$', views.LectureFromCourse)
router.register(r'^lectures/version/{lecture}/$', views.LectureVersionFromLecture)
router.register(r'^versionid/{pk}/$', views.LectureVersionID)
router.register(r'^schoolid/{pk}/$', views.SchoolID)
router.register(r'^courseid/{pk}/$', views.CourseID)
router.register(r'^lectureid/{pk}/$', views.LectureID)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_ramework')),
]
