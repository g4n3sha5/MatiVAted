from django.shortcuts import render, redirect
from .models import NewUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
# Create your views here.


def acc_register(response):
    print("response.method", response.method)

    if response.method == "POST":
        form = NewUser(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            messages.success(response, "Registration successfull")
            redirect("/")
    else:
        form = NewUser()

    return render(response, "register/register.html", {"form": form})

def acc_login(response):
    pass