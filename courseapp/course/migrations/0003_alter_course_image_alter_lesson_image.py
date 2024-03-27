# Generated by Django 5.0.3 on 2024-03-27 15:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
