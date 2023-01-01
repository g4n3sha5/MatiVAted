from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import TrainingSession, Technique, Suggestion, User
from .forms import TrainingSessionForm, addTechniqueForm, descriptionSuggestion

from django.contrib import messages


# Create your views here.


def BJJournalIndex(request):
    context = {
        'user': request.user
    }
    return render(request, "BJJournal/BJR_index.html", context)


def dashboard(request):
    context = {

    }

    return render(request, "BJJournal/BJR_dashboard.html", context)


def addSession(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, auto_id=True)

        if form.is_valid():
            sessionInstance = form.save(commit=False)
            messages.success(request, "Added your session")
            form.save()
            sessionInstance.addedByUser.add(request.user)
            return HttpResponseRedirect('/addSession')
        else:
            messages.error(request, "Invalid form. ")

    else:
        form = TrainingSessionForm()

    context = {
        'BJRform': form,
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_addSession.html", context)


def yourSessions(request):
    context = {
        # 'BJRform': form,
        'sessionsList': TrainingSession.objects.all()
    }

    return render(request, "BJJournal/BJR_yourSessions.html", context)


def singleSessionView(request, id):

    Session = TrainingSession.objects.get(pk=id)
    context = {
        'session': Session,
        'form': TrainingSessionForm(instance=Session)
    }
    return render(request, "BJJournal/BJR_yourSessions/BJR_yourSessions_singleSessionView.html", context)


def editSession(request, id):
    print(request)
    Session = TrainingSession.objects.get(pk=id)
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=Session, auto_id=True)
        print(request.POST)
        if form.is_valid():
            print("valid")
            form.save()

    return redirect ('/yourSessions')


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
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_Techniques.html", context)


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
