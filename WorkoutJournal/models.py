from django.db import models
from datetime import date
# Create your models here.

class Technique (models.Model):
    name = models.CharField(max_length=42)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class TrainingSession(models.Model):
    TStypes = (
        ('GI', 'Gi'),
        ('NOGI', 'No Gi'),
        ('GYM', 'Gym')
    )

    type = models.CharField(choices=TStypes, blank=False, max_length=16)
    date = models.DateField(default=date.today)
    location = models.CharField(max_length=50)
    length = models.SmallIntegerField()
    notes = models.CharField(max_length=300)
    techniques = models.ForeignKey(Technique, on_delete=models.CASCADE)
    def __str__(self):
        return (self.type, self.date)