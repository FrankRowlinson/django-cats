from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse("Main page filled with beautiful cats")

def pictures(request):
    return HttpResponse("<h1>Here you can see all pictures of cats</h1>")