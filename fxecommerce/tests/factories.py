import factory
import pytest
import string
from faker import Faker
from pytest_factoryboy import register
from fxecommerce.inventory import models
import factory.fuzzy

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    category_name = factory.Sequence(lambda x: f"category_name_{x}")
    description = factory.Sequence(lambda x: f"description_{x}")
    image = "images/default.png"


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Supplier

    company_name = factory.Faker('company')
    contact_name = fake.lexify(text="contact_name_??????")
    contact_title = factory.Sequence(lambda x: f"contact_title_{x}")
    address = factory.Faker('address')
    city = factory.Faker('city')
    region = factory.Faker('state')
    postal_code = factory.Faker('zipcode')
    country = factory.Faker('country')
    phone = factory.Faker('phone_number')
    fax = factory.Faker('fax')
    homepage = fake.lexify(text="homepage_??????")




'''class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    product_name = factory.Sequence(lambda x: f"product_name_{x}")
    description = factory.Sequence(lambda x: f"description_{x} with some long text")
    supplier_id = factory.Sequence(lambda x: x)
    category_id = factory.Sequence(lambda x: x)
    quantity_per_unit = factory.Sequence(lambda x, y: f"amount of {x} in {y} boxes")
    unit_price = factory.Sequence(lambda x: x)
    units_in_stock = factory.Sequence(lambda x: x)
    units_on_order = factory.Sequence(lambda x: x)
    reorder_level = factory.Sequence(lambda x: x)
    discontinued = factory.Sequence(lambda x: x)'''


register(CategoryFactory)
register(SupplierFactory)
