import factory
import pytest
import string
from faker import Faker
from pytest_factoryboy import register
from fxecommerce.inventory import models

fake = Faker()
fake.seed_instance(4321)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    category_name = factory.Sequence(lambda x: f"category_name_{x}")
    description = factory.Sequence(lambda x: f"description_{x}")
    image = factory.Sequence(lambda x: f"images{x}/default.png")


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Supplier

    company_name = factory.Faker('company')
    contact_name = factory.Faker('name_nonbinary')
    contact_title = factory.Faker('job')
    address = factory.Faker('address')
    city = factory.Faker('city')
    region = factory.Faker('state')
    postal_code = factory.Faker('zipcode')
    country = factory.Faker('country')
    phone = factory.Faker('phone_number')
    fax = factory.Faker('phone_number')
    homepage = factory.Faker('domain_name')




class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    product_name = factory.Faker('bothify', text='Product_?????####', letters='ABCDE')
    quantity_per_unit = factory.Faker('bothify', text='## boxes x ## bags')
    unit_price = factory.Faker('random_number',digits=5, fix_len=False)
    units_in_stock = factory.Faker('random_number',digits=5, fix_len=False)
    units_on_order = factory.Faker('random_number',digits=5, fix_len=False)
    reorder_level = factory.Faker('random_number',digits=5, fix_len=False)
    discontinued = factory.Faker('random_int',min=0, max=1, step=1)


register(CategoryFactory)
register(SupplierFactory)
register(ProductFactory)
