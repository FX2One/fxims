import pytest
from inventory.models import (Region, Territory, EmployeeTerritory, Shipper, CustomerDemographics, CustomerCustomerDemo, CustomerDemographics, Category, Supplier,
Product, Shipper, Order, OrderDetails, User, Customer, Employee)
import datetime

@pytest.mark.django_db
def test_region_creation():
    region = Region.objects.create(
        region_id=1,
        region_description='Test Region'
    )

    assert region.region_id == 1
    assert region.region_description == 'Test Region'


@pytest.mark.django_db
def test_territory_creation():
    region = Region.objects.create(
        region_id=1,
        region_description='Test Region'
    )

    territory = Territory.objects.create(
        territory_id='T001',
        territory_description='Test Territory',
        region_id=region
    )

    assert territory.territory_id == 'T001'
    assert territory.territory_description == 'Test Territory'
    assert territory.region_id == region


@pytest.mark.django_db
def test_employee_territory_creation():
    region = Region.objects.create(
        region_id=1,
        region_description='Test Region'
    )

    territory = Territory.objects.create(
        territory_id='T001',
        territory_description='Test Territory',
        region_id=region
    )

    user = User.objects.create_user(
        email='test@example.com',
        password='testpassword',
        user_type=1
    )

    employee = Employee.objects.get(user=user)

    employee_territory = EmployeeTerritory.objects.create(
        employee_id=employee,
        territory_id=territory
    )

    assert employee_territory.employee_id == employee
    assert employee_territory.territory_id == territory


@pytest.mark.django_db
def test_shipper_creation():
    shipper = Shipper.objects.create(
        company_name='Test Shipper',
        phone='123-456-7890',
        freight_price=10.50
    )

    assert shipper.company_name == 'Test Shipper'
    assert shipper.phone == '123-456-7890'
    assert shipper.freight_price == 10.50


@pytest.mark.django_db
def test_customer_customer_demo_model():
    customer_demographics = CustomerDemographics.objects.create(
        customer_type_id="1",
        customer_desc="Test description"
    )
    user = User.objects.create(email="testuser@example.com", password="testpassword")
    customer = Customer.objects.create(user=user)
    customer_customer_demo = CustomerCustomerDemo.objects.create(
        customer_id=customer,
        customer_type_id=customer_demographics
    )

    assert customer_customer_demo.customer_id == customer
    assert customer_customer_demo.customer_type_id == customer_demographics


@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(
        category_name="TestCategory",
        description="Test category description"
    )

    assert category.category_name == "TestCategory"
    assert category.description == "Test category description"


@pytest.mark.django_db
def test_supplier_model():
    supplier = Supplier.objects.create(
        company_name="TestSupplier",
        contact_name="TestContact",
        contact_title="TestTitle",
        address="TestAddress",
        city="TestCity",
        postal_code="12345",
        country="TestCountry",
        phone="1234567890"
    )

    assert supplier.company_name == "TestSupplier"
    assert supplier.contact_name == "TestContact"
    assert supplier.contact_title == "TestTitle"
    assert supplier.address == "TestAddress"
    assert supplier.city == "TestCity"
    assert supplier.postal_code == "12345"
    assert supplier.country == "TestCountry"
    assert supplier.phone == "1234567890"


@pytest.mark.django_db
def test_product_model():
    category = Category.objects.create(
        category_name="TestCategory",
        description="Test category description"
    )
    supplier = Supplier.objects.create(
        company_name="TestSupplier",
        contact_name="TestContact",
        contact_title="TestTitle",
        address="TestAddress",
        city="TestCity",
        postal_code="12345",
        country="TestCountry",
        phone="1234567890"
    )
    product = Product.objects.create(
        product_name="TestProduct",
        supplier_id=supplier,
        category_id=category,
        quantity_per_unit="10",
        unit_price=10.0,
        units_in_stock=100,
        units_on_order=10,
        reorder_level=10,
        discontinued=False
    )

    assert product.product_name == "TestProduct"
    assert product.supplier_id == supplier
    assert product.category_id == category
    assert product.quantity_per_unit == "10"
    assert product.unit_price == 10.0
    assert product.units_in_stock == 100
    assert product.units_on_order == 10
    assert product.reorder_level == 10
    assert product.discontinued == False

@pytest.mark.django_db
def test_order_model():
    user_e = User.objects.create(email="testemployee@example.com", password="testpassword", user_type=1)
    user_c = User.objects.create(email="testcustomer@example.com", password="testpassword", user_type=4)
    customer = user_c.customer
    employee = user_e.employee
    shipper = Shipper.objects.create(company_name="TestShipper", phone="1234567890")

    order = Order.objects.create(
        customer_id=customer,
        employee_id=employee,
        order_date="2023-01-01",
        required_date="2023-01-02",
        shipped_date="2023-01-03",
        ship_via=shipper,
        freight=10.0,
        ship_name="TestShipName",
        ship_address="TestShipAddress",
        ship_city="TestShipCity",
        ship_postal_code="12345",
        ship_country="TestShipCountry",
    )

    assert order.customer_id == customer
    assert order.employee_id == employee
    assert datetime.datetime.strptime(order.order_date, "%Y-%m-%d").date() == datetime.date(2023, 1, 1)
    assert datetime.datetime.strptime(order.required_date, "%Y-%m-%d").date() == datetime.date(2023, 1, 2)
    assert datetime.datetime.strptime(order.shipped_date, "%Y-%m-%d").date() == datetime.date(2023, 1, 3)
    assert order.ship_via == shipper
    assert order.freight == 10.0
    assert order.ship_name == "TestShipName"
    assert order.ship_address == "TestShipAddress"
    assert order.ship_city == "TestShipCity"
    assert order.ship_postal_code == "12345"
    assert order.ship_country == "TestShipCountry"

@pytest.mark.django_db
def test_order_details_model():
    # Creating required instances for OrderDetails
    user_e = User.objects.create(email="testemployee@example.com", password="testpassword", user_type=1)
    user_c = User.objects.create(email="testcustomer@example.com", password="testpassword", user_type=4)
    customer = user_c.customer
    employee = user_e.employee
    shipper = Shipper.objects.create(company_name="TestShipper", phone="1234567890")
    category = Category.objects.create(category_name="TestCategory", description="Test category description")
    supplier = Supplier.objects.create(
        company_name="TestSupplier",
        contact_name="TestContact",
        contact_title="TestTitle",
        address="TestAddress",
        city="TestCity",
        postal_code="12345",
        country="TestCountry",
        phone="1234567890"
    )
    product = Product.objects.create(
        product_name="TestProduct",
        supplier_id=supplier,
        category_id=category,
        quantity_per_unit="10",
        unit_price=10.0,
        units_in_stock=100,
        units_on_order=10,
        reorder_level=10,
        discontinued=False
    )
    order = Order.objects.create(
        customer_id=customer,
        employee_id=employee,
        order_date="2023-01-01",
        required_date="2023-01-02",
        shipped_date="2023-01-03",
        ship_via=shipper,
        freight=10,
        ship_name="TestShipName",
        ship_address="TestShipAddress",
        ship_city="TestShipCity",
        ship_postal_code="12345",
        ship_country="TestShipCountry",
    )
    

    # Creating OrderDetails instance
    order_details = OrderDetails.objects.create(
        order_id=order,
        product_id=product,
        unit_price=10.0,
        quantity=5,
        discount=0.0,
        created_by=user_c
    )

    assert order_details.order_id == order
    assert order_details.product_id == product
    assert order_details.unit_price == 10.0
    assert order_details.quantity == 5
    assert order_details.discount == 0.0
    assert order_details.created_by == user_c