from django.shortcuts import render

# Create your views here.
def about (request):

    context={

    }
    return render(request, "Presentation/about.html", context)

def aboutSection (request, section):


    context ={

    }
    return render(request, f"Presentation/{section}.html", context)