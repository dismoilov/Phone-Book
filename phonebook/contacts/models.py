from django.db import models
from django.utils import timezone


class Contact(models.Model):
    DisplayName = models.CharField(max_length=50)
    OfficeNumber = models.CharField(max_length=10, unique=True)
    MobileNumber = models.CharField(max_length=15, null=True, blank=True)
    OtherNumber = models.CharField(max_length=15, null=True, blank=True)


class Call(models.Model):
    caller = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    recording = models.FileField(upload_to='recordings')
