from django.db import models
from django.utils import timezone
import pytz
from django.utils.html import mark_safe


class Contact(models.Model):
    DisplayName = models.CharField(max_length=50)
    OfficeNumber = models.CharField(max_length=10, unique=True)
    MobileNumber = models.CharField(max_length=15, null=True, blank=True)
    OtherNumber = models.CharField(max_length=15, null=True, blank=True)


class CallCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Главная категория")

    def __str__(self):
        return self.name


class CallSubCategory(models.Model):
    category = models.ForeignKey(CallCategory, on_delete=models.CASCADE, related_name="subcategories",
                                 verbose_name="Главная категория")
    name = models.CharField(max_length=100, unique=True, verbose_name="Подкатегория")

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Call(models.Model):
    CALL_TYPES = [
        ('incoming', 'Входящий'),
        ('outgoing', 'Исходящий'),
        ('local', 'Локальный'),
        ("missed", "Missed"),
    ]

    call_id = models.CharField(max_length=50, unique=True, verbose_name="ID звонка")
    caller = models.CharField(max_length=20, verbose_name="Номер звонящего")
    receiver = models.CharField(max_length=20, verbose_name="Номер получателя")
    call_type = models.CharField(max_length=10, choices=CALL_TYPES, verbose_name="Тип звонка")
    duration = models.PositiveIntegerField(null=True, blank=True, verbose_name="Длительность (сек)")
    date = models.DateField(default=timezone.now, verbose_name="Дата звонка")
    time = models.TimeField(default=timezone.now, verbose_name="Время звонка")
    recording = models.FileField(upload_to='recordings', null=True, blank=True, verbose_name="Запись звонка")
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")
    category = models.ForeignKey(CallCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name="Категория")
    subcategory = models.ForeignKey(CallSubCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name="Подкатегория")

    @property
    def sound_display(self):
        if self.recording:
            return mark_safe(
                f'<audio controls name="media"><source src="{self.recording.url}" type="audio/mpeg"></audio>')
        return ""

    def save(self, *args, **kwargs):
        uzbekistan_tz = pytz.timezone('Asia/Tashkent')
        self.time = timezone.now().astimezone(uzbekistan_tz).time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.call_id} ({self.call_type})"
