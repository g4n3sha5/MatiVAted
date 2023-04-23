from django.shortcuts import render
from .models import Notification
from .forms import ContactForm
from django.core.mail import send_mail
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


# def reportS1uggestion (request):
#     return {'suggestForm' : ContactForm()}

def sendSuggestion (request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():


            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            send_mail(title, content, "no-reply@mativated.com", ['kmatysiak-it@outlook.com'])
            sent = True

        context = {
            'sent' : sent,
            'suggestForm' : ContactForm()
        }
        return render (request, "main/bugModal.html", context)




