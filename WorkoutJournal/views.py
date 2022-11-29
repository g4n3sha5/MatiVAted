from django.shortcuts import render

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
    context = {

    }
    return render(request, "BJJournal/BJR_addSession.html", context)