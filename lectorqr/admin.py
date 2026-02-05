from django.contrib import admin
from .models import Paciente, ScanLog

admin.site.register(Paciente)

@admin.register(ScanLog)
class ScanLogAdmin(admin.ModelAdmin):
    list_display = ('scanner', 'paciente', 'timestamp')
    list_filter = ('timestamp', 'scanner')
    search_fields = ('scanner__username', 'paciente__id', 'paciente__nombre')
