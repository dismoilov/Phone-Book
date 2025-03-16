from django.contrib import admin
from .models import Contact, Call, CallCategory, CallSubCategory

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('DisplayName', 'OfficeNumber', 'MobileNumber', 'OtherNumber')

@admin.register(CallCategory)
class CallCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(CallSubCategory)
class CallSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('call_id', 'caller', 'receiver', 'call_type', 'duration', 'date', 'time', 'category', 'subcategory', 'sound_display')
    list_filter = ('call_type', 'date', 'category')
    search_fields = ('caller', 'receiver', 'call_id')
    readonly_fields = ('call_id', 'caller', 'receiver', 'call_type', 'duration', 'date', 'time', 'recording', 'sound_display')

    def has_change_permission(self, request, obj=None):
        return True  # Можно редактировать категорию и подкатегорию

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
