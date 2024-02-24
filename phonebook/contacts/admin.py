from django.contrib import admin
from .models import Contact, Call


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('DisplayName', 'OfficeNumber', 'MobileNumber', 'OtherNumber',)

admin.site.register(Call)