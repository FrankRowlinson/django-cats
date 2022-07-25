from django.urls import path

from .views import *


urlpatterns = [
    path('', main),
    path('pics/<str:category>/', pictures),
]