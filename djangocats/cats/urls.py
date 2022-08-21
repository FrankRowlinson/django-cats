from django.urls import path

from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('category/<str:name>/', CategoryPage.as_view(), name='category'),
    path('addpost/', AddPostPage.as_view(), name='addpost'),
    path('post/<slug:cat_slug>/', PostPage.as_view(), name='post'),
    path('login/', LoginPage.as_view(), name='login'),
    path('signup/', SignupPage.as_view(), name='register'),
]