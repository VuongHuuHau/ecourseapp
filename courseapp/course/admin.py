from django.contrib import admin
from .models import Category, Lesson, Course, Tag
from django.utils.html import mark_safe
from django import forms
from django import forms
from ckeditor_uploader.widgets \
    import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
     description= forms.CharField(widget=CKEditorUploadingWidget)

class Meta:
    model = Course
fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'updated_date', 'active']
    search_fields = ['subject', 'description']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, app):
        if app.image:
            return mark_safe(f"<img width='120' src='{app.image.url}' />")

    class Media:
        css = {
            'all': ['/static/css/style.css']
        }


admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Tag)
