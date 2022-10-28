from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, CreateNewList

# Create your views here.

def index(response):
    # ls = ToDoList.objects.get(id=id)
    return render(response, "Journal/index.html", {})

def urladjuster(response, id):
    checklist = ToDoList.objects.get(pk = id)
    context = {
        'checklist': checklist,
        'id': id
    }

    if response.method =="POST":
        if response.POST.get("save"):
            for item in checklist.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.checked = True
                else:
                    item.checked = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("newItemText")
            if len(txt) > 2:
                checklist.item_set.create(text = txt)
            else:
                print("Text too short")

    return render(response, "Journal/list.html", context)

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    context = {
        'form': form,
        'ListCollection' : ToDoList.objects.all()
    }
    return render(response, "Journal/create.html", context)