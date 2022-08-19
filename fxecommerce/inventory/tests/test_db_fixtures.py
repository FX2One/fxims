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
        (1,'football','All equipment related to Sports','default.png'),
        (2,'E-Games','Video games','default.png')
    ],
)
def test_inventory_category_dbfixture(
  db, django_database_fixture_setup, category_id, category_name, description, image
):
    result = models.Category.objects.get(category_id=category_id)
    print(f'cat_id{result.category_id}=={result.category_name}')
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image


"""parametrize with FactoryBoy package"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_name, description, image",
    [
        ('football','All football equipment','default.png'),
        ('basketball','All basketball equipment','default.png'),
        ('volleyball','All volleyball equipment','default.png')

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
    print(f'ticd: {result.category_name}')
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image

"""parametrize using factory.Sequence to autopopulate not defined field"""
"""parametrize with FactoryBoy package"""
@pytest.mark.parametrize(
    "category_name, image",
    [
        ('football','default.png'),
        ('basketball','default.png'),
        ('volleyball','default.png')
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


def load_param_json(json_path):
    with open(json_path) as f:
        return json.load(f)

abs_path = '../fixtures/db_supplier_fixture.json'


def load_test_vals(abs_path,json_id):
    load_test_case = load_param_json(abs_path)
    return load_test_case[json_id]['fields'].values()

jld = JsonLoadData()
cf = ConfigFixture()

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    jld.load_keys(cf.SUPPLIER_FIXTURE),
    [
        ('Adeedas','Adee Das','Adeedas Company','Adee address','Munich','Bavaria','11-222','Germany','777-777-777','777-777-778','adeedas.com'),
        ('Puma','Pumba ','Pumba Company','Pumba address','Berlin','Brandenburgia','21-122','Germany','888-777-777','888-777-778','pumba.com'),
        load_test_vals(abs_path,0),
        load_test_vals(abs_path,1),
        jld.load_values(cf.SUPPLIER_FIXTURE,2)
    ],
)
def test_inventory_supplier_dbfixture_insert(
        db,supplier_factory,company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,homepage
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
    print(result.contact_title)
    print(result.company_name)
    print(result.city)
    print(result.phone)
    print(result.homepage)
    assert result.company_name == company_name
    assert result.contact_title == contact_title
    assert result.city == city
    assert result.region == region
    assert result.postal_code == postal_code
    assert result.country == country
    assert result.phone == phone
    assert result.fax == fax
    assert result.homepage == homepage



'''
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,homepage",
    [
        ('Adidas','Adi Das','Adidas Company','Adi address','Munich','Bawaria','11-222','Germany','777-777-777','777-777-778','adidas.com'),
        ('Nike','Mark Nikovic'),
        ('Puma','Pum Anters'),
        ('Reebok','Reebeca Oklah')
    ],
)
'''
'''@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "db,supplier_factory,company_name,contact_name,contact_title,address,city,region,postal_code,country,phone,fax,homepage",
    [
        ()
    ]
):
def test_inventory_supplier_dbfixture_insert(
    db,
    supplier_factory,
    company_name,
    contact_name,
    contact_title,
    address,
    city,
    region,
    postal_code,
    country,
    phone,
    fax,
    homepage
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
    )'''



'''@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "product_name","description","supplier_id","category_id","unit_price","units_in_stock","units_on_order","reorder_level","discontinued",
    [
        ('Nike Football v2','New 2022 football model',1,1,'24 - 500ml bottles',18,3,1,1,0)
    ],
)
def test_inventory_product_dbfixture(
        db, product_factory,product_name,description,supplier_id,category_id,unit_price,units_in_stock,units_on_order,reorder_level,discontinued
):
    result = product_factory.create(
        product_name=product_name,
        description=description,
        supplier_id=supplier_id,
        category_id=category_id,
        unit_price=unit_price,
        units_in_stock=units_in_stock,
        units_on_order=units_on_order,
        reorder_level=reorder_level,
        discontinued=discontinued
    )
    assert result.product_name == product_name'''


