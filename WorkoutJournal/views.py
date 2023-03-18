from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import TrainingSession, Technique, Suggestion, User
from Clubs.models import UserMembership, Club
from .forms import TrainingSessionForm, addTechniqueForm, descriptionSuggestion
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from main.views import getBaseTemplate

# Create your views here.

# def countAllHours (user):
#

#     return myDict
@login_required
def BJJournalIndex(request):

    template = "BJR_index.html"
    if request.META.get('HTTP_HX_REQUEST'):
        template =  "BJR_index_reloadContent.html"
    # count = countAllHours(request.user)
    user = request.user
    total = TrainingSession.objects.filter(user_id=user.id).count()
    gi = TrainingSession.objects.filter(user_id=user.id, type="GI").count()
    nogi = TrainingSession.objects.filter(user_id=user.id, type="NOGI").count()
    gym = TrainingSession.objects.filter(user_id=user.id, type="GYM").count()
    LAST_MONTH = datetime.today() - timedelta(days=30)
    last30days = TrainingSession.objects.filter(user_id=user.id, date__gte=LAST_MONTH).count()


    context = {
        'total': total,
        'gi': gi,
        'nogi': nogi,
        'gym': gym,
        'last30days': last30days
    }
    return render(request, f"BJJournal/{template}", context)

    # context = {
    #     'user': request.user,
    #     'total' : count['total'],
    #     'gi' : count['gi'],
    #     'nogi' : count['nogi'],
    #     'gym' : count['gym'],
    #     'last30days' : count['last30days'],}}
    #
    # }




@login_required
def dashboard(request):
    context = {

    }

    return render(request, "BJJournal/BJR_dashboard.html", context)

@login_required
def addSession(request):
    authorized = False
    uid = request.user.id

    try:
        membership = UserMembership.objects.get(user_id=uid)
        yourClub = Club.objects.get(id=membership.club_id)
        authorized = membership.authorized
    except:
        membership, yourClub = None, None


    if authorized == "FULL" or "TRAININGS":
        authorized = True

    if request.method == 'POST':
        form = TrainingSessionForm( request.POST, auto_id=True)

        if form.is_valid():
            instance = form.save(commit=False)

            instance.user = request.user
            instance.save()
            messages.success(request, "Added your session")
            techn = form.cleaned_data.get('techniques')
            for t in techn:
                instance.techniques.add(t.id)

            return HttpResponseRedirect('/addSession')
        else:
            messages.error(request, "Invalid form. ")

    else:
        form = TrainingSessionForm()



    context = {
        'form': form,
        'Club': yourClub,
        'techniquesList': Technique.objects.all(),
        'base_template' : getBaseTemplate(request, "BJJournal"),
        'authorized' : authorized

    }


    template_name = "BJJournal/BJR_addSession/BJR_addSession.html"

    return render(request, template_name , context)

@login_required
def editSession(request, id=None, orderIndex=None):
    try:
        membership = UserMembership.objects.get(user_id=request.user.id)
        yourClub = Club.objects.get(id=membership.club_id)
    except:
        membership, yourClub = None, None

    Session = TrainingSession.objects.get(pk=id)

    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=Session)
        instance = form.save(commit=False)
        if form.is_valid():
            instance.techniques.clear()
            techn = form.cleaned_data.get('techniques')
            for t in techn:
                instance.techniques.add(t.id)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/yourSessions')
    else:
        form = TrainingSessionForm(instance=Session)

    context = {
        'Club': yourClub,
        'id': id,
        'form': form,
        'orderIndex': orderIndex,
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_editSession.html", context)

@login_required
def removeSession(request, id):
    session = TrainingSession.objects.get(pk=id)
    session.delete()
    return HttpResponseRedirect('/yourSessions')

@login_required
def yourSessions(request):
    sessionsList = TrainingSession.objects.filter(user_id = request.user.id).order_by('-id')
    for index, item in enumerate(reversed(sessionsList), start=1):
        setattr(item, 'orderIndex', index)

    p = Paginator(sessionsList, 6)
    page = request.GET.get('page')
    sessions = p.get_page(page)

    form = TrainingSessionForm()

    context = {
        'form': form,
        'sessionsList': sessions,
        'base_template' : getBaseTemplate(request, "BJJournal")
    }
    # html = render_to_string('BJJournal/BJR_yourSessions.html', context)
    # return JsonResponse(html, safe=False)
    return render(request, "BJJournal/BJR_yourSessions/BJR_yourSessions.html", context)

@login_required
def singleSessionView(request, id, orderIndex):
    Session = TrainingSession.objects.get(pk=id)
    context = {
        'session': Session,
        'orderIndex': orderIndex,
        'form': TrainingSessionForm(instance=Session)
    }
    return render(request, "BJJournal/BJR_yourSessions/singleSessionView.html", context)

@login_required
def techniques(request):
    if request.method == 'POST':
        form = addTechniqueForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Added your technique")
            return redirect('/techniques')

        else:
            messages.error(request, "Invalid form. ")

    else:
        form = addTechniqueForm()

    context = {
        'TechForm': form,
        'techniquesList': Technique.objects.all(),
        'base_template': getBaseTemplate(request, "BJJournal")
    }
    return render(request, "BJJournal/BJR_Techniques.html", context)

@login_required
def singleTechniqueView(request, id):
    techniqueObj = Technique.objects.get(pk=id)

    if request.method == 'POST':
        form = descriptionSuggestion(request.POST)

        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.technique_id = id
            suggestion.save()
            suggestion.addedByUser.add(request.user)

    else:
        form = descriptionSuggestion()

    UserSuggestions = request.user.suggestedByUser.all()
    userObjects = []

    for x in UserSuggestions:
        if x.technique_id == id:
            userObjects.append(Suggestion.objects.get(id=x.id))
        # userObjects.append(Suggestion.objects.get(id=x.id))
    context = {
        'technique': techniqueObj,
        'SuggestForm': form,
        'UserSuggestions': userObjects
    }
    return render(request, "BJJournal/BJR_Techniques/BJR_Techniques_singleTechniqueView.html", context)

# suggestion.techSuggestion.add(id)


# def addTechnique(request):
#     if request.method == 'POST':
#         form = addTechniqueForm(request.POST)
#         if form.is_valid():
#             tp = form.cleaned_data["type"]
#             leng = form.cleaned_data["length"]
#             dat = form.cleaned_data["date"]
#             loc = form.cleaned_data["location"]
#             # ts = TrainingSession(name=n)
#             # ts.save()
#             # t.user_lists.add(request.user)
#     #
#     # else:
#     #     form = TrainingSessionForm()
#
#     # context = {
#     #     'BJRform': form,
#     #     'techniquesList': Technique.objects.all()
#     # }
#     return render(request, "BJJournal/BJR_addSession.html", context)
