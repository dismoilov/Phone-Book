from django.db import models
import xml.etree.ElementTree as ET


class Contact(models.Model):
    DisplayName = models.CharField(max_length=50)
    OfficeNumber = models.CharField(max_length=10, unique=True)
    MobileNumber = models.CharField(max_length=15, null=True, blank=True)
    OtherNumber = models.CharField(max_length=15, null=True, blank=True)

