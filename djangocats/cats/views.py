from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def main(request):
    context = {'title': 'coolcats! main page'}
    return render(request, 'cats/index.html', context=context)

def about(request):
    context = {'title': 'About coolcats!'}
    return render(request, 'cats/about.html', context=context)

def pictures(request, category):
    if category not in ("funny", "serious", "cute"):
        raise Http404
        
    return HttpResponse(f"""<h1>Here you can see all pictures of cats 
    in category {category}</h1>""")

def page_not_found(request, exception):
    return HttpResponseNotFound("We don't have such kitties :C")