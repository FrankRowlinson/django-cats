from django.urls import path

from .views import *


urlpatterns = [
    path('', main, name='home'),
    path('about/', about, name='about'),
    path('category/<str:name>/', show_category, name='category'),
    path('addpost/', add_post, name='addpost')
]