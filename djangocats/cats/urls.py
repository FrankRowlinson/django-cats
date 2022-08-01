from django.urls import path

from .views import *


urlpatterns = [
    path('', main, name='home'),
    path('pics/<str:category>/', pictures, name='pics'),
    path('about/', about, name='about'),
]