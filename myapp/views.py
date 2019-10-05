from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Teacher
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'myapp/home.html', context)

def home(request):
    context = {
        'teachers': Teacher.objects.all()
    }
    return render(request, 'myapp/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'myapp/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9


class TeacherListView(ListView):
    model = Teacher
    template_name = 'myapp/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'teachers'
    ordering = ['-date_posted']
    paginate_by = 9


class UserPostListView(ListView):
    model = Post
    template_name = 'myapp/user_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class UserTeacherListView(ListView):
    model = Teacher
    template_name = 'myapp/teacher_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'teachers'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class TeacherDetailView(DetailView):
    model = Teacher


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TeacherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teacher
    fields = ['teacher_name', 'course_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        teacher = self.get_object()
        if self.request.user == teacher.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TeacherDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Teacher
    success_url = '/'

    def test_func(self):
        teacher = self.get_object()
        if self.request.user == teacher.author:
            return True
        return False


def about(request):
    return render(request, 'myapp/about.html', {'title': 'about'})


def Post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, f'图片上传成功！')

    context = {
        'post_form': post_form
    }

    return render(request, 'myapp/home.html', context)
