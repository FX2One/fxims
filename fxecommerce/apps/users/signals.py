from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile

from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 4:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)
    instance.profile.save()




