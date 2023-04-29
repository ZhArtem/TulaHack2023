from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
]