import pytest
from fxecommerce.inventory import models
import json
from utils import JsonLoadData, ConfigFixture

jld = JsonLoadData()
cf = ConfigFixture()


"""CATEGORY TESTS"""
"""regular parametrize test"""
"""asserts against db_category_fixture_id.json"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_id, category_name, description, image",
    [
        (1, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales', 'default.png'),
        (2, 'Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings', 'default.png')
    ],
)
def test_inventory_category_dbfixture(
        db, django_database_fixture_setup, category_id, category_name, description, image
):
    result = models.Category.objects.get(category_id=category_id)
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image


"""regular parametrize test"""
"""asserts against db_category_fixture_id.json"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.CATEGORY_FIXTURE),
    [
        jld.load_values(cf.CATEGORY_FIXTURE, 0),
        jld.load_values(cf.CATEGORY_FIXTURE, 1)
    ],
)
def test_inventory_category_dbfixture_json_file(
        db, django_database_fixture_setup, category_id, category_name, description, image
):
    result = models.Category.objects.get(category_id=category_id)
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_name, description",
    [
        ('football', 'All football equipment'),
        ('basketball', 'All basketball equipment'),
        ('volleyball', 'All volleyball equipment')
    ],
)
def test_inventory_category_dbfixture_insert(
        db, category_factory, category_name, description
):
    result = category_factory.create(
        category_name=category_name,
        description=description,
    )
    print(result.category_id)
    print(result.category_name)
    print(result.description)
    print(result.image)
    assert result.category_name == category_name
    assert result.description == description



@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.CATEGORY_FIXTURE),
    [
        jld.load_values(cf.CATEGORY_FIXTURE, 0),
        jld.load_values(cf.CATEGORY_FIXTURE, 1),
        jld.load_values(cf.CATEGORY_FIXTURE, 2),
    ],
)
def test_inventory_category_insert_some_db(
        db, category_factory, category_id,category_name, description, image
):
    result = category_factory.create(
        category_id=category_id,
        category_name=category_name,
        description=description
    )
    print(result.category_id)
    print(result.category_name)
    print(result.description)
    assert result.category_name == category_name
    assert result.description == description



"""parametrize using factory.Sequence to autopopulate not defined field"""
"""parametrize with FactoryBoy package"""
@pytest.mark.parametrize(
    "category_name, image",
    [
        ('football', 'default.png'),
        ('basketball', 'default.png'),
        ('volleyball', 'default.png')
    ],
)
def test_inventory_category_dbfixture_insert_fb(
        db, category_factory, category_name, image
):
    result = category_factory.create(
        category_name=category_name,
        image=image
    )
    assert result.category_name == category_name
    assert result.image == image



"""SUPPLIER TESTS"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    # parametrize pattern example utils
    # "company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,homepage",
    jld.load_keys(cf.SUPPLIER_FIXTURE),
    [
        # parameters example utils
        # ('Adeedas','Adee Das','Adeedas Company','Adee address','Munich','Bavaria','11-222','Germany','777-777-777','777-777-778','adeedas.com'),
        jld.load_values(cf.SUPPLIER_FIXTURE, 0),
        jld.load_values(cf.SUPPLIER_FIXTURE, 1),
        jld.load_values(cf.SUPPLIER_FIXTURE, 2),
    ],
)
def test_inventory_supplier_dbfixture_insert(
        db, supplier_factory, supplier_id,company_name, contact_name, contact_title, address, city, region, postal_code, country,
        phone, fax, homepage
):
    result = supplier_factory.create(
        supplier_id=supplier_id,
        company_name=company_name,
        contact_name=contact_name,
        contact_title=contact_title,
        address=address,
        city=city,
        region=region,
        postal_code=postal_code,
        country=country,
        phone=phone,
        fax=fax,
        homepage=homepage
    )
    assert result.company_name == company_name
    assert result.contact_name == contact_name
    assert result.contact_title == contact_title
    assert result.city == city
    assert result.region == region
    assert result.postal_code == postal_code
    assert result.country == country
    assert result.phone == phone
    assert result.fax == fax
    assert result.homepage == homepage


# test against supplier_factory
@pytest.mark.parametrize(
    "company_name",
    [
        ('Adeedas'),
        ('Beedas'),
        ('Locas')
    ],
)
def test_inventory_supplier_factory_insert(
        db,supplier_factory, company_name
):
    result = supplier_factory.create(
        company_name=company_name)
    print(f'company name: {result.company_name}')
    print(f'contact name: {result.contact_name}')
    print(f'contact title: {result.contact_title}')
    print(f'city: {result.city}')
    print(f'region: {result.region}')
    print(f'zip code: {result.postal_code}')
    print(f'country: {result.country}')
    print(f'phone: {result.phone}')
    print(f'fax: {result.fax}')
    print(f'homepage: {result.homepage}')
    assert result.company_name == company_name


# test against database
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.SUPPLIER_FIXTURE),
    [
        jld.load_values(cf.SUPPLIER_FIXTURE, 0),
        jld.load_values(cf.SUPPLIER_FIXTURE, 1),
        jld.load_values(cf.SUPPLIER_FIXTURE, 2),
    ]
)
def test_supplier_on_jld_db_json(
        db, django_database_fixture_setup,supplier_id,company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,homepage
):
    result = models.Supplier.objects.get(supplier_id=supplier_id)
    print(result.fax)
    print(result.company_name)
    print(result.homepage)
    print(result.city)
    assert result.company_name == company_name
    assert result.contact_name == contact_name
    assert result.contact_title == contact_title
    assert result.address == address
    assert result.city == city
    assert result.region == region
    assert result.postal_code == postal_code
    assert result.country == country
    assert result.phone == phone
    assert result.fax == fax
    assert result.homepage == homepage


""" TEST PRODUCTS """

#test with database
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.PRODUCT_FIXTURE),
    [
        jld.load_values(cf.PRODUCT_FIXTURE, 0),
        jld.load_values(cf.PRODUCT_FIXTURE, 1),
        jld.load_values(cf.PRODUCT_FIXTURE, 2),
    ],
)
def test_inventory_product_dbfixture(
        db, django_database_fixture_setup,product_id, product_name,supplier_id,category_id,quantity_per_unit,unit_price,units_in_stock,units_on_order,reorder_level,discontinued
):
    result = models.Product.objects.get(product_id=product_id)
    assert result.product_name == product_name
    assert result.quantity_per_unit == quantity_per_unit
    assert result.unit_price == unit_price
    assert result.units_in_stock == units_in_stock
    assert result.units_on_order == units_on_order
    assert result.reorder_level == reorder_level
    assert result.discontinued == discontinued


#test with factory creation
@pytest.mark.parametrize(
    jld.load_keys(cf.PRODUCT_FIXTURE),
    [
        jld.load_values(cf.PRODUCT_FIXTURE, 0),
        jld.load_values(cf.PRODUCT_FIXTURE, 1),
        jld.load_values(cf.PRODUCT_FIXTURE, 2),
    ],
)
def test_inventory_product_factory(
    db, product_factory, product_id, product_name,supplier_id,category_id,quantity_per_unit,unit_price,units_in_stock,units_on_order,reorder_level,discontinued
):
    result = product_factory.create(product_id=product_id)
    print(result.product_id)
    print(result.product_name)
    print(result.quantity_per_unit)
    print(result.unit_price)
    print(result.units_in_stock)
    print(result.units_on_order)
    print(result.reorder_level)
    print(result.discontinued)
    assert result.product_id == product_id


""" TEST EMPLOYEE """
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.EMPLOYEE_FIXTURE),
    [
        jld.load_values(cf.EMPLOYEE_FIXTURE, 0),
        jld.load_values(cf.EMPLOYEE_FIXTURE, 1),
        jld.load_values(cf.EMPLOYEE_FIXTURE, 2),
    ],
)
def test_inventory_employee_dbfixture(
        db,
        django_database_fixture_setup,
        employee_id,
        last_name,
        first_name,
        title,
        title_of_courtesy,
        birth_date,
        hire_date,
        address,
        city,
        region,
        postal_code,
        country,
        home_phone,
        extension,
        photo,
        notes,
        reports_to,
        photo_path
):
    result = models.Employee.objects.get(employee_id=employee_id)
    result_birth_date = str(result.birth_date)
    result_hire_date = str(result.hire_date)
    assert result.employee_id == employee_id
    assert first_name == first_name
    assert last_name == last_name
    assert title == title
    assert title_of_courtesy == title_of_courtesy
    assert result_birth_date == birth_date
    assert result_hire_date == hire_date
    assert address == address
    assert city == city
    assert region == region
    assert postal_code == postal_code
    assert country == country
    assert home_phone == home_phone
    assert extension == extension
    assert photo == photo
    assert notes == notes
    assert reports_to == reports_to
    assert photo_path == photo_path

""" TEST EMPLOYEE TERRITORIES """
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.EMPLOYEE_TERRITORIES_FIXTURE),
    [
        jld.load_values(cf.EMPLOYEE_TERRITORIES_FIXTURE, 0),
        jld.load_values(cf.EMPLOYEE_TERRITORIES_FIXTURE, 1),
        jld.load_values(cf.EMPLOYEE_TERRITORIES_FIXTURE, 2)
    ],
)
def test_inventory_employee_territories_dbfixture(
        db,
        django_database_fixture_setup,
        employee_id,
        territory_id
):
    '''
    how to tackle ManyToMany relationship in test
    https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/?fbclid=IwAR33HITPlrZhaPmpPtZR9mQDpjLV_ERWcpFASMtqJELTPNSaEac6mEn_0Mw
    '''

    # get Employee objects by ID <containing model contains M2M>
    emp = models.Employee.objects.get(employee_id=employee_id)

    # get Territory objects by ID <other mother M2M is pointed to>
    ter = models.Territory.objects.get(territory_id=territory_id)

    # add Territory to Relation
    emp.territories.add(ter)

    # get first Territory object of M2M relationship between Employee and Territory models
    db_employee_to_territories = emp.territories.first()

    # set two way relationship
    db_territories_set_employee = ter.employee_set.first()

    assert db_employee_to_territories.territory_id == ter.territory_id
    assert db_territories_set_employee.employee_id == emp.employee_id


""" TEST ORDER """
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.ORDER_FIXTURE),
    [
        jld.load_values(cf.ORDER_FIXTURE, 0),
        jld.load_values(cf.ORDER_FIXTURE, 1),
        jld.load_values(cf.ORDER_FIXTURE, 2)
    ],
)
def test_inventory_order_dbfixture(
        db,
        django_database_fixture_setup,
        order_id,
        customer_id,
        employee_id,
        order_date,
        required_date,
        shipped_date,
        ship_via,
        freight,
        ship_name,
        ship_address,
        ship_city,
        ship_region,
        ship_postal_code,
        ship_country
):
    result_order = models.Order.objects.get(order_id=order_id)
    result_customer = models.Customer.objects.get(customer_id=customer_id)
    result_employee = models.Employee.objects.get(employee_id=employee_id)
    result_shipper = models.Shipper.objects.get(shipper_id=ship_via)
    result_order_date = str(result_order.order_date)
    result_required_date = str(result_order.required_date)
    result_shipped_date = str(result_order.shipped_date)

    assert result_customer.customer_id == customer_id
    assert result_employee.employee_id == employee_id
    assert result_order_date == order_date
    assert result_required_date == required_date
    assert result_shipped_date == shipped_date
    assert result_shipper.shipper_id == ship_via

    assert str(result_order.ship_via) == str(ship_via)
    assert str(result_order.freight) == str(freight)

    assert result_order.ship_name == ship_name
    assert result_order.ship_address == ship_address
    assert result_order.ship_city == ship_city
    assert result_order.ship_region == ship_region
    assert result_order.ship_postal_code == ship_postal_code
    assert result_order.ship_country == ship_country








