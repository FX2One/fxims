import factory
import pytest
import string
from faker import Faker
from pytest_factoryboy import register
from fxecommerce.inventory import models

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

    product_name = fake.lexify(text='product_??????????')
    supplier_id = fake.random_digit_not_null()
    category_id = fake.random_digit_not_null()
    quantity_per_unit = fake.lexify(text='amount ?? in 1 box which contains ?? on pallete')
    unit_price = fake.random_number(digits=5, fix_len=False)
    units_in_stock = fake.random_number(digits=5, fix_len=False)
    units_on_order = fake.random_number(digits=5, fix_len=False)
    reorder_level = fake.random_number(digits=5, fix_len=False)
    discontinued = fake.random_int(min=0, max=1, step=1)


register(CategoryFactory)
register(SupplierFactory)
register(ProductFactory)
