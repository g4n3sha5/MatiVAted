from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Club(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    logo = models.ImageField(default='defaultLogo.png', upload_to='clubs_logo',  blank=True, null=True)
    estabilished = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=2500, blank=True, null=True)
    phoneNumber = models.TextField(max_length=100, blank=True, null=True)
    email = models.TextField(max_length=100, blank=True, null=True)
    website = models.TextField(max_length=100, blank=True, null=True)
    # GRAFIK!!
    instructors = models.TextField(max_length=100, blank=True, null=True)
    authorizedUser = models.ForeignKey(User, related_name= "authorizedUser",on_delete=models.CASCADE, null=True, blank=True)
    creator = models.ForeignKey(User, related_name="clubCreator", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.estabilished}'