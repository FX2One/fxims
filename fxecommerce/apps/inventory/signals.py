
from django.dispatch import receiver
from .models import Order, OrderDetails, Product, Shipper, Category, Supplier, Region
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from users.models import Customer, User, Employee
from django.core.validators import MinValueValidator
from . import utils as const
from django.core.mail import send_mail
from django.conf import settings
from decimal import Decimal

@receiver(pre_save, sender=OrderDetails)
def update_product_stock(sender, instance, **kwargs):
    # template error to employee in views to be done /admin panel form ???
    existing_order_details = OrderDetails.objects.filter(order_id=instance.order_id)
    if existing_order_details.exists() and existing_order_details[0].id != instance.id:
        raise ValidationError("OrderDetails with order_id already exists")

    if instance.pk is None:
        instance.product_id.units_in_stock -= instance.quantity
        instance.product_id.units_on_order += instance.quantity
        instance.product_id.save(update_fields=['units_in_stock', 'units_on_order'])


@receiver(pre_delete, sender=OrderDetails)
def revert_product_stock(sender, instance, **kwargs):
    try:
        original_product = Product.objects.get(pk=instance.product_id.pk)
    except Product.DoesNotExist:
        return

    original_product.units_in_stock += instance.quantity
    original_product.units_on_order -= instance.quantity
    original_product.save(update_fields=['units_in_stock', 'units_on_order'])



@receiver(pre_save, sender=Order)
def update_order_freight(sender, instance, **kwargs):
    # Check if the instance has a related Shipper
    if instance.ship_via:
        shipper = instance.ship_via
        try:
            if shipper.freight_price is not None:
                instance.freight = shipper.freight_price
        except Shipper.DoesNotExist:
            pass



@receiver(post_save, sender=OrderDetails)
def update_order_customer(sender, instance, created, **kwargs):
    if created and instance.created_by.user_type == 4:  # check if user is a customer
        order = instance.order_id  # assign instance order_id to Order.order_id
        customer = Customer.objects.get(user=instance.created_by)  # get object id by OrderDetails.created_by
        order.customer_id = customer  # Order.customer_id is exactly the same User.customer
        if hasattr(customer, 'customer_specialist'):
            order.employee_id = customer.customer_specialist  # assign employee_id to order if customer has customer_specialist
        order.save()


@receiver(pre_save, sender=Product)
def restock_product(sender, instance, **kwargs):
    if instance.units_in_stock < instance.reorder_level:
        subject = f"FXIMS: Time to restock {instance.product_name}"
        message = f'Time to restock: {instance.product_name} is on {instance.units_in_stock} units left'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = []
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

@receiver(post_save, sender=OrderDetails)
def update_order_details_unit_price(sender, instance, **kwargs):
    """Update the OrderDetails.unit_price with Product.unit_price"""
    if instance.product_id and not instance.unit_price:
        instance.unit_price = instance.product_id.unit_price
        instance.total_amount = instance.unit_price * instance.quantity
        if instance.discount == 0:
            instance.discounted_total = instance.total_amount
        elif instance.discount:
            instance.discounted_total = instance.total_amount - (instance.total_amount * (instance.discount / 100))
            if instance.order_id.freight:
                instance.total_price = Decimal(instance.discounted_total) + Decimal(instance.order_id.freight)
        instance.save()


@receiver(post_save, sender=Order)
def update_order_freight_price(sender, instance, **kwargs):
    # Update the Order.freight with Shipper.freight_price
    if instance.ship_via and not instance.freight:
        instance.freight = instance.ship_via.freight_price
        instance.save()

    if instance.freight:
        # Get the related OrderDetails instances
        order_details = instance.orders.all()

        # Update the total_price for each instance
        for order_detail in order_details:
            order_detail.total_price = order_detail.discounted_total + Decimal(instance.freight)
            order_detail.save()


@receiver(post_save, sender=OrderDetails)
def update_order_status(sender, instance, **kwargs):
    # Check if the total_price of the OrderDetail instance is greater than 0
    if instance.total_price > 0:
        # Get the related Order instance
        order = instance.order_id

        # Check if the order_status of the Order instance is not already 2
        if order.order_status != 2:
            # Update the order_status to 2 and save the Order instance
            order.order_status = 2
            order.save()


@receiver(post_delete, sender=OrderDetails)
def orderdetails_order_status_change_after_delete(sender, instance, **kwargs):
    if instance.order_id:  # Check if the OrderDetails instance had an order_id
        order = instance.order_id
        order.order_status = 3
        order.customer_id = None
        order.ship_via = None

        cancel = '-'
        order.ship_name = cancel
        order.ship_address = cancel
        order.ship_city = cancel
        order.ship_region = cancel
        order.ship_postal_code = cancel
        order.ship_country = cancel
        order.save()


@receiver(post_save, sender=OrderDetails)
def update_order_customer(sender, instance, created, **kwargs):
    if created and instance.created_by.user_type == 4:  # check if user is a customer
        order = instance.order_id  # assign instance order_id to Order.order_id
        customer = Customer.objects.get(user=instance.created_by)  # get object id by OrderDetails.created_by
        order.customer_id = customer  # Order.customer_id is exactly the same User.customer
        if hasattr(customer, 'customer_specialist'):
            order.employee_id = customer.customer_specialist  # assign employee_id to order if customer has customer_specialist
        order.save()