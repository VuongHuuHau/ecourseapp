from rest_framework import viewsets, generics
from course.models import  Category, Course, Lesson
from course import serializers , paginations


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializers_class=serializers.CourseSerializer

