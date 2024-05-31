from django.contrib import admin
from .models import RegistryHours, WorkShift


class WorkShiftAdmin(admin.ModelAdmin):
    list_display = ('shift',)


class RegistryHoursAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'work_shift', 'start_time', 'end_time', 'description',)


admin.site.register(RegistryHours, RegistryHoursAdmin)
admin.site.register(WorkShift, WorkShiftAdmin)
