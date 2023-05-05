from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from functools import wraps
from Clubs.models import UserMembership


def index(request):

    return render(request, "main/index.html")


def getBaseTemplate(request, app):
    if not request.META.get('HTTP_HX_REQUEST'):
        base_template = f"{app}/base.html"
    else:
        base_template = "main/partial.html"

    return base_template


def userAuth(func):
    @wraps(func)
    def wrapped(request, *args, **kwargs):
        authorized = request.session.get('authorized')
        if authorized:
            return func(request, *args, **kwargs)

        try:
            authorized = UserMembership.objects.get(user_id=request.user.id).authorized
        except:
            authorized = False

        request.session['authorized'] = authorized

        return func(request, *args, **kwargs)


    return wrapped