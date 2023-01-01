from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
# from .models import NewUser
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile

# # Create your views here.
#
#
def myAccount(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UserProfileForm()

    # UserProfile.objects.get(user=request.user)
    context = {
        'form' : form,
        'UserProfile' : UserProfile.objects.get(user=request.user)
    }

    return render (request, "myaccount/myaccount.html", context)