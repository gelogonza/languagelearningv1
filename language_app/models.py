from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    audio_url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
    
class Translation(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    original_text = models.TextField()
    translated_text = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    completed_lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.user.username

