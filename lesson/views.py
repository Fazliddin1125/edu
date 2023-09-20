from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Teacher, Document, Video
# Create your views here.
class HomePageView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers
        }
        return render(request, 'index.html', context)

class TeachersView(View):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        # documents = get_list_or_404(Document, author__id=id)
        author = get_object_or_404(Teacher, id=id)
        documents = Document.objects.filter(author=author)
        videos = Video.objects.filter(teacher=author)
        context = {
            'teacher': teacher,
            'documents': documents,
            'videos': videos
        }
        return render(request, 'teachers.html', context)
