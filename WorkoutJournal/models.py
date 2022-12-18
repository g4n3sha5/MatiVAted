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
        ('GI', 'Gi'),
        ('NOGI', 'No Gi'),
        ('GYM', 'Gym')
    )

    type = models.CharField(choices=TStypes, blank=False, max_length=16)
    date = models.DateField(default=date.today)
    location = models.CharField(max_length=50)
    length = models.IntegerField()
    notes = models.CharField(max_length=300)
    techniques = models.ForeignKey(Technique, on_delete=models.CASCADE, null = True)
    addedByUser = models.ManyToManyField(User, related_name="user_session", blank=False)

    def __str__(self):
        return self.type, self.date


class Suggestion(models.Model):
    addedByUser = models.ManyToManyField(User, related_name="suggestedByUser", default=None)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, default=None, null=True, blank=True)
    content = models.CharField(max_length=2500)

