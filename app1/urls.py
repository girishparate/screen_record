from .views import *
from django.urls import path

urlpatterns = [
    path('home', Home.as_view(), name='home')
]
