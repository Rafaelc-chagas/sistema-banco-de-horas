from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RegistryHours, worked_hours


@receiver(post_save, sender=RegistryHours)
def update_worked_hours(sender, instance, **kwargs):
    worked_hours(instance)
