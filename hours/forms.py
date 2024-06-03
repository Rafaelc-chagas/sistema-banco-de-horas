from django import forms
from django.core.exceptions import ValidationError
from .models import RegistryHours
from datetime import time


class RegistryHoursForm(forms.ModelForm):
    class Meta:
        model = RegistryHours
        fields = ('work_shift', 'start_time', 'end_time', 'description',)
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'work_shift': 'Turno de Trabalho',
        }

    def clean(self):
        cleaned_data = super().clean()
        work_shift = cleaned_data.get("work_shift")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and end_time <= start_time:
            raise ValidationError("O horário de fim deve ser maior que o horário de início.")

        if work_shift:
            shift_name = work_shift.shift.lower()
            noon = time(12, 0)

        if shift_name == 'manhã' and start_time and start_time >= noon:
            raise ValidationError("Para o turno da manhã, o horário de início não pode ser superior ou igual às 12:00.")

        if shift_name == 'tarde' and start_time and start_time < noon:
            raise ValidationError("Para o turno da tarde, o horário de início não pode ser inferior às 12:00.")

        return cleaned_data
