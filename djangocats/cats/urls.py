from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', cache_page(60)(MainPage.as_view()), name='home'),
    path('about/', about, name='about'),
    path('category/<str:name>/', CategoryPage.as_view(), name='category'),
    path('addpost/', AddPostPage.as_view(), name='addpost'),
    path('post/<slug:cat_slug>/', PostPage.as_view(), name='post'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', SignupPage.as_view(), name='signup'),
]