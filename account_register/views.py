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
    try:
        membership = UserMembership.objects.get(user_id=request.user.id)
        yourClub = Club.objects.get(id = membership.club_id)

    except:
        yourClub = None

    currentProfile =  UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=currentProfile)
    context = {
        'form': form,
        'UserProfile': currentProfile,
        'club' : yourClub
    }

    if request.method == 'POST':
        template = 'profile_reloadContent'
        form = UserProfileForm(request.POST,
                               request.FILES,
                               instance = currentProfile)
                               # initial = {
                               #     'belt' : currentProfile.belt
                               # })

        if form.is_valid():
            form.save()
            context['form'] = form
            context['success'] = True
    else:
        template = 'profile'
    # UserProfile.objects.get(user=request.user)


    return render (request, f"myaccount/{template}.html", context)

def account(request):
    if request.method == "POST":

        if "delete" in request.POST:

            idd = request.user.id
            u = User.objects.get(id = idd)
            # p = UserProfile.objects.get(user_id == idd)
            u.delete()

        return HttpResponseRedirect(reverse("index"))
        # p.delete()
    context={
        'user' : request.user
    }
    return render(request, 'myaccount/account.html', context)

def magiclogin(request):
    user = authenticate(email = 'test@qa.pl', password='tester65')
    login(request, user, backend = "django.contrib.auth.backends.ModelBackend")

    return HttpResponseRedirect(reverse('profile'))
