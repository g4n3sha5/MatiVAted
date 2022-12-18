from django.contrib import admin
from .models import Technique, TrainingSession, Suggestion
# Register your models here.

#
admin.site.register(Technique)
admin.site.register(TrainingSession)
admin.site.register(Suggestion)