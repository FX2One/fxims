from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command('loaddata', 'db_admin_fixture.json') #basic admin creation admin@admin.com ,admin1
        call_command('loaddata', 'db_region_fixture.json')
        call_command('loaddata', 'db_territory_fixture.json')
        call_command('loaddata', 'db_employee_fixture.json')
        call_command('loaddata', 'db_employee_territories_fixture.json')
        call_command('loaddata', 'db_shipper_fixture.json')
        call_command('loaddata', 'db_customer_demo_fixture.json')
        call_command('loaddata', 'db_customer_fixture.json')
        call_command('loaddata', 'db_customer_customer_demo_fixture.json')
        call_command('loaddata', 'db_category_fixture.json')
        call_command('loaddata', 'db_supplier_fixture.json')
        call_command('loaddata', 'db_product_fixture.json')
        call_command('loaddata', 'db_order_fixture.json')
        call_command('loaddata', 'db_order_details_fixture.json')
