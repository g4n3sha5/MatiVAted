from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    userSender = models.ForeignKey(User, related_name='userSender', on_delete=models.CASCADE)
    userReceiver = models.ManyToManyField(User, related_name='userReceiver', blank=True)