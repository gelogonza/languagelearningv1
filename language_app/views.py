from django.shortcuts import render
from .models import Lesson

def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'language_app/lesson_detail.html', {'lesson': lesson})

def quiz_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    # You can add quiz logic here
    return render(request, 'language_app/quiz_detail.html', {'lesson': lesson})
