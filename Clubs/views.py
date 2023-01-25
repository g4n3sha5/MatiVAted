from django.shortcuts import render, redirect
from .models import Club, UserMembership, Request
from account_register.models import UserProfile
from .forms import ClubForm
from django.db.models import Case, When, Value

from django.contrib import messages


# Create your views here.
def ClubsIndex(request):
    try:
        yourClub = Club.objects.get(creator=request.user)

    except:
        yourClub = None

    form = ClubForm(instance=yourClub)

    context = {
        'form': form,
        'Club': yourClub,
        'user': request.user,
    }
    if request.method == 'POST':
        yourClub, created = Club.objects.get_or_create(creator=request.user)
        form = ClubForm(request.POST, request.FILES, instance=yourClub)

        if form.is_valid():
            instance = form.save(commit=False)
            yourClub.creator = request.user
            UserMembership(user=request.user, authorized='FULL', memberType='Head', club=yourClub).save()
            instance.save()

            context['form'] = form
            context['Club'] = yourClub
            context['success'] = True
    else:
        template = 'index'

    if request.META.get('HTTP_HX_REQUEST'):
        template = 'Clubs_reloadContent'

    return render(request, f"Clubs/{template}.html", context)


def clubMembers(request):
    BELT_ORDER = Case(
        When(belt='Black Belt', then=Value(1)),
        When(belt='Brown Belt', then=Value(2)),
        When(belt='Purple Belt', then=Value(3)),
        When(belt='Blue Belt', then=Value(4)),
        When(belt='White Belt', then=Value(5)),
        When(belt='No Info', then=Value(6)),
    )
    MEMBER_ORDER = Case(
        When(memberType='Head', then=Value(1)),
        When(memberType='Instructor', then=Value(2)),
        When(memberType='Professor', then=Value(3)),
        When(memberType='Student', then=Value(4)),
    )
    try:
        yourClub = Club.objects.get(creator=request.user)
        # membersList = UserMembership.objects.filter(club=yourClub).order_by('memberType').values()
        membersList = UserMembership.objects.filter(club=yourClub).order_by(MEMBER_ORDER)
    except:
        yourClub = None
        membersList = None
        print("YOU DONT HAVE A CLUB!")


    profilesDict = {

    }

    for profile in UserProfile.objects.all().order_by(BELT_ORDER):
        for member in membersList:
            if profile.user_id == member.user_id:
                profilesDict[profile] = member

    print(profilesDict)
    # UserProfile.objects.all().order_by('belt')
    context = {
        'membersList': membersList,
        'profiles' : profilesDict
    }

    # for x in context['profiles']:
    #     print(x.belt)
    return render(request, "Clubs/clubMembers.html", context)


def clubsTrainings(request):
    context = {}
    return render(request, "Clubs/clubsTrainings.html", context)


def clubsSchedule(request):
    context = {}
    return render(request, "Clubs/clubsSchedule.html", context)


def clubsList(request):
    context = {
        'clubsList': Club.objects.all(),

    }
    return render(request, "Clubs/clubsList.html", context)


def singleClubView(request, id):
    myClub = Club.objects.get(pk=id)
    context = {
        'Club': myClub
    }

    userRequest = Request.objects.filter(user=request.user, club=myClub)
    if userRequest:
        context['alreadySent'] = True
        return render(request, "Clubs/singleClubView.html", context)

    if request.method == 'POST':
        userRequest = Request(status='NO', user=request.user, club=myClub)
        userRequest.save()

    return render(request, "Clubs/singleClubView.html", context)

# def joinClub (request, id):
#     myClub = Club.objects.get(pk=id)
#     context = {
#         'Club': myClub
#     }
#
#
#
#
#     return render(request, "Clubs/singleClubView.html", context)
#
