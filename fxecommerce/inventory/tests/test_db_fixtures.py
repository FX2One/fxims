import pytest
from fxecommerce.inventory import models


"""regular parametrize test"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_id, category_name, description, image",
    [
        (1,'football','All equipment related to Sports','default.png')
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
    print(result.category_name)
    assert result.category_name == category_name
    assert result.image == image





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


