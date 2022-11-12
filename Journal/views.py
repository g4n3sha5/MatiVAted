from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, CreateNewList

# Create your views here.


def listManager(request, id):
    checklist = ToDoList.objects.get(pk=id)
    context = {
        'checklist': checklist,
        'id': id
    }

    if request.method =="POST":
        if request.POST.get("save"):
            for item in checklist.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.checked = True
                else:
                    item.checked = False
                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("newItemText")
            if len(txt) > 2:
                checklist.item_set.create(text=txt)
            else:
                print("Text too short")

    return render(request, "Journal/singleListView.html", context)

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
            t.user_lists.add(request.user)
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    context = {
        'form': form,
        'ListCollection' : ToDoList
    }
    if request.user.is_authenticated:
        context['ListCollection'] = request.user.user_lists.all()
    return render(request, "Journal/create.html", context)

#removing list at /create/
def removeList(request, id):
    print("ACAB")
    userLists = request.user.user_lists
    userLists.remove(id)

    context = {
        'lists' : userLists.all(),
        'id' : id
    }
    return render(request, "Journal/listsView.html", context)