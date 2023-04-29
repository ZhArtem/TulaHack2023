from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreate.as_view(), name='post_create'),

    path('contact/', contact, name='contact'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]