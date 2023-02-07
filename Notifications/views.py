from django.shortcuts import render
from .models import Notification
# Create your views here.
def notifications (request):
    myNotifications = Notification.objects.filter(userReceiver = request.user.id)


    context = {
        'notifications' : myNotifications
    }
    return render