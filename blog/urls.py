from django.urls import path
from .views import hello_blog

urlpatterns = [
    path('', hello_blog, name='hello_blog'),
]