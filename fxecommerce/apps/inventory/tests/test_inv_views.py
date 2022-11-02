import pytest
from inventory import models
from django.urls import reverse


# https://pytest-django.readthedocs.io/en/latest/helpers.html#django-user-model
# https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client

def test_new_user(django_user_model):
    django_user_model.objects.create(email="test@test.com", password="something")


def test_with_client(client):
    response = client.get('/')
    assert response.status_code == 200


def test_with_authenticated_client(client, django_user_model):
    email = 'test@test.com'
    password = "somesecurepass"
    user = django_user_model.objects.create_user(email=email, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    client.login(email=email, password=password)
    response_employee = client.get('/employee/')
    response_order = client.get('/order/')
    response_products = client.get('/products/')
    response_category = client.get('/category/')
    assert response_employee.status_code == 200
    assert response_order.status_code == 200
    assert response_products.status_code == 200
    assert response_category.status_code == 200

    # prepared data to test slug redirect
    # create Products model
    result = models.Product.objects.create(product_name='Tea', discontinued=True, slug='tea')

    # create response to product detail url
    response = client.get(reverse('inventory:product_detail', args=[result.slug]))
    assert response.status_code == 200

    # check if request path matches reverse response taken
    assert response.request['PATH_INFO'] == f'/products/{result.slug}'


