from .models import Course,Category,Lesson
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    def to_representation(self,  instance):
        rep= super().to_representation(instance)
        rep['image']=instance.image.url

        return rep
    class Meta:
        model= Course
        fiel=['id','subject','image',' created_date']