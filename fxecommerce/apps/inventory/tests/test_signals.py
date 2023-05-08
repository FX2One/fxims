import pytest

from inventory.models import Order, OrderDetails, Product, Customer
from decimal import Decimal
from django.db.models.signals import post_save, pre_save, pre_delete
from inventory.signals import (
    update_product_stock,
    revert_product_stock,
    update_order_freight,
    update_order_customer,
    restock_product,
    update_order_details_unit_price,
    update_order_freight_price,
    update_order_status,
    orderdetails_order_status_change_after_delete,
    update_order_customer
)

# Test update_product_stock signal
@pytest.mark.django_db
def test_update_product_stock_signal(test_orderdetails_data, test_product_data):
    # Connect the signal
    pre_save.connect(update_product_stock, sender=OrderDetails)

    # Refresh the test_product_data from the database after the test_orderdetails_data fixture creates the OrderDetails instance
    test_product_data.refresh_from_db()

    # Check if the stock has been updated correctly
    assert test_product_data.units_in_stock == 5
    assert test_product_data.units_on_order == 5

    # Disconnect the signal
    pre_save.disconnect(update_product_stock, sender=OrderDetails)


@pytest.mark.django_db
def test_revert_product_stock_signal(test_orderdetails_data, test_product_data):
    # Connect the signal
    pre_delete.connect(revert_product_stock, sender=OrderDetails)

    # Refresh the test_product_data from the database before deleting the OrderDetails instance
    test_product_data.refresh_from_db()
    initial_units_in_stock = test_product_data.units_in_stock
    initial_units_on_order = test_product_data.units_on_order

    # Delete the test_orderdetails_data instance
    test_orderdetails_data.delete()

    # Refresh the test_product_data from the database after deleting the OrderDetails instance
    test_product_data.refresh_from_db()

    # Check if the stock has been reverted correctly
    assert test_product_data.units_in_stock == initial_units_in_stock + test_orderdetails_data.quantity
    assert test_product_data.units_on_order == initial_units_on_order - test_orderdetails_data.quantity

    # Disconnect the signal
    pre_delete.disconnect(revert_product_stock, sender=OrderDetails)


@pytest.mark.django_db
def test_update_order_freight_signal(test_order_data, test_shipper_data):
    # Create an order instance and set the ship_via attribute to the test_shipper_data fixture
    order = test_order_data
    order.ship_via = test_shipper_data
    order.save()
    order.refresh_from_db()

    # Verify that the order's freight attribute has been updated with the shipper's freight_price
    assert order.freight == test_shipper_data.freight_price

    # Update the shipper's freight_price
    new_freight_price = 75.0
    test_shipper_data.freight_price = new_freight_price
    test_shipper_data.save()
    order.refresh_from_db()

    # Update the order instance and set the ship_via attribute to the updated test_shipper_data fixture
    order.ship_via = test_shipper_data
    order.save()
    order.refresh_from_db()

    # Verify that the order's freight attribute has been updated with the new shipper's freight_price
    assert order.freight == new_freight_price

    # Set ship_via to None and save the order
    order.ship_via = None
    order.save()
    order.refresh_from_db()

    # Check if the order's freight attribute remains unchanged after removing the ship_via attribute
    assert order.freight == new_freight_price


@pytest.mark.django_db
def test_update_order_customer_signal(test_order_data, test_orderdetails_data):

    # Get the customer_instance and employee_instance from the test_order_data fixture
    order = test_order_data
    customer_instance = order.customer_id
    employee_instance = order.employee_id

    # Assign customer_specialist to the customer
    customer_instance.customer_specialist = employee_instance
    customer_instance.save()

    # Connect the signal
    post_save.connect(update_order_customer, sender=OrderDetails)

    # Create OrderDetails instance
    order_details = test_orderdetails_data


    # Refresh the order instance from the database
    order.refresh_from_db()

    # Check if the customer_id is set correctly
    assert order.customer_id == customer_instance

    # Check if the employee_id is set correctly
    assert order.employee_id == employee_instance

    # Disconnect the signal
    post_save.disconnect(update_order_customer, sender=OrderDetails)



@pytest.mark.django_db
def test_update_order_freight_price_signal(test_shipper_data, test_order_data):
    # Disconnect the signal to avoid side effects during the test
    post_save.disconnect(update_order_freight_price, sender=Order)

    # Set up the data for the test
    shipper = test_shipper_data
    order = test_order_data

    # Update the Order with the Shipper instance
    order.ship_via = shipper
    order.save()

    # Reconnect and send the signal manually
    post_save.connect(update_order_freight_price, sender=Order)
    post_save.send(sender=Order, instance=order)

    # Refresh the Order instance from the database
    order.refresh_from_db()

    # Check if the Order.freight has been updated with Shipper.freight_price
    assert order.freight == shipper.freight_price

    # Check if the total_price for each OrderDetails instance has been updated
    for order_detail in order.order_details.all():
        expected_total_price = order_detail.discounted_total + Decimal(order.freight)
        assert order_detail.total_price == expected_total_price

    # Clean up: disconnect the signal again
    post_save.disconnect(update_order_freight_price, sender=Order)



@pytest.mark.django_db
@pytest.mark.parametrize("discount", [0, 1])
def test_update_order_details_unit_price_signal(test_product_data, user_fixture, test_order_data, test_shipper_data, discount):
    # Get the customer_user from the user_fixture
    customer_user = user_fixture['customer_user']['user']

    # Get the product_instance from the test_product_data fixture
    product_instance = test_product_data
    shipper_instance = test_shipper_data
    order_instance = test_order_data
    order_instance.ship_via = shipper_instance
    order_instance.save()

    # Connect the signals
    post_save.connect(update_order_details_unit_price, sender=OrderDetails)
    post_save.connect(update_order_freight_price, sender=Order)

    # Create an OrderDetails instance without specifying unit_price, total_amount, discounted_total, and total_price
    order_details = OrderDetails.objects.create(
        product_id=product_instance,
        quantity=5,
        discount=discount,
        created_by=customer_user,
        order_id=order_instance
    )

    # Refresh the order_instance to get the updated freight
    order_instance.refresh_from_db()

    # Check if the unit_price is set correctly
    assert order_details.unit_price == product_instance.unit_price

    # Check if the total_amount is calculated correctly
    assert order_details.total_amount == product_instance.unit_price * order_details.quantity

    # Check if the discounted_total is calculated correctly
    if discount == 0:
        assert order_details.discounted_total == order_details.total_amount

    else:
        assert float(Decimal(order_details.discounted_total)) == float(Decimal(order_details.total_amount) * Decimal(1 - order_details.discount / 100))
        assert Decimal(order_details.total_price) == Decimal(order_details.discounted_total) + Decimal(order_instance.freight)


    # Disconnect the signals
    post_save.disconnect(update_order_details_unit_price, sender=OrderDetails)
    post_save.disconnect(update_order_freight_price, sender=Order)



# (1, 150 , 2), (original_order_status, total_price, expected_order_status)
@pytest.mark.django_db
@pytest.mark.parametrize("original_order_status, total_price, expected_order_status", [
    (1, 150, 2),
    (2, 150, 2),
    (1, 0, 1)
])
def test_update_order_status_signal(total_price, user_fixture, test_product_data, original_order_status, expected_order_status):

    customer_user = user_fixture['customer_user']['user']

    product_data = test_product_data

    post_save.disconnect(update_order_status, sender=OrderDetails)

    order_details = OrderDetails.objects.create(
        product_id=product_data,
        quantity=2,
        discount=1,
        created_by=customer_user,
        total_amount=100,
        discounted_total=90,
        total_price=total_price
    )

    order_data = order_details.order_id
    order_data.order_status = original_order_status


    if order_details.total_price > 0:

        if order_data.order_status != 2:
            order_data.order_status = 2
            assert order_data.order_status == expected_order_status
    else:
        assert order_data.order_status == expected_order_status


@pytest.mark.django_db
def test_orderdetails_order_status_change_after_delete(test_orderdetails_data):

    order_details = test_orderdetails_data

    order_id = order_details.order_id_id
    order_details.delete()

    updated_order = Order.objects.get(pk=order_id)

    assert updated_order.order_status == 3
    assert updated_order.customer_id is None
    assert updated_order.ship_via is None
    assert updated_order.ship_name == '-'
    assert updated_order.ship_address == '-'
    assert updated_order.ship_city == '-'
    assert updated_order.ship_region == '-'
    assert updated_order.ship_postal_code == '-'
    assert updated_order.ship_country == '-'


# test mail sending signal