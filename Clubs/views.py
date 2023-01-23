from django.shortcuts import render
from .models import Club
from .forms import ClubForm
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
        'user': request.user
    }

    if request.method == 'POST':
        yourClub, created = Club.objects.get_or_create(creator=request.user)
        form = ClubForm(request.POST, request.FILES, instance=yourClub)

        if form.is_valid():
            instance = form.save(commit=False)
            yourClub.creator =  request.user
            instance.save()

            context['form'] = form
            context['Club'] = yourClub
            context['success'] = True
    else:
        template = 'index'




    if request.META.get('HTTP_HX_REQUEST'):
        template = 'index_reloadContent'

    return render(request, f"Clubs/{template}.html", context)



def clubMembers (request):
    context={}
    return render(request, "Clubs/clubMembers.html", context)

def clubsTrainings (request):
    context={}
    return render(request, "Clubs/clubsTrainings.html", context)

def clubsSchedule (request):
    context={}
    return render(request, "Clubs/clubsSchedule.html", context)

def clubsList (request):
    context={
        'clubsList' : Club.objects.all()
    }
    return render(request, "Clubs/clubsList.html", context)

def singleClubView (request, id):
    myClub = Club.objects.get(pk=id)
    context={
        'Club' : myClub
    }
    return render(request, "Clubs/singleClubView.html", context)

