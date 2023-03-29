from django.shortcuts import render
from .models import Notification


# Create your views here.


def notifi(request):
    return Notification.objects.filter(userReceiver=request.user.id)


def notifications(request):
    return {'notifications': notifi(request)}


def clearNotifications(request):
    if request.method == 'DELETE':
        myset = Notification.objects.filter(userReceiver=request.user)
        for x in myset:
            x.userReceiver.remove(request.user.id)


    return render(request, "Notifications/notificationIcon.html", {'notifications' : notifi(request)})
