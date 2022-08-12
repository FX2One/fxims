import pytest
from fxecommerce.inventory import models


"""regular parametrize test"""
'''@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, category_name, description, image",
    [
        (1,'football','footbal','images/default.png'),
        (10,'basketball','basketball','images/default.png'),
        (101,'volleyball','volleyball','images/default.png')
    ],
)
def test_inventory_category_dbfixture(
  db, django_database_fixture_setup, id, category_name, description, image
):
    result = models.Category.objects.get(id=id)
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image'''


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