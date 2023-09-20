from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Science(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("science_data", args=[self.name])


class Teacher(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    level = models.CharField(max_length=50)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    photo = models.ImageField(default='images/photo.jpg', upload_to='images/')

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse("teacher_data", args=[self.firstname])

class Document(models.Model):
    title = models.CharField(max_length=400)
    pptx_file = models.FileField(upload_to='pptx_file')
    type = models.CharField(max_length=20)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=400)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

