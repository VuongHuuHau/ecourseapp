
from django.urls import path, re_path, include
from rest_framework import routers
from course import views




r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='categories')
r.register('course', views.CategoryViewSet, basename='course')
urlpatterns = [
    path('', include(r.urls)),
]

