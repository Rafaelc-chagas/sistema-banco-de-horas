from django.db import models
from accounts.models import EmployeeUser
from datetime import datetime, timedelta
from decimal import Decimal


class WorkShift(models.Model):
    shift = models.CharField(max_length=25, verbose_name='turno')

    def __str__(self):
        return self.shift


class RegistryHours(models.Model):
    employee = models.ForeignKey(EmployeeUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    work_shift = models.ForeignKey(WorkShift, on_delete=models.PROTECT, related_name='work_shift')
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.full_name} - {self.date} - {self.work_shift} {self.start_time} - {self.end_time}"


def worked_hours(registry):
    total_hours = timedelta()

    if registry.start_time and registry.end_time:
        start_time = datetime.combine(datetime.today(), registry.start_time)
        end_time = datetime.combine(datetime.today(), registry.end_time)
        total_hours = end_time - start_time

    worked = total_hours.total_seconds() / 3600.0

    if worked > 4:
        overtime = worked - 4
        overtime_decimal = Decimal(str(overtime))
        registry.employee.hours += overtime_decimal
    else:
        missing_hours = 4 - worked
        missing_hours_decimal = Decimal(str(missing_hours))
        registry.employee.hours -= missing_hours_decimal

    registry.employee.save()
