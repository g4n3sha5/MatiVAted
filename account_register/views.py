from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
# from .models import NewUser
# from django.codiscordntrib.auth.forms import UserCreationForm
# from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile
from Clubs.models import Club, UserMembership
from WorkoutJournal.models import Technique
# # Create your views here.
#
#
def myAccount(request):
    try:
        # yourClub = Club.objects.get(creator=request.user)

        # yourClub = UserMembership.getMyUsersClub(request)
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
        # 'techniques' : Technique.objects.all()
    }

    if request.method == 'POST':
        template = 'myaccount_reloadContent'
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
        template = 'myaccount'
    # UserProfile.objects.get(user=request.user)


    return render (request, f"myaccount/{template}.html", context)