# Generated by Django 5.0.3 on 2024-04-05 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
    ]
