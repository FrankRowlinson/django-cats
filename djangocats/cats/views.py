from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from cats.models import *


categories = Category.objects.all()
category_names = [category.name for category in categories.order_by('name')]


def main(request):
    context = {
        'title': 'coolcats! main page', 
        'categories': categories
    }
    return render(request, 'cats/index.html', context=context)

def about(request):
    context = {
        'title': 'About coolcats!',
        'category_count': categories.count(), 
        'picture_count': Cat.objects.count(),
        'categories': categories
        }
    return render(request, 'cats/about.html', context=context)

def show_category(request, name):
    if name not in category_names:
        raise Http404
        
    return HttpResponse(f"""<h1>Here you can see all pictures of cats 
    in category {name}</h1>""")

def page_not_found(request, exception):
    return HttpResponseNotFound("We don't have such kitties :C")