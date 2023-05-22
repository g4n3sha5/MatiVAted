from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Club, UserMembership, Request, BELT_ORDER, MEMBER_ORDER
from WorkoutJournal.models import TrainingSession
from account_register.models import UserProfile
from .forms import ClubForm, MemberForm
from django.contrib.auth.decorators import login_required
from main.views import getBaseTemplate
from django.contrib import messages
from main.views import userAuth

# Create your views here.
def userClub( userID):
    return UserMembership.objects.get(user_id=userID).club

def userHasClub(request):
    try:
        userClub(request.user.id)
        return True
    except:
        return False


@login_required
@userAuth
def ClubsIndex(request):

    try:
        # find what club is the user in
        club = userClub(request.user.id)
        yourClub = Club.objects.get(id=club.club_id)


    except:
        yourClub,club  = None, None


    context = {
        'form': ClubForm(instance=yourClub),
        'Club': yourClub,
        'user': request.user,
        'authorized' : request.session.get('authorized'),
        'success' : False
    }
    template = 'index'

    if request.method == 'POST':

        if club:
            yourClub = Club.objects.get(id=club.club_id)

        else:
            yourClub = Club.objects.create()

        form = ClubForm(request.POST, request.FILES, instance=yourClub)

        if form.is_valid():

            instance = form.save(commit=False)
            if not club:
                yourClub.creator = request.user
                UserMembership(user_id=request.user.id, authorized='FULL', memberType='Head', club=yourClub).save()
            instance.save()

            context['form'] = form
            context['Club'] = yourClub
            context['success'] = True



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
@userAuth
def clubMembers(request):
    profilesDict, requestsDict = {}, {}
    try:
        membership = UserMembership.objects.get(user_id=request.user.id)
        yourClub = Club.objects.get(id=membership.club_id)
        membersListT = UserMembership.objects.filter(club=yourClub).order_by(MEMBER_ORDER)
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
        'authorized': request.session.get('authorized'),
        'requestsDict': requestsDict,
        'userHasClub' : userHasClub(request),
        'base_template' : getBaseTemplate(request, "Clubs")

    }

    return render(request, "Clubs/clubMembers.html", context)

@login_required
def memberRemove(request, id):
    userDel = UserMembership.objects.get(pk=id)
    userDel.delete()
    return HttpResponseRedirect(reverse('clubMembers'))




def profileMemberMatcher (userID):

    profile = UserProfile.objects.get(user_id=userID)
    membership = UserMembership.objects.get(user_id=userID)
    return [profile, membership]



@userAuth
def memberProfile(request, clubID, userID):
    profileDict = {}
    authorizedRequest, myProfile = False, False
    ARR = profileMemberMatcher(userID)

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


    if userID == request.user.id:
        myProfile = True

    context = {
        'profile': profileDict,
        'authorizedRequest': request.session.get('authorized'),
        'myProfile' : myProfile,
        'form' : form
    }
    return render(request, "Clubs/memberProfileModal.html", context)

def clubTrainings(request):
    uid = request.user.id
    try:
        userclub = userClub(uid)
    except:
        userclub = None
    sessionsList = TrainingSession.objects.filter(club=userclub).order_by('-id')

    for index, item in enumerate(reversed(sessionsList), start=1):
        setattr(item, 'orderIndex', index)
        if request.user in item.participants.all():
            setattr(item, 'participant', True)


    p = Paginator(sessionsList, 6)
    page = request.GET.get('page')
    sessions = p.get_page(page)


    context = {
        'base_template': getBaseTemplate(request, "Clubs"),
        'userHasClub': userHasClub(request),
        'sessionsList': sessions
    }
    return render(request, "Clubs/clubsTrainings.html", context)

def clubTraining(request, trainingID, action):
    training = TrainingSession.objects.get(id=trainingID)
    if request.method == "POST":
        if action == "join":
            training.participants.add(request.user)
        if action == "leave":
            training.participants.remove(request.user)

    return HttpResponseRedirect(reverse(clubTrainings))

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
        'userHasClub' : userHasClub(request)
    }

    try:
        userMembership = UserMembership.objects.get(user=request.user.id)
        # context['userHasClub'] = True
    except:
        userMembership = None

    try:
        userRequest = Request.objects.get(user_id=request.user.id)
        context['alreadySent'] = True

        # return render(request, "Clubs/singleClubView.html", context)

    except:
        userRequest = False



    if request.method == 'POST':
        userRequest = Request(status='NO', user_id=request.user.id, club=myClub)
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
        newMember = UserMembership(user_id=myrequest.user_id,
                                   club_id=myrequest.club_id,
                                   )
        newMember.save()
        myrequest.delete()

    if request.method == 'DELETE':
        # myrequest.status = 'REJECTED'
        myrequest.delete()


    return clubMembers(request)



# def joinClub (request, id):
#     myClub = Club.objects.get(pk=id)
#     context = {
#         'Club': myClub
#     }
#
#     return render(request, "Clubs/singleClubView.html", context)
#
