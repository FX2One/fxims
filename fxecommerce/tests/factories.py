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

    company_name = factory.Sequence(lambda x: f"company_name_{x}")
    contact_name = factory.Sequence(lambda x: f"contact_name_{x}")
    contact_title = factory.Sequence(lambda x: f"contact_title_{x}")
    address = factory.Sequence(lambda x: f"address_{x}")
    city = factory.Sequence(lambda x:f"city_{x}")
    region = factory.Sequence(lambda x: f"region_{x}")
    postal_code = factory.Sequence(lambda a,b,c,d,e: f"zip_code: {a}{b}:{c}{d}{e}")
    country = factory.Sequence(lambda x: f"country_{x}")
    phone = factory.Sequence(lambda a,b,c,d,e,f,g,h,j: f"phone: {a}{b}{c}-{d}{e}{f}-{g}{h}{j}")
    fax = factory.Sequence(lambda a,b,c,d,e,f,g,h,j: f"fax: {a}{b}{c}-{d}{e}{f}-{g}{h}{j}")
    homepage = factory.Sequence(lambda x: f"www.{x}_homepage_{x}")


'''class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    product_name = factory.Sequence(lambda x: f"product_name_{x}")
    description = factory.Sequence(lambda x: f"description_{x}_{x}_{x} with some long text")
    supplier_id = factory.Sequence(lambda x: x)
    category_id = factory.Sequence(lambda x: x)
    quantity_per_unit = factory.Sequence(lambda x, y: f"amount of {x} in {y} boxes")
    unit_price = factory.Sequence(lambda x: x)
    units_in_stock = factory.Sequence(lambda x: x)
    units_on_order = factory.Sequence(lambda x: x)
    reorder_level = factory.Sequence(lambda x: x)
    discontinued = factory.Sequence(lambda x: x)'''


register(CategoryFactory)

