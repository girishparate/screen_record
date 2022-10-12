from .views import *
from django.urls import path

urlpatterns = [
    path('start', StartVideo.as_view(), name='start'),

    path('stop', StopView.as_view(), name='stop')
]
