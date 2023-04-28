from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsHome.as_view(), name='home'),
    path('<int:pk>/', ShowPost.as_view(), name='post'),
]