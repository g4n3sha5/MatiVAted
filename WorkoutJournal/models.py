from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


class Technique (models.Model):
    TechniqueTypes = (
        ('Choke', 'Choke'),
        ('Throw', 'Throw'),
        ('Lever', 'Lever'),
        ('Sweep', 'Sweep'),
        ('Position', 'Position')
    )
    type = models.CharField(choices=TechniqueTypes, max_length=15)
    EnglishName = models.CharField(max_length=42, blank=False, unique=True)
    otherName = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=2500, blank=True)


    def __str__(self):
        return self.EnglishName


class TrainingSession(models.Model):
    TStypes = (
        ('GI', 'GI'),
        ('NOGI', 'NOGI'),
        ('GYM', 'GYM')
    )
    HOURS_LENGTH = [(i, i) for i in range(0, 7)]
    MINUTES_LENGTH =[(i, i) for i in range(0, 51, 10)]
    MINUTES_LENGTH.append((15,15))
    MINUTES_LENGTH.append((45,45))
    MINUTES_LENGTH.sort()
    FIGHT_TIME =[(i, i) for i in range(0, 51, 5)]

    type = models.CharField(choices=TStypes, blank=False, max_length=16)
    date = models.DateField(default=date.today, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    hoursLength = models.IntegerField(blank=False, null=True)
    minutesLength = models.IntegerField(blank=False, null=True, default = 00)
    totalLength =  models.IntegerField(blank=True, null=True, default = 0)
    notes = models.TextField(max_length=2500,blank=True, null=True)
    techniques = models.ManyToManyField(Technique, blank=True)
    fightTime = models.IntegerField(blank=True, null=True)
    addedByUser = models.ManyToManyField(User, related_name="addedByUser", blank=True)
    #change to foreign key???????? ^
    def __str__(self):
        return f'{self.type} {self.date}'
    def parseMinutes(self, hours, minutes):
        hoursToMins = hours * 60
        return hoursToMins + minutes

    def clean(self):
        if (self.fightTime > self.parseMinutes(self.hoursLength, self.minutesLength)):
            raise ValidationError("Sparring Time is longer than training!")
    def save(self, *args, **kwargs):
        self.totalLength = self.parseMinutes(self.hoursLength, self.minutesLength)
        print(self.totalLength)
        super(TrainingSession, self).save(*args, **kwargs)



class Suggestion(models.Model):
    addedByUser = models.ManyToManyField(User, related_name="suggestedByUser", default=None)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, default=None, null=True, blank=True)
    content = models.TextField(max_length=2500)

