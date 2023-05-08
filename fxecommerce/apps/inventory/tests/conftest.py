import pytest
from django.contrib.auth.models import Group
from users.models import User, Employee, Customer
from inventory.models import Category, Product, Supplier, OrderDetails, Order, Shipper
import datetime

@pytest.fixture
def user_fixture(db):
    # Employee User
    employee_group = Group.objects.get(name='Employee')
    employee_user = User.objects.create_user(
        email='employee@test.com',
        password='testpassword',
        user_type=1,
    )
    employee_user.groups.add(employee_group)
    employee_user.save()

    # Customer User
    customer_group = Group.objects.get(name='Customer')
    customer_user = User.objects.create_user(
        email='customer@test.com',
        password='testpassword',
        user_type=4,
    )
    customer_user.groups.add(customer_group)
    customer_user.save()

    # Extra Staff User
    extra_staff_group = Group.objects.get(name='ExtraStaff')
    extra_staff_user = User.objects.create_user(
        email='extrastaff@test.com',
        password='testpassword',
        user_type=1,
    )
    extra_staff_user.groups.add(extra_staff_group)
    extra_staff_user.save()

    return {
        'employee_user': {
            'user': employee_user,
            'password': 'testpassword',
        },
        'customer_user': {
            'user': customer_user,
            'password': 'testpassword',
        },
        'extra_staff_user': {
            'user': extra_staff_user,
            'password': 'testpassword',
        },
    }


@pytest.fixture
def test_category_data(db):
    return Category.objects.create(
        category_name="TestCategory",
        description="TestDescription"
    )

@pytest.fixture
def categories_data(db):
    return [
        Category.objects.create(category_name=f"Category {i}") for i in range(1,5)
    ]


@pytest.fixture
def test_supplier_data(db):
    return Supplier.objects.create(
        company_name="Example Company",
        contact_name="John Doe",
        contact_title="Manager",
        address="123 Main St",
        city="New York",
        postal_code="10001",
        country="USA",
        phone="+1 (212) 555-1212",
    )

@pytest.fixture
def suppliers_data(db):
    return [
        Supplier.objects.create(
            company_name=f"Supplier {i}",
            contact_name="John Doe",
            contact_title="Manager",
            address="123 Main St",
            city="New York",
            postal_code="10001",
            country="USA",
            phone="+1 (212) 555-1212"
        ) for i in range(1,5)
    ]


@pytest.fixture
def test_product_data(test_category_data, test_supplier_data, db):
    category = test_category_data
    supplier = test_supplier_data

    product = Product.objects.create(
        product_name="Test Single Product",
        supplier_id=supplier,
        category_id=category,
        quantity_per_unit=10,
        unit_price=20.0,
        units_in_stock=10,
        units_on_order=0,
        reorder_level=3,
        discontinued=False
    )

    return product

@pytest.fixture
def products_data(test_category_data, test_supplier_data, db):
    category = test_category_data
    supplier = test_supplier_data

    products = [
        Product.objects.create(
            product_name=f"Test Product {i}",
            supplier_id=supplier,
            category_id=category,
            quantity_per_unit=10,
            unit_price=20.0 * i,
            units_in_stock=10 * i,
            units_on_order=0,
            reorder_level=3 * i,
            discontinued=False
        ) for i in range(1,5)
    ]

    return products

@pytest.fixture
def test_orderdetails_data(test_product_data, user_fixture, db):
    test_product = test_product_data
    customer_user = user_fixture['customer_user']['user']

    order_data = OrderDetails.objects.create(
        product_id=test_product,
        quantity=5,
        unit_price=test_product.unit_price,
        discount=0,
        created_by=customer_user
    )

    return order_data


@pytest.fixture
def test_orderdetails_data_calculation(test_product_data, user_fixture, db):
    test_product = test_product_data
    customer_user = user_fixture['customer_user']['user']

    order_data = OrderDetails.objects.create(
        product_id=test_product,
        quantity=5,
        discount=0,
        created_by=customer_user
    )

    return order_data




@pytest.fixture
def test_order_data(db, user_fixture):
    customer_user = user_fixture['customer_user']['user']
    employee_user = user_fixture['employee_user']['user']

    customer_instance = Customer.objects.get(user=customer_user)
    employee_instance = Employee.objects.get(user=employee_user)

    order = Order.objects.create(
        customer_id=customer_instance,
        employee_id=employee_instance,
        order_date=datetime.date.today(),
        required_date=datetime.date.today() + datetime.timedelta(days=7),
        shipped_date=None,
        ship_via=None,
        freight=None,
        ship_name="John Doe",
        ship_address="123 Main St",
        ship_city="New York",
        ship_region="NY",
        ship_postal_code="10001",
        ship_country="USA",
        order_status=1
    )

    return order


@pytest.fixture
def test_shipper_data(db):
    shipper = Shipper.objects.create(
        company_name="Test Shipping Company",
        phone="123-456-7890",
        freight_price=50.0,
    )

    return shipper
