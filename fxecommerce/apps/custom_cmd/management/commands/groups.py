from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.db import models
import logging

GROUPS = {
    "Employee": {
        "category": ["add","view"],
        "customer": ["view"],
        "employee": ["view"],
        "order": ["add", "delete","change", "view"],
        "product": ["add", "delete", "change", "view"],
    },

    "Customer": {
        "category": ["view"],
        "order": ["add", "view"],
        "product": ["view"],
    },
}


class Command(BaseCommand):

    help = "Creates read only default permission groups for users"

    def handle(self, *args, **options):

        for group_name in GROUPS:

            group, created = Group.objects.get_or_create(name=group_name)

            # Loop models in group
            for app_model in GROUPS[group_name]:

                # Loop permissions in group/model
                for permission_name in GROUPS[group_name][app_model]:

                    # Generate permission name as Django would generate it
                    name = f"Can {permission_name} {app_model}"

                    try:
                        model_add_permissions = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning(f"Permission {name} not found")
                        continue

                    group.permissions.add(model_add_permissions)