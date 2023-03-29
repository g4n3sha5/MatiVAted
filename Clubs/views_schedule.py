from django.shortcuts import render, HttpResponseRedirect, reverse
from datetime import datetime, date
from .models import Schedule, UserMembership

from django.contrib.auth.decorators import login_required
from main.views import getBaseTemplate
from .forms import ScheduleForm
from django.utils.safestring import mark_safe
from .views import userHasClub, userClub

@login_required
def clubSchedule(request):
    days = Schedule.days
    authorized = False
    hoursDict = {}


    try:
        myClub = userClub(request.user.id)
        membership = UserMembership.objects.get(user_id=request.user.id)
        if membership.authorized == 'FULL':
            authorized = True
    except:
        myClub = False

    try:
        mySchedule = Schedule.objects.get(club_id=myClub.id)
        fields = mySchedule._meta.get_fields()
    except:
        mySchedule = None

    if mySchedule:
        for day in days:
            dayTable = getattr(mySchedule, day)
            if bool(dayTable):
                dayDict = sorted(dayTable.items())
                for time, info in dayDict:
                    timeHours = int(time[:2])
                    if timeHours not in hoursDict:
                        hoursDict[timeHours] = []

                    hoursDict[timeHours].append([day, time, info])
        hoursDict = sorted(hoursDict.items())



    context = {
        'authorized' : authorized,
        'club' : myClub,
        'days' : days,
        'hoursDict' : hoursDict,
        'base_template': getBaseTemplate(request, "Clubs"),
        'userHasClub': userHasClub(request)
     }


    return render(request, 'Clubs/clubsSchedule.html', context)


def addTrainingModal(request, type, day):
    form = ScheduleForm()
    myClub = userClub(request.user.id)

    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            mySchedule = Schedule.objects.get_or_create(club=myClub)[0]
            data = form.cleaned_data
            time, description  = data['time'], data['description']
            dayField = getattr(mySchedule, day)
            dayField[time] = [type, description]
            mySchedule.save()

        return HttpResponseRedirect(reverse('clubSchedule'))

    context ={
        'scheduleForm' : form,
        'type' : type,
        'day' : day

    }
    return render(request, 'Clubs/clubsScheduleModal.html', context)


def removeTrainingSchedule(request, type, day, hour, clubID):
    mySchedule = Schedule.objects.get(club_id=clubID)
    dayField = getattr(mySchedule, day)

    for hourDB, info in dayField.items():
        if hourDB == hour:
            del dayField[hourDB]
            mySchedule.save()
            break
    return HttpResponseRedirect(reverse('clubSchedule'))


# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()


