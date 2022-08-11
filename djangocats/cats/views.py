from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from cats.forms import *


category_names = [category.name for category in Category.objects.order_by('name')]


def main(request):
    context = {
        'title': 'coolcats! Main page', 
        'rand_cats': Cat.objects.order_by('?')[:3]
    }
    return render(request, 'cats/index.html', context=context)

def about(request):
    context = {
        'title': 'About coolcats!',
        'picture_count': Cat.objects.count(),
        }
    return render(request, 'cats/about.html', context=context)

def show_category(request, name):
    if name not in category_names:
        raise Http404
    posts = Cat.objects.filter(category=Category.objects.get(name=name))
    context = {
        'title': f'coolcats! {name.capitalize()}',
        'name': name,
        'picture_count': posts.count(),
        'posts': posts,
    } 
    return render(request, 'cats/category.html', context=context)

def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'title': "Add kitty cat to our database!",
    }
    return render(request, 'cats/addpost.html', context=context)

def page_not_found(request, exception):
    return HttpResponseNotFound("We don't have such kitties :C")