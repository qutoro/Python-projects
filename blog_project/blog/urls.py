from django.urls import path
from .views import *
urlpatterns = [
    path('', register, name='register'),
    path('chat/', create_post, name='chat'),
    path('<int:post_id>/comments/', comment, name='comment'),
]