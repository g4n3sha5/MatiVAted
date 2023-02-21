from django.db import models
from datetime import datetime
from calendar import HTMLCalendar
# Create your models here.
from Clubs.models import Club
from WorkoutJournal.models import TrainingSession

# class TableDay (models.Model):
#     days = (
#         ('monday',)
#     )

class Calendar (HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

        # formats a day as a td
        # filter events by day

    def formatday(self, day, events):
        events_per_day = events.filter(date__day=day)
        d = ""
        for event in events_per_day:
            d += f"<li> {event.get_html_url} </li>"
        if day != 0:
            html =  f"<td><span class='date'>{day}</span><ul> {d} </ul></td> <button type='button' class='scheduleAddTraining'>Add Traning </button>"

            return html
        return "<td></td>"

        # formats a week as a tr

    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=False, **kwargs):

        cal = (
            '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        )  # noqa
        cal += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        )
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week)}\n"
        return cal