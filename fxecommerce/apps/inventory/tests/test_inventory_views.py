import pytest
from django.urls import reverse
from inventory.models import Category, OrderDetails, Supplier, Product, Order
from users.models import Employee, Customer, User
from datetime import datetime
from django.core.exceptions import PermissionDenied

@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'customer_user', 'employee_user'])
def test_category_create_view(client, user_fixture, test_category_data, user_key):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    client.login(email=user.email, password=password)
    response = client.post(reverse('inventory:category_new'), test_category_data)

    if user_key in ['employee_user', 'extra_staff_user']:
        assert response.url == reverse('inventory:category')
        assert response.status_code == 302
        assert Category.objects.filter(category_name=test_category_data['category_name']).exists()
    else:
        assert response.url == reverse('inventory:home')
        assert response.status_code == 302
        assert not Category.objects.filter(category_name=test_category_data['category_name']).exists()


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'customer_user', 'employee_user'])
def test_category_list_view(client, user_fixture, categories_data, user_key):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    client.login(email=user.email, password=password)
    response = client.get(reverse('inventory:category'))

    assert response.status_code == 200

    for category in categories_data:
        assert category.category_name in response.content.decode()
    assert all(category.category_name in response.content.decode()
               for category in categories_data)

@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'customer_user', 'employee_user'])
def test_order_details_create_view(client, user_fixture, user_key, test_product_data, test_orderdetails_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    test_product = test_product_data
    customer_user = user_fixture['customer_user']['user']

    client.login(email=user.email, password=password)
    url = reverse('inventory:order_new')

    if user_key in ['employee_user', 'extra_staff_user', 'customer_user']:
        order_data_post = {
            "product_id": test_product.product_id,
            "quantity": test_orderdetails_data.quantity,
            "unit_price": test_orderdetails_data.unit_price,
            "discount": test_orderdetails_data.discount,
            "created_by": customer_user.id
        }

        response = client.post(url, order_data_post)

        assert response.status_code == 302
        assert response.url == reverse('inventory:order')
        assert OrderDetails.objects.filter(product_id=test_product.product_id, quantity=test_orderdetails_data.quantity).exists()
    else:
        assert not OrderDetails.objects.filter(product_id=test_product.product_id, quantity=test_orderdetails_data.quantity).exists()



@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'customer_user', 'employee_user'])
def test_order_details_update_view(client, user_fixture, user_key, test_product_data, test_orderdetails_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    test_product = test_product_data
    customer_user = user_fixture['customer_user']['user']

    client.login(email=user.email, password=password)
    url = reverse('inventory:order_edit', args=[test_orderdetails_data.id])

    updated_quantity = 3
    updated_discount = 1

    order_data_post = {
        "product_id": test_product.product_id,
        "quantity": updated_quantity,
        "unit_price": test_orderdetails_data.unit_price,
        "discount": updated_discount,
        "created_by": customer_user.id
    }

    if user_key in ['employee_user', 'extra_staff_user', 'customer_user']:
        response = client.post(url, order_data_post)

        assert response.status_code == 302
        assert OrderDetails.objects.filter(id=test_orderdetails_data.id, quantity=updated_quantity).exists()

    else:
        assert not OrderDetails.objects.filter(id=test_orderdetails_data.id, quantity=updated_quantity).exists()


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'customer_user', 'employee_user'])
def test_order_details_delete_view(client, user_fixture, user_key, test_orderdetails_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']


    client.login(email=user.email, password=password)
    url = reverse('inventory:order_delete', args=[test_orderdetails_data.id])

    if user_key in ['employee_user', 'extra_staff_user', 'customer_user']:
        response = client.post(url)

        assert response.status_code == 302
        assert not OrderDetails.objects.filter(id=test_orderdetails_data.id).exists()

    else:
        assert OrderDetails.objects.filter(id=test_orderdetails_data.id).exists()


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'employee_user', 'customer_user'])
def test_order_specification_detail_view(client, user_fixture, user_key, order_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    test_order = order_data

    client.login(email=user.email, password=password)
    url = reverse('inventory:order_detail', args=[test_order.order_id])

    if user_key in ['employee_user', 'extra_staff_user']:
        response = client.get(url)
        assert response.status_code == 200
    else:
        response = client.get(url)
        assert response.status_code == 403



@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'employee_user', 'customer_user'])
def test_product_list_view(client, user_fixture, user_key, products_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    client.login(email=user.email, password=password)
    url = reverse('inventory:product_list')

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['object_list']) == len(products_data)


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'employee_user', 'customer_user'])
def test_product_detail_view(client, user_fixture, user_key, test_product_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    test_product = test_product_data
    client.login(email=user.email, password=password)
    url = reverse('inventory:product_detail', args=[test_product.slug])

    if user_key in ['employee_user', 'extra_staff_user']:
        response = client.get(url)
        assert response.status_code == 200
        assert response.context['product'] == test_product

    else:
        response = client.get(url)
        assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'employee_user', 'customer_user'])
def test_product_create_view(client, user_fixture, user_key, test_category_data, test_supplier_data, test_product_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    client.login(email=user.email, password=password)
    url = reverse('inventory:product_new')

    product_data = {
        'product_name': test_product_data.product_name,
        'supplier_id': test_supplier_data.supplier_id,
        'category_id': test_category_data.category_id,
        'quantity_per_unit': test_product_data.quantity_per_unit,
        'unit_price': test_product_data.unit_price,
        'units_in_stock': test_product_data.units_in_stock,
        'units_on_order': test_product_data.units_on_order,
        'reorder_level': test_product_data.reorder_level,
        'discontinued': test_product_data.discontinued
    }

    if user_key in ['extra_staff_user', 'employee_user']:
        response = client.post(url, data=product_data)

        assert response.status_code == 302
        assert response.url == reverse('inventory:product_list')

        # Check if the new product was created in the database
        new_product = Product.objects.filter(product_name=product_data['product_name']).first()
        assert new_product is not None
        assert Product.objects.filter(product_id=new_product.product_id).exists()

    else:
        response = client.post(url, data=product_data)
        assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'employee_user', 'customer_user'])
def test_product_update_view(client, user_fixture, user_key, test_category_data, test_supplier_data, test_product_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    client.login(email=user.email, password=password)
    url = reverse('inventory:product_edit', kwargs={'slug': test_product_data.slug})

    updated_product_data = {
        'product_name': 'Updated Product Name',
        'supplier_id': test_supplier_data.supplier_id,
        'category_id': test_category_data.category_id,
        'quantity_per_unit': 15,
        'unit_price': 25.0,
        'units_in_stock': 20,
        'units_on_order': 5,
        'reorder_level': 5,
        'discontinued': False
    }

    if user_key in ['extra_staff_user', 'employee_user']:
        response = client.post(url, data=updated_product_data)

        assert response.status_code == 302
        assert response.url == reverse('inventory:product_list')

        # Check if the product was updated in the database
        updated_product = Product.objects.get(product_id=test_product_data.product_id)
        assert updated_product.product_name == updated_product_data['product_name']
        assert int(updated_product.quantity_per_unit) == int(updated_product_data['quantity_per_unit'])
        assert updated_product.unit_price == updated_product_data['unit_price']
        assert updated_product.units_in_stock == updated_product_data['units_in_stock']
        assert updated_product.units_on_order == updated_product_data['units_on_order']
        assert updated_product.reorder_level == updated_product_data['reorder_level']
        assert updated_product.discontinued == updated_product_data['discontinued']

    else:
        response = client.post(url, data=updated_product_data)
        assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize("user_key", ['extra_staff_user', 'employee_user', 'customer_user'])
def test_product_delete_view(client, user_fixture, user_key, test_product_data):
    user_data = user_fixture[user_key]
    user = user_data['user']
    password = user_data['password']

    client.login(email=user.email, password=password)
    product_to_delete = test_product_data
    url = reverse('inventory:product_delete', kwargs={'slug': product_to_delete.slug})

    if user_key in ['extra_staff_user', 'employee_user']:
        response = client.post(url)

        assert response.status_code == 302
        assert response.url == reverse('inventory:product_list')

        # Check if the product was deleted from the database
        assert not Product.objects.filter(product_id=product_to_delete.product_id).exists()

    else:
        response = client.post(url)
        assert response.status_code == 403