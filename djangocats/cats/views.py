from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import *
from cats.forms import *


category_names = Category.objects.names()


class MainPage(ListView):
    model = Cat
    template_name = 'cats/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'coolcats! Main page'}
    paginate_by = 10

    def get_queryset(self):
        return Cat.objects.filter(is_public=True)


class CategoryPage(ListView):
    model = Cat
    template_name = 'cats/category.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 20

    def get_queryset(self):
        return Cat.objects.filter(category__name=self.kwargs['name'], is_public=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"coolcats! {self.kwargs['name'].capitalize()}" 
        return context


class PostPage(DetailView):
    model = Cat
    template_name = 'cats/post.html'
    slug_url_kwarg = 'cat_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context['post'].title
        return context


class AddPostPage(CreateView):
    form_class = AddPostForm
    template_name = 'cats/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add kitty cat to our database!"
        return context


class SignupPage(CreateView):
    form_class = UserCreationForm
    template_name = 'cats/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Become a Kittizen!"
        return context


class LoginPage(DetailView):
    pass


def about(request):
    context = {
        'title': 'About coolcats!',
        'picture_count': Cat.objects.count(),
        }
    return render(request, 'cats/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("We don't have such kitties :C")


# def main(request):
#     context = {
#         'title': 'coolcats! Main page',
#         'new': Cat.objects.new(3),
#     }
#     return render(request, 'cats/index.html', context=context)


# def show_category(request, name):
#     if name not in category_names:
#         raise Http404
#     posts = Cat.objects.by_category(name)

#     context = {
#         'title': f'coolcats! {name.capitalize()}',
#         'name': name,
#         'posts': posts,
#     } 
#     return render(request, 'cats/category.html', context=context)


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     context = {
#         'form': form,
#         'title': "Add kitty cat to our database!",
#     }
#     return render(request, 'cats/addpost.html', context=context)