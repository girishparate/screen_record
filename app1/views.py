from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class Home(APIView):
    @staticmethod
    def get(request):
        return render(request, 'app1.html')
