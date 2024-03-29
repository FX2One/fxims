from django.core.management import call_command
from django.core.management.base import BaseCommand

'''
admin@admin: admin1,
ricsu@ricsu: ricsu1,
whitc@whitc: whitc1,
tortu@tortu: tortu1
'''


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command('loaddata', 'db_group_fixture.json')
        call_command('groups')
        call_command('loaddata', 'db_admin_fixture.json')
        call_command('loaddata', 'db_user_fixture.json')
        call_command('loaddata', 'db_employee_fixture.json')
        call_command('loaddata', 'db_customer_fixture.json')
        call_command('loaddata', 'db_region_fixture.json')
        call_command('loaddata', 'db_territory_fixture.json')
        call_command('loaddata', 'db_employee_territories_fixture.json')
        call_command('loaddata', 'db_shipper_fixture.json')
        call_command('loaddata', 'db_customer_demo_fixture.json')
        call_command('loaddata', 'db_customer_customer_demo_fixture.json')
        call_command('loaddata', 'db_category_fixture.json')
        call_command('loaddata', 'db_supplier_fixture.json')
        call_command('loaddata', 'db_product_fixture.json')
        call_command('loaddata', 'db_order_fixture.json')
        call_command('loaddata', 'db_order_details_fixture.json')

