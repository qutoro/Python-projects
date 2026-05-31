from django.urls import path,include

urlpatterns = [
    path('hello/', include("hello.urls")),
]