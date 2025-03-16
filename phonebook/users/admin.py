from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Operator, VoipNumber


class OperatorAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("personal_phone", "local_number")}),
    )


admin.site.register(Operator, OperatorAdmin)
admin.site.register(VoipNumber)
