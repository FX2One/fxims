import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'db_group_fixture.json')

'''creating default superuser'''
@pytest.fixture
def create_admin(django_user_model):
    """return default admin user"""

    return django_user_model.objects.create_superuser("admin","admin@admin.com","password")


""" 
https://pytest-django.readthedocs.io/en/latest/database.html 
more on setting database fixture with pytest
while storing straight to db, password has to be hashed in .json file
the best way is to run shell in project
from django.contrib.auth.hashers import make_password
make_password('your_password') and copy result into .json file
"""
@pytest.fixture(scope='session')
def django_database_fixture_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        """ can be used as a context manager to enable database access for the specified fixture"""
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

