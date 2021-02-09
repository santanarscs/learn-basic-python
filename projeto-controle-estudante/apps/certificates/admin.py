from django.contrib import admin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description', 'created_at', 'updated_at']


admin.site.register(Certificate, CertificateAdmin)
