from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from .task import *

# Create your views here.
class StartVideo(APIView):
    @staticmethod
    def get(request):
        return render(request, 'sample.html')

    @staticmethod
    def post(request):
        ticket = Ticket.objects.create(data_obj=request.POST['data_obj'], user=request.user)
        ticket.save()
        scrn.apply_async(args=[ticket.id, str(request.user)], countdown=0)

        return JsonResponse({'success':"success"})


class StopView(APIView):
    @staticmethod
    def get(request):
        ticket = Ticket.objects.filter(user=request.user).order_by('id')
        ticket = ticket.reverse()[0]
        ticket.video_stop = True
        ticket.save()       
        return JsonResponse({'success':"success"})