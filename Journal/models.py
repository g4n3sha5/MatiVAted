from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.


class ToDoList(models.Model):
    user_lists = models.ManyToManyField(User, related_name="user_lists", blank=False)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.text


# form for create, create.html
class CreateNewList(forms.Form):
    name = forms.CharField(label="List name", max_length=200)
    checked = forms.BooleanField(required=False)
