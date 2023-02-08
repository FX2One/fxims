from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Customer, Employee

from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == 1:
        Employee.objects.create(user=instance)
    elif created and instance.user_type == 4:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 4:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)
        instance.customer.save()
    else:
        group = Group.objects.get(name='Employee')
        instance.groups.add(group)
        instance.employee.save()




