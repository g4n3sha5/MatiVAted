from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Club, UserMembership, Request, BELT_ORDER, MEMBER_ORDER
from Notifications.models import Notification
from account_register.models import UserProfile
from .forms import ClubForm, MemberForm
from django.contrib.auth.decorators import login_required
from main.views import getBaseTemplate
from django.contrib import messages


# Create your views here.

def checkRequests():
    requests =  Request.objects.filter(status = 'YES')
    for item in requests:
        newMember = UserMembership(user_id=item.user_id,
                                 club_id=item.club_id,
                                   )
        newMember.save()
        item.delete()

@login_required
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

userProfiles = UserProfile.objects.all()


# def getProfilesDict(memberList, profilesDict = {}):
#     for member in memberList:
#         for profile in userProfiles.order_by(BELT_ORDER):
#             if profile.user_id == member.user_id:
#                 profilesDict[profile] = member
#
#     return profilesDict
@login_required
def clubMembers(request):
    checkRequests()
    profilesDict, requestsDict = {}, {}
    authorized = False
    try:
        membership = UserMembership.objects.get(user_id=request.user.id)
        yourClub = Club.objects.get(id=membership.club_id)
        if membership.authorized == 'FULL':
            authorized = True
        membersListT = UserMembership.objects.filter(club=yourClub).order_by(MEMBER_ORDER)
        # membersListT = yourClub.membersList().order_by(MEMBER_ORDER)
        requestListT = yourClub.requestList()

    except:
        yourClub, membersListT, isMember, requestListT = None, None, None, None

    if membersListT:
        # profilesDict = getProfilesDict(membersListT)
        for member in membersListT:
            for profile in userProfiles.order_by(BELT_ORDER):
                if profile.user_id == member.user_id:
                    profilesDict[profile] = member

    if requestListT:
        for userRequest in requestListT:
            if userRequest.status != 'REJECTED':
                requestProfile = userProfiles.get(user_id=userRequest.user_id)
                requestsDict[requestProfile] = userRequest


    context = {
        'membersList': membersListT,
        'profiles': profilesDict,
        'Club': yourClub,
        'authorized': authorized,
        'requestsDict': requestsDict,
        'base_template' : getBaseTemplate(request, "Clubs")

    }

    return render(request, "Clubs/clubMembers.html", context)
@login_required
def memberRemove(request, id):
    userDel = UserMembership.objects.get(pk=id)
    userDel.delete()
    return HttpResponseRedirect(reverse('clubMembers'))


# def editMemberPermissions(request, memberID, form):
#
#     return HttpResponseRedirect(reverse('clubMembers'))
#

def profileMemberMatcher (userID):

    profile = UserProfile.objects.get(user_id=userID)
    membership = UserMembership.objects.get(user_id=userID)
    return [profile, membership]



def memberProfile(request, clubID, userID):
    profileDict = {}
    authorizedRequest, myProfile = False, False
    ARR = profileMemberMatcher(userID)
    requestUserAuthorized = profileMemberMatcher(request.user.id)[1]
    # profile, member = profileMemberMatcher(userID)

    # user profile and membership that has been clicked
    profile, member = ARR[0], ARR[1]
    profileDict[profile] = member

    if request.method == 'POST':

        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('clubMembers'))
    else:
         form = MemberForm(instance=member)

    if requestUserAuthorized.authorized == 'FULL':
        authorizedRequest = True
    if userID == request.user.id:
        myProfile = True

    context = {
        'profile': profileDict,
        'authorizedRequest': authorizedRequest,
        'myProfile' : myProfile,
        'form' : form
    }
    return render(request, "Clubs/memberProfileModal.html", context)

def clubTrainings(request):
    context = {
        'base_template': getBaseTemplate(request, "Clubs")
    }
    return render(request, "Clubs/clubsTrainings.html", context)



@login_required
def clubsList(request):
    context = {
        'clubsList': Club.objects.all(),
        'base_template': getBaseTemplate(request, "Clubs"),

    }
    return render(request, "Clubs/clubsList.html", context)

@login_required
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

@login_required
def leaveClub(request):
    membership = UserMembership.objects.get(user_id=request.user.id)
    membership.delete()
    return redirect('/clubs/')

@login_required
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

    # return reverse('/clubMembers')



# def joinClub (request, id):
#     myClub = Club.objects.get(pk=id)
#     context = {
#         'Club': myClub
#     }
#
#     return render(request, "Clubs/singleClubView.html", context)
#
