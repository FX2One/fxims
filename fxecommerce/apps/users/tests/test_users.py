import pytest
from users.models import User, Employee, Customer
from django.contrib.auth.models import Group


@pytest.mark.django_db
def test_create_user():
    # Create a new user
    user = User.objects.create_user(
        email='user@example.com',
        password='testpassword',
        user_type=1
    )

    # Check if the user was created correctly
    assert user.email == 'user@example.com'
    assert user.user_type == 1
    assert not user.is_staff
    assert not user.is_superuser
    assert user.is_active

    # Check if the user was added to the Employee group
    employee_group = Group.objects.get(name='Employee')
    assert user.groups.filter(pk=employee_group.pk).exists()

    # Create a new customer user
    customer_user = User.objects.create_user(
        email='customer@example.com',
        password='testpassword',
        user_type=4
    )

    # Check if the customer user was created correctly
    assert customer_user.email == 'customer@example.com'
    assert customer_user.user_type == 4
    assert not customer_user.is_staff
    assert not customer_user.is_superuser
    assert customer_user.is_active

    # Check if the customer user was added to the Customer group
    customer_group = Group.objects.get(name='Customer')
    assert customer_user.groups.filter(pk=customer_group.pk).exists()

@pytest.mark.django_db
def test_create_customer():
    email = "customer@example.com"

    # Create and save the User instance with user_type=4
    user = User.objects.create_user(email=email, user_type=4, password='test_password')

    # Customer is created by signals.py
    customer = user.customer

    # Update all the customer fields
    customer.company_name = 'Updated Company'
    customer.contact_name = 'Updated Contact Name'
    customer.contact_title = 'Updated Contact Title'
    customer.address = 'Updated Address'
    customer.city = 'Updated City'
    customer.postal_code = 'Updated Postal Code'
    customer.country = 'Updated Country'
    customer.phone = 'Updated Phone'
    customer.save()

    # clean instance from db with latest changes
    customer.refresh_from_db()

    assert customer.company_name == 'Updated Company'
    assert customer.contact_name == 'Updated Contact Name'
    assert customer.contact_title == 'Updated Contact Title'
    assert customer.address == 'Updated Address'
    assert customer.city == 'Updated City'
    assert customer.postal_code == 'Updated Postal Code'
    assert customer.country == 'Updated Country'
    assert customer.phone == 'Updated Phone'



@pytest.mark.django_db
def test_create_employee():
    # Generate a unique email address for the test
    email = "employee@example.com"

    # Create and save the User instance with user_type=1
    user = User.objects.create_user(email=email, user_type=1, password='test_password')

    # Employee is created by signals.py
    employee = user.employee

    # Update all the Employee fields
    employee.last_name = 'Updated Last Name'
    employee.first_name = 'Updated First Name'
    employee.title = 'Updated Title'
    employee.address = 'Updated Address'
    employee.city = 'Updated City'
    employee.postal_code = 'Updated Postal Code'
    employee.country = 'Updated Country'
    employee.home_phone = 'Updated Home Phone'
    employee.extension = '1234'
    employee.save()

    # clean instance from db with latest changes
    employee.refresh_from_db()


    assert employee.last_name == 'Updated Last Name'
    assert employee.first_name == 'Updated First Name'
    assert employee.title == 'Updated Title'
    assert employee.address == 'Updated Address'
    assert employee.city == 'Updated City'
    assert employee.postal_code == 'Updated Postal Code'
    assert employee.country == 'Updated Country'
    assert employee.home_phone == 'Updated Home Phone'
    assert employee.extension == '1234'