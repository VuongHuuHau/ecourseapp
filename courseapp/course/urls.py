
from django.urls import path, re_path, include
from rest_framework import routers
from . import views


r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='categories')
r.register('course', views.CourseViewSet, basename='courses')
r.register('user', views.UserViewSet, basename='users')
r.register('lesson', views.LessonViewSet, basename='lessons')
r.register('comments', views.CommentViewSet, basename='comments')
urlpatterns = [
    path('', include(r.urls)),
]

