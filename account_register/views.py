# from django.shortcuts import render, redirect
# from .models import NewUser
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
#
# # Create your views here.
#
#
# def acc_register(request):
#     if request.method == "POST":
#         form = NewUser(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Registration successfull")
#     else:
#         form = NewUser()
#
#     return render(request, "account/signup.html", {"form": form})
