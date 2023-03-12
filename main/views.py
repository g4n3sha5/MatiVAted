from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


def index (request):
    return render(request, "main/index.html", {})

# def renderFromFooter(request, app, view):
#
#
#     return HttpResponseRedirect(reverse(f"{view}"))