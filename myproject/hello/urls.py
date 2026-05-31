from django.urls import path, re_path
from .views import *
from . import views


urlpatterns = [
    path('', hello_view),
    path('items/', hello_json),
    path("setcookie/",set_cookies),
    path("getcookie", get_cookies),
    path("blogs/<int:id>/", hello_blogs),
    path("user/<str:name>/", hello_address),
    path("news/<str:name>/", hello_news),
    path('aboutus/', hello_view2),
    path("<int:id>/", hello_id),
    path("user/<str:username>/", hello_user),
    path("info/", hello_info),
    re_path(r'^(?P<text>[a-zA-Z0-9]+)/$', hello_numbers)
]
