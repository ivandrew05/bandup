from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(default='bandup/media/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Teacher(models.Model):
    teacher_image = models.ImageField(default='bandup/media/default.jpg', upload_to='profile_pics')
    teacher_name = models.CharField(max_length=100)
    years_of_playing = models.CharField(max_length=100)
    course_content = models.CharField(max_length=5000)
    charging_fee = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name

    def get_absolute_url(self):
        return reverse('teacher-detail', kwargs={'pk': self.pk})

