from rest_framework import viewsets, generics
from .models import  Category, Course, Lesson
from . import serializers


class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer
