# Generated by Django 4.2.5 on 2023-09-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_teacher_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(default='photo.jpg', upload_to='images/'),
        ),
    ]
