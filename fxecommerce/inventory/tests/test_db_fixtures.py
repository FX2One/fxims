import pytest
from fxecommerce.inventory import models
import json
from utils import JsonLoadData, ConfigFixture

"""regular parametrize test"""
"""asserts against db_category_fixture_id.json"""


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_id, category_name, description, image",
    [
        (1, 'football', 'All equipment related to Sports', 'default.png'),
        (2, 'E-Games', 'Video games', 'default.png')
    ],
)
def test_inventory_category_dbfixture(
        db, django_database_fixture_setup, category_id, category_name, description, image
):
    result = models.Category.objects.get(category_id=category_id)
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image


"""parametrize with FactoryBoy package"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_name, description, image",
    [
        ('football', 'All football equipment', 'default.png'),
        ('basketball', 'All basketball equipment', 'default.png'),
        ('volleyball', 'All volleyball equipment', 'default.png')

    ],
)
def test_inventory_category_dbfixture_insert_fb(
        db, category_factory, category_name, description, image
):
    result = category_factory.create(
        category_name=category_name,
        description=description,
        image=image
    )
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image


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
def test_inventory_category_dbfixture_insert_fb2(
        db, category_factory, category_name, image
):
    result = category_factory.create(
        category_name=category_name,
        image=image
    )
    assert result.category_name == category_name
    assert result.image == image


jld = JsonLoadData()
cf = ConfigFixture()


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    # parametrize pattern example
    # "company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,homepage"
    jld.load_keys(cf.SUPPLIER_FIXTURE),
    [
        # parameters example
        # ('Adeedas','Adee Das','Adeedas Company','Adee address','Munich','Bavaria','11-222','Germany','777-777-777','777-777-778','adeedas.com'),
        jld.load_values(cf.SUPPLIER_FIXTURE, 0),
        jld.load_values(cf.SUPPLIER_FIXTURE, 1),
        jld.load_values(cf.SUPPLIER_FIXTURE, 2),
    ],
)
def test_inventory_supplier_dbfixture_insert(
        db, supplier_factory, company_name, contact_name, contact_title, address, city, region, postal_code, country,
        phone, fax, homepage
):
    result = supplier_factory.create(
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
    assert result.contact_title == contact_title
    assert result.city == city
    assert result.region == region
    assert result.postal_code == postal_code
    assert result.country == country
    assert result.phone == phone
    assert result.fax == fax
    assert result.homepage == homepage


