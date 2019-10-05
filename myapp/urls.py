from . import views
from django.urls import path
from .views import (PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, 
TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView)


urlpatterns = [
    # path("", PostListView.as_view(), name="myapp-home"),
    path("", TeacherListView.as_view(), name="myapp-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    # path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("teacher/<int:pk>/", TeacherDetailView.as_view(), name="teacher-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
#     path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("teacher/<int:pk>/update/", TeacherUpdateView.as_view(), name="teacher-update"),
    path("teacher/<int:pk>/update/",
         TeacherUpdateView.as_view(), name="teacher-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("teacher/<int:pk>/delete/",
         TeacherDeleteView.as_view(), name="teacher-delete"),
    path("about/", views.about, name="myapp-about"),
]
