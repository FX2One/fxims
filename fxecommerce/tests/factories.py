import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from fxecommerce.inventory import models

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(text="category_name_?????")
    description = fake.lexify(text="description_?????")
    image = "images/default.png"

register(CategoryFactory)

