from django.db import models
from django.utils import timezone
import pytz
from django.utils.html import mark_safe

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

    @property
    def sound_display(self):
        if self.recording:
            return mark_safe(f'<audio controls name="media"><source src="{self.recording.url}" type="audio/mpeg"></audio>')
        return ""

    def save(self, *args, **kwargs):
        uzbekistan_tz = pytz.timezone('Asia/Tashkent')
        self.time = timezone.now().astimezone(uzbekistan_tz).time()
        super().save(*args, **kwargs)
