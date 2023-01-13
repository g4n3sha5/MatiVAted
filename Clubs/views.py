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
