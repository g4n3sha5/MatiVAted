from django.db import models
from datetime import date
from django.contrib.auth.models import User

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
    TSlength = [(i, i) for i in range(1, 7)]

    type = models.CharField(choices=TStypes, blank=False, max_length=16)
    date = models.DateField(default=date.today, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    length = models.IntegerField(choices=TSlength, blank=False, null=True)
    notes = models.TextField(max_length=2500,blank=True, null=True)
    techniques = models.ManyToManyField(Technique, blank=True)
    addedByUser = models.ManyToManyField(User, related_name="addedByUser", blank=True)
    #change to foreign key???????? ^
    def __str__(self):
        return f'{self.type} {self.date}'

class Suggestion(models.Model):
    addedByUser = models.ManyToManyField(User, related_name="suggestedByUser", default=None)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, default=None, null=True, blank=True)
    content = models.TextField(max_length=2500)

