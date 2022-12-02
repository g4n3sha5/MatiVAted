from django.shortcuts import render
from .models import TrainingSession, addSessionForm
# Create your views here.
def BJJournalIndex (request):

    context = {
        'user' : request.user
    }
    return render(request, "BJJournal/BJR_index.html", context)

def dashboard(request):

    context = {

    }

    return render (request, "BJJournal/BJR_dashboard.html", context)



def addSession(request):
    if request.method == 'POST':
        form = addSessionForm(request.POST)

        if form.is_valid():
            tp = form.cleaned_data["type"]
            leng = form.cleaned_data["length"]
            dat = form.cleaned_data["date"]
            loc = form.cleaned_data["location"]
            nots = form.cleaned_data["notes"]
            # ts = TrainingSession(name=n)
            # ts.save()
            # t.user_lists.add(request.user)

    else:
        form = addSessionForm()

    context = {
        'BJRform': form
    }
    return render(request, "BJJournal/BJR_addSession.html", context)