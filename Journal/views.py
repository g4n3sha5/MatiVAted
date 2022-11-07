from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, CreateNewList

# Create your views here.



def urladjuster(request, id):
    checklist = ToDoList.objects.get(pk = id)
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
                checklist.item_set.create(text = txt)
            else:
                print("Text too short")

    return render(request, "Journal/list.html", context)

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n, user = request.user)
            t.save()
            request.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    context = {
        'form': form,
        'ListCollection' : ToDoList.objects.all()
    }
    return render(request, "Journal/create.html", context)


def removeList(request, lists):
    print("abc")
    return render(request, "Journal/remove.html", )