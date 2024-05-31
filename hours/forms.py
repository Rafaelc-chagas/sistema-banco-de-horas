from django import forms
from .models import RegistryHours


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
