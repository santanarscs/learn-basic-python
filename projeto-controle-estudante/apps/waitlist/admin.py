from django.contrib import admin
from .models import WaitlistEntry


class WaitlistEntryAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'created_at']


admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
