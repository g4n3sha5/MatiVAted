from django.shortcuts import render
from datetime import datetime, date
from .models import Schedule
from .utilis import Calendar
from .models import UserMembership
from django.utils.safestring import mark_safe



def clubsSchedule(request):
    dat = get_date(request.GET.get('day'))
    cal = Calendar(dat.today, dat.month)
    userHasClub = False
    HTMLcal = cal.formatmonth()

    #
    # if UserMembership.objects.get(user_id = request.user.id):
    #     userHasClub = True

    context = {
        'userHasClub' : UserMembership.objects.get(user_id = request.user.id),
        'cal' : mark_safe(HTMLcal),

    }
    return render(request, 'Clubs/clubsSchedule.html', context)

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


