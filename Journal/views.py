from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, CreateNewList, singleListForm
from django.contrib.auth.decorators import login_required
from main.views import getBaseTemplate
# Create your views here.

@login_required
def newTaskToDo(request, checklist):
    txt = request.POST.get("newItemText")
    if len(txt) > 2:
        checklist.item_set.create(text=txt)
    else:
        print("Text too short")

def saveTaskStatus(request):
    pass
@login_required
def listManager(request, id):
    try:
        userLists = request.user.user_lists
        clickedList = userLists.get(pk=id)
    except:
        return redirect('/create')
    checklist = ToDoList.objects.get(pk=id)

    context = {
        'checklist': checklist,
        'id': id,

    }
    if request.method =="POST":
        if request.POST.get("newItemText"):
            newTaskToDo(request, checklist)

        for item in checklist.item_set.all():
            if request.POST.get("c" + str(item.id)) == "clicked":
                item.checked = True
            else:
                item.checked = False




            item.save()



    return render(request, "Journal/create_singleListView.html", context)
@login_required
def formValidator (request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            t.user_lists.add(request.user)
    else:
        form = CreateNewList()

    return form

# @login_required
def create(request):
    # pathC = request.get_full_path()[1: -1]

    context = {
        'form': formValidator(request),
        'ListCollection' : ToDoList,
        'base_template' : getBaseTemplate(request, "BJJournal")
    }
    if request.user.is_authenticated:
        context['ListCollection'] = request.user.user_lists.all()

    # return render(request, "Journal/create.html", context)
    return render(request, "Journal/create.html", context)
def saveItem (request):
    pass


#removing list at /create/
@login_required
def removeList(request, id):
    ToDoList.objects.get(pk = id).delete()
    userLists = request.user.user_lists
    userLists.remove(id)
    context = {
        'ListCollection' : userLists.all(),
        'form' : formValidator(request)
    }
    return render(request, "Journal/create_reloadContent.html", context)


#removing item at /singlelistView
@login_required
def removeItem(request, listId, itemId):
    checklist = ToDoList.objects.get(pk=listId)
    Item.objects.get(pk=itemId).delete()
    return render(request, "Journal/create_singleListView.html", {'checklist' : checklist})