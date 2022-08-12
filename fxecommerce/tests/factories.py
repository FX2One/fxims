import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from fxecommerce.inventory import models


fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    category_name = factory.Sequence(lambda x: f"category_name_{x}")
    description = factory.Sequence(lambda y: f"description_{y}")
    image = "images/default.png"

register(CategoryFactory)

