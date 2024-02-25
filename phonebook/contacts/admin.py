from django.contrib import admin
from .models import Contact, Call


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('DisplayName', 'OfficeNumber', 'MobileNumber', 'OtherNumber',)


class CallAdmin(admin.ModelAdmin):
    list_display = ('caller', 'receiver', 'date', 'time', 'sound_display', 'status')
    list_filter = ('caller', 'receiver', 'date', 'status')
    search_fields = ('caller', 'receiver')
    readonly_fields = ('caller', 'receiver', 'date', 'time', 'recording', 'sound_display', 'status')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Call, CallAdmin)
