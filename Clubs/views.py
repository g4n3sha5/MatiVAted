from django.shortcuts import render

# Create your views here.
def ClubsIndex(request):
    context = {
        'user': request.user
    }

    return render(request, "Clubs/index.html", context)
