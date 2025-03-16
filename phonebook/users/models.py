from django.db import models
from django.contrib.auth.models import AbstractUser


class VoipNumber(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name="IP-номер")

    def __str__(self):
        return self.number


class Operator(AbstractUser):
    personal_phone = models.CharField(max_length=20, unique=True, verbose_name="Личный номер")
    local_number = models.OneToOneField(VoipNumber, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name="Локальный номер")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.personal_phone})"
