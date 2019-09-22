from django import forms
from .models import Post, Teacher


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['cover_image']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_image']
