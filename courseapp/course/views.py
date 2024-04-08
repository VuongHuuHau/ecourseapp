from xml.sax import parse

from rest_framework import viewsets, generics, status, parsers, permissions
from .models import Category, Course, Lesson,User
from . import paginators, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class =serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator


    def get_queryset(self):
        queryset = self.queryset
        if self.action == 'list':
            q = self.request.query_params.get('q')
            if q:
                queryset = queryset.filter(subject__icontains=q)
            cate_id= self.request.query_params.get('category_id')
            if cate_id:
                queryset = queryset.filter(category_id=cate_id)

        return queryset
    @action(methods=['get'], url_path='lessons',detail=True)
    def get_lessons(self , request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)

        q = self.request.query_params.get('q')
        if q:
            lessons = lessons.filter(subject__icontains=q)

        return Response(serializers.LessonSerializer(lessons, many=True).data,
                        status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related('tag').filter(active=True)
    serializer_class = serializers.LessonDetailSerializer

    @action(methods=['get'], url_path='comment', detail=True)
    def get_comment(self, request, pk):
        comment = self.get_object().comment_set.select_related('user').order_by("-id")
        paginator = paginators.CommentPaginator()
        page = paginator.paginate_queryset(comment, request)
        if page is not None:
            serializer = serializers.CommentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        return Response(serializers.CommentSerializer(comment, many=True).data,
                        status=status.HTTP_200_OK)


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser,]

    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='currrent-user',detail= False)
    def get_current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)