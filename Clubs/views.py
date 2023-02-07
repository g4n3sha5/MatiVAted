from django.shortcuts import render, redirect, reverse
from .models import Club, UserMembership, Request
from Notifications.models import Notification
from account_register.models import UserProfile
from .forms import ClubForm
from django.db.models import Case, When, Value

from django.contrib import messages


# Create your views here.

def checkRequests():

    requests =  Request.objects.filter(status = 'YES')
    for item in requests:
        newMember = UserMembership(user_id=item.user_id,
                                 club_id=item.club_id,
                                   )
        newMember.save()
        print(newMember)
        print(item)
        item.delete()


def ClubsIndex(request):

    authorized = True
    try:
        # find what club is the user in
        membership = UserMembership.objects.get(user_id=request.user.id)
        yourClub = Club.objects.get(id=membership.club_id)
        # yourClub = Club.objects.get(creator=request.user)
        if membership.authorized != 'FULL':
            authorized = False

    except:
        yourClub = None

    form = ClubForm(instance=yourClub)

    context = {
        'form': form,
        'Club': yourClub,
        'user': request.user,
        'authorized': authorized
    }
    if request.method == 'POST':
        yourClub, created = Club.objects.get_or_create(id=membership.club_id)
        # yourClub, created = Club.objects.get_or_create(creator=request.user)
        form = ClubForm(request.POST, request.FILES, instance=yourClub)

        if form.is_valid():
            instance = form.save(commit=False)
            if not membership:
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
    print("index")
    checkRequests()

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
    profilesDict = {

    }
    requestsDict = {

    }
    authorized = False
    try:
        membership = UserMembership.objects.get(user_id=request.user.id)
        yourClub = Club.objects.get(id=membership.club_id)
        if membership.authorized == 'FULL':
            authorized = True
        # membersList = UserMembership.objects.filter(club=yourClub).order_by('memberType').values()
        membersList = UserMembership.objects.filter(club=yourClub).order_by(MEMBER_ORDER)
        requestList = Request.objects.filter(club=yourClub)

    except:
        yourClub, membersList, isMember, requestList = None, None, None, None

    userProfiles = UserProfile.objects.all()
    if yourClub and membersList:
        for profile in userProfiles.order_by(BELT_ORDER):
            for member in membersList:
                if profile.user_id == member.user.id:
                    profilesDict[profile] = member

    if requestList:
        for userRequest in requestList:
            if userRequest.status != 'REJECTED':
                requestProfile = userProfiles.get(user_id=userRequest.user_id)
                requestsDict[requestProfile] = userRequest

        # for profile in UserProfile.objects.all().order_by(BELT_ORDER):
        #     for member in membersList:
        #         if profile.user_id == member.user_id:
        #             # if profile.user_id == request.user_id:
        #             #     profilesDict[profile] = [member, request]

        # profilesDict[profile] = [member]

    context = {
        'membersList': membersList,
        'profiles': profilesDict,
        'Club': yourClub,
        'authorized': authorized,
        'requestsDict': requestsDict

    }

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
        'Club': myClub,
        'userHasClub': False
    }

    try:
        userMembership = UserMembership.objects.get(user=request.user)
        context['userHasClub'] = True
    except:
        userMembership = None

    try:
        userRequest = Request.objects.get(user=request.user)
        context['alreadySent'] = True
        # return render(request, "Clubs/singleClubView.html", context)
    except:
        userRequest = False


    if request.method == 'POST':
        userRequest = Request(status='NO', user=request.user, club=myClub)
        userRequest.save()
        context['alreadySent'] = True
    return render(request, "Clubs/singleClubView.html", context)


def leaveClub(request):
    membership = UserMembership.objects.get(user_id=request.user.id)
    membership.delete()
    return redirect('/clubs/')


def handleRequest(request, requestID):
    myrequest = Request.objects.get(id=requestID)

    if request.method == 'POST':
        myrequest.status = 'YES'
        myrequest.save()
    if request.method == 'DELETE':
        myrequest.status = 'REJECTED'
        myrequest.save()

    return clubMembers(request)
    # return reverse('/clubMembers')



# def joinClub (request, id):
#     myClub = Club.objects.get(pk=id)
#     context = {
#         'Club': myClub
#     }
#
#     return render(request, "Clubs/singleClubView.html", context)
#
