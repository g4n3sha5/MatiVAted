from django.shortcuts import render, HttpResponseRedirect, reverse
from datetime import datetime, date
from .models import Schedule, UserMembership, userClub
from .utilis import Calendar
from django.contrib.auth.decorators import login_required

from .forms import ScheduleForm
from django.utils.safestring import mark_safe


@login_required
def clubSchedule(request):
    days = Schedule.days
    # userHasClub = False
    myClub = userClub(request.user.id)
    try:
        mySchedule = Schedule.objects.get(club_id=myClub.id)
        fields = mySchedule._meta.get_fields()
    except:
        mySchedule = None

    hoursDict = {}
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

    authorized = False
    membership = UserMembership.objects.get(user_id=request.user.id)
    if membership.authorized == 'FULL':
        authorized = True

    # for timeHour, sessionsArray in hoursDict:
    #     print(timeHour, sessionsArray)

    context = {
        # 'userHasClub' : UserMembership.objects.get(user_id = request.user.id),
        # 'cal' : mark_safe(HTMLcal),
        # 'dayDict' : dayDict,
        'authorized' : authorized,
        'club' : userClub(request.user.id),
        'days' : days,
        'hoursDict' : hoursDict
     }


    return render(request, 'Clubs/clubsSchedule.html', context)


def addTrainingModal(request, type, day):
    form = ScheduleForm()
    myClub = userClub(request.user.id)

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        print("cojestkurwa")
        if form.is_valid():
            print("huj")
            mySchedule = Schedule.objects.get_or_create(club=myClub)[0]
            data = form.cleaned_data
            time, description  = data['time'], data['description']
            dayField = getattr(mySchedule, day)
            dayField[time] = [type, description]
            mySchedule.save()
        print(form.errors)
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


