from django.db import models
from django.contrib.auth.models import User
from Notifications.models import Notification
from account_register.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Case, When, Value
# Create your models here.
MEMBER_ORDER = Case(
    When(memberType='Head', then=Value(1)),
    When(memberType='Instructor', then=Value(2)),
    When(memberType='Professor', then=Value(3)),
    When(memberType='Student', then=Value(4)),
)
BELT_ORDER = Case(
    When(belt='Black Belt', then=Value(1)),
    When(belt='Brown Belt', then=Value(2)),
    When(belt='Purple Belt', then=Value(3)),
    When(belt='Blue Belt', then=Value(4)),
    When(belt='White Belt', then=Value(5)),
    When(belt='No Info', then=Value(6)),
)

class Club(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    logo = models.ImageField(default='defaultLogo.png', upload_to='clubs_logo',  blank=True, null=True)
    estabilished = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.TextField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=2500, blank=True, null=True)
    phoneNumber = models.TextField(max_length=100, blank=True, null=True)
    email = models.TextField(max_length=100, blank=True, null=True)
    website = models.TextField(max_length=100, blank=True, null=True)
    # GRAFIK!!
    creator = models.ForeignKey(User, related_name="clubCreator", on_delete=models.CASCADE, null=True, blank=True)

    def numbers_list(self):
        if self.phoneNumber:
            return self.phoneNumber.split(',')

    def authorizedMembers(self):
        return UserMembership.objects.filter(authorized = 'FULL', club_id = self.id )

    def membersList (self):
        return UserMembership.objects.filter(club=self).order_by(MEMBER_ORDER)
    def requestList (self):
        return Request.objects.filter(club=self)


    def __str__(self):
        return f'{self.name} {self.estabilished}'



class UserMembership(models.Model):
    MEMBER_TYPES = (
        ('Head', 'Head'),
        ('Instructor', 'Instructor'),
        ('Professor', 'Professor'),
        ('Student', 'Student')
    )
    AUTHORIZED = (
        ('FULL', 'FULL'),
        ('TRAININGS', 'TRAININGS'),
        ('NON-AUTHORIZED', 'NON-AUTHORIZED')

    )

    user = models.ForeignKey(User, related_name="userMembership", on_delete=models.CASCADE)
    authorized = models.CharField(choices=AUTHORIZED, max_length=30, default = "NON-AUTHORIZED")
    memberType = models.CharField(choices=MEMBER_TYPES, max_length=40, default='Student')
    slug = models.SlugField(null=True, blank=True)
    club = models.ForeignKey(Club, related_name='membersClub', on_delete=models.CASCADE, null=True)
class Request (models.Model):
    ACCEPTED = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        ('REJECTED', 'REJECTED'),
    )
    club = models.ForeignKey(Club, related_name ="request", on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name = "userRequest", on_delete=models.CASCADE)
    status = models.CharField(choices = ACCEPTED, max_length=30)

    def save(self, *args, **kwargs):
        clubID = self.club.id
        receiverClub = Club.objects.get(id = clubID)
        authorizedMembers = receiverClub.authorizedMembers()
        for member in authorizedMembers:
            myNotification = Notification(
                message="A user sent a request to join your club!",
                userSender=self.user,
            )
            myNotification.save()
            authorizedUser = User.objects.get(id=member.user_id)
            myNotification.userReceiver.add(authorizedUser)

        super(Request, self).save(*args, **kwargs)



# @receiver(post_save, sender=Request)
# def create_notification(sender, instance, created, **kwargs):
#     if created:
#
#
