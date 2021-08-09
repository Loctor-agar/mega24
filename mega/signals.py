from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Company, Looking


@receiver(post_save, sender=Company)
def get_counter_views(sender, instance, created, **kwargs):
    if created:
        Looking.objects.create(id=instance)