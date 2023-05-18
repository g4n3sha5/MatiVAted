from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
# from .models import NewUser
# from django.codiscordntrib.auth.forms import UserCreationForm
# from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile
from Clubs.models import Club, UserMembership
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from WorkoutJournal.models import Technique


# # Create your views here.
#
#
def profile(request):
    currentProfile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=currentProfile)
    context = {
        'form': form,
        'UserProfile': currentProfile,
        'success': False

    }
    template = 'profile'


    if request.method == 'POST':
        template = 'profile_reloadContent'
        form = UserProfileForm(request.POST,
                               request.FILES,
                               instance=currentProfile)

        if form.is_valid():
            form.save()
            context['form'] = form
            context['success'] = True


    return render(request, f"myaccount/{template}.html", context)


def account(request):
    if request.method == "POST":

        if "delete" in request.POST:
            idd = request.user.id
            u = User.objects.get(id=idd)

            u.delete()

        return HttpResponseRedirect(reverse("index"))
        # p.delete()
    context = {
        'user': request.user
    }
    return render(request, 'myaccount/account.html', context)


def magiclogin(request):
    user = authenticate(email='test2@qa.pl', password='test2@qa.pl')

    login(request, user, backend="allauth.account.auth_backends.AuthenticationBackend")

    return HttpResponseRedirect(reverse('profile'))
