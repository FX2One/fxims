# https://simpleisbetterthancomplex.com/tips/2016/10/17/django-tip-18-translations.html
# usage of ugettext_lazy
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from .managers import ProductManager, OrderDetailsManager, OrderManager, CategoryManager
import uuid
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from users.models import Customer, User, Employee
from django.core.validators import MinValueValidator
from . import utils as const
from django.core.mail import send_mail
from django.conf import settings

class Region(models.Model):
    region_id = models.PositiveSmallIntegerField(
        verbose_name=_('Region id'),
        db_column='RegionID',
        primary_key=True
    )
    region_description = models.CharField(
        verbose_name=_('Region description'),
        db_column='RegionDescription',
        max_length=50
    )

    class Meta:
        db_table = 'region'
        verbose_name_plural = _('Regions')

    def __str__(self):
        return self.region_description


class Territory(models.Model):
    territory_id = models.CharField(
        verbose_name=_('Territory id'),
        db_column='TerritoryID',
        primary_key=True,
        max_length=20
    )
    territory_description = models.CharField(
        verbose_name=_('Territory description'),
        db_column='TerritoryDescription',
        max_length=50
    )
    region_id = models.ForeignKey(
        Region,
        db_column='RegionID',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'territory'
        verbose_name_plural = _('Territories')

    def __str__(self):
        return self.territory_description


class EmployeeTerritory(models.Model):
    employee_id = models.ForeignKey(
        'users.Employee',
        db_column='EmployeeID',
        on_delete=models.CASCADE
    )
    territory_id = models.ForeignKey(
        Territory,
        db_column='TerritoryID',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'employee_territories'
        verbose_name_plural = _('Employee territories')


class Shipper(models.Model):
    shipper_id = models.AutoField(
        verbose_name=_('Shipper ID'),
        db_column='ShipperID',
        primary_key=True
    )
    company_name = models.CharField(
        verbose_name=_('Company name'),
        db_column='CompanyName',
        max_length=40,
        blank=False,
        null=False
    )
    phone = models.CharField(
        _('Phone'),
        db_column='Phone',
        max_length=24,
        blank=False,
        null=False
    )

    freight_price = models.DecimalField(
        verbose_name=_('Freight price'),
        db_column='FreightPrice',
        null=True,
        max_digits=19,
        decimal_places=4,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        db_table = 'shipper'
        verbose_name_plural = _('Shippers')

    def __str__(self):
        return str(self.company_name)


class CustomerDemographics(models.Model):
    customer_type_id = models.CharField(
        verbose_name=_('Customer Type_ID'),
        db_column='CustomerTypeID',
        primary_key=True,
        max_length=5
    )
    customer_desc = models.TextField(
        verbose_name=_('Customer description'),
        db_column='CustomerDesc',
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'customerdemographics'

    def __str__(self):
        return self.customer_type_id


class CustomerCustomerDemo(models.Model):
    customer_id = models.ForeignKey(
        "users.Customer",
        db_column='CustomerID',
        on_delete=models.CASCADE
    )
    customer_type_id = models.ForeignKey(
        CustomerDemographics,
        db_column='CustomerTypeID',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'customer_customer_demo'
        verbose_name_plural = _('CustomerCustomerDemos')


class Category(models.Model):
    category_id = models.AutoField(
        verbose_name=_('Category ID'),
        db_column='CategoryID',
        primary_key=True
    )
    category_name = models.CharField(
        verbose_name=_('Category name'),
        db_column='CategoryName',
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        help_text=_("format: required. Max_length: 100")
    )
    description = models.TextField(
        verbose_name=_('Description'),
        db_column='Description',
        max_length=150,
        blank=False,
        null=False,
        help_text=_("format: required. Max_length: 150")
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        db_column='Image',
        blank=True,
        upload_to='category/'
    )

    objects = CategoryManager()


    class Meta:
        db_table = 'category'
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_id = models.AutoField(
        verbose_name=_('Supplier ID'),
        db_column='SupplierID',
        primary_key=True
    )
    company_name = models.CharField(
        verbose_name=_('Company name'),
        db_column='CompanyName',
        max_length=40,
        blank=False,
        null=False
    )
    contact_name = models.CharField(
        verbose_name=_('Contact name'),
        db_column='ContactName',
        max_length=30,
        blank=False,
        null=False
    )
    contact_title = models.CharField(
        verbose_name=_('Contact title'),
        db_column='ContactTitle',
        max_length=30,
        blank=False,
        null=False
    )
    address = models.CharField(
        verbose_name=_('Address'),
        db_column='Address',
        max_length=60,
        blank=False,
        null=False
    )
    city = models.CharField(
        verbose_name=_('City'),
        db_column='City',
        max_length=15,
        blank=False,
        null=False
    )
    region = models.CharField(
        verbose_name=_('Region'),
        db_column='Region',
        max_length=15,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        verbose_name=_('Postal code'),
        db_column='PostalCode',
        max_length=10,
        blank=False,
        null=False
    )
    country = models.CharField(
        verbose_name=_('Country'),
        db_column='Country',
        max_length=15,
        blank=False,
        null=False
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        db_column='Phone',
        max_length=24,
        blank=False,
        null=False
    )
    fax = models.CharField(
        verbose_name=_('Fax'),
        db_column='Fax',
        max_length=24,
        blank=True,
        null=True
    )
    homepage = models.TextField(
        verbose_name=_('HomePage'),
        db_column='HomePage',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'supplier'
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_id = models.AutoField(
        verbose_name=_('Product ID'),
        db_column='ProductID',
        primary_key=True
    )
    product_name = models.CharField(
        verbose_name=_('Product name'),
        db_column='ProductName',
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        help_text=_("format: required. max_length: 100")
    )
    supplier_id = models.ForeignKey(
        Supplier,
        db_column='SupplierID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    category_id = models.ForeignKey(
        Category,
        db_column='CategoryID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE
    )
    quantity_per_unit = models.CharField(
        verbose_name=_('Quantity per Unit'),
        db_column='QuantityPerUnit',
        max_length=20,
        blank=False,
        null=False
    )
    unit_price = models.DecimalField(
        verbose_name=_('Unit price'),
        db_column='UnitPrice',
        null=True,
        max_digits=19,
        decimal_places=4,
        validators=[MinValueValidator(0)]
    )
    units_in_stock = models.SmallIntegerField(
        verbose_name=_('Units in Stock'),
        db_column='UnitsInStock',
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
    units_on_order = models.SmallIntegerField(
        verbose_name=_('Units on Order'),
        db_column='UnitsOnOrder',
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
    reorder_level = models.SmallIntegerField(
        verbose_name=_('Reorder level'),
        db_column='ReorderLevel',
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
    discontinued = models.BooleanField(
        verbose_name=_('Discontinued'),
        db_column='Discontinued',
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        null=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        generate_uuid = uuid.uuid4()
        slug_uuid = generate_uuid.hex

        self.slug = slugify(slug_uuid)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('inventory:product_detail', kwargs={'slug': self.slug})

    objects = ProductManager()

    class Meta:
        db_table = 'product'
        verbose_name_plural = _("Products")
        ordering = ['product_name']


class Order(models.Model):
    order_id = models.AutoField(
        verbose_name=_('Order ID'),
        db_column='OrderID',
        primary_key=True,
    )
    customer_id = models.ForeignKey(
        "users.Customer",
        db_column='CustomerID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    employee_id = models.ForeignKey(
        'users.Employee',
        db_column='EmployeeID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    order_date = models.DateField(
        verbose_name=_('Order date'),
        db_column='OrderDate',
        blank=True,
        null=True,
        db_index=True
    )
    required_date = models.DateField(
        verbose_name=_('Required_date'),
        db_column='RequiredDate',
        blank=True,
        null=True
    )
    shipped_date = models.DateField(
        verbose_name=_('Shipped date'),
        db_column='ShippedDate',
        blank=True,
        null=True,
        db_index=True
    )
    ship_via = models.ForeignKey(
        Shipper,
        db_column='ShipVia',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE
    )

    freight = models.DecimalField(
        verbose_name=_('Freight'),
        db_column='Freight',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4,
        default=None
    )

    data_insert_msg = '--- insert data ---'

    ship_name = models.CharField(
        verbose_name=_('Ship name'),
        db_column='ShipName',
        max_length=40,
        blank=False,
        null=False,
        default=data_insert_msg
    )

    ship_address = models.CharField(
        verbose_name=_('Ship address'),
        db_column='ShipAddress',
        max_length=60,
        blank=False,
        null=False,
        default=data_insert_msg
    )

    ship_city = models.CharField(
        verbose_name=_('Ship city'),
        db_column='ShipCity',
        max_length=40,
        blank=False,
        null=False,
        default=data_insert_msg
    )

    ship_region = models.CharField(
        verbose_name=_('Ship region'),
        db_column='ShipRegion',
        max_length=40,
        blank=True,
        null=True,
        default=data_insert_msg
    )

    ship_postal_code = models.CharField(
        verbose_name=_('Ship postal code'),
        db_column='ShipPostalCode',
        max_length=40,
        blank=False,
        null=False,
        db_index=True,
        default=data_insert_msg
    )

    ship_country = models.CharField(
        verbose_name=_('Shipped country'),
        db_column='ShipCountry',
        max_length=40,
        blank=False,
        null=False,
        default=data_insert_msg
    )

    order_status = models.PositiveSmallIntegerField(choices=const.ORDER_STATUS, default=1)

    order_details = models.ManyToManyField(
        Product,
        verbose_name=_('Products'),
        blank=True,
        through='OrderDetails'
    )

    objects = OrderManager()


    class Meta:
        db_table = 'order'
        verbose_name_plural = _("Orders")
        ordering = ['-order_id']

    def __str__(self):
        return f'Order ID: {str(self.order_id)} [ordered for {self.customer_id}]'


class OrderDetails(models.Model):
    order_id = models.ForeignKey(
        Order,
        db_column='OrderID',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
        related_name='orders',
    )

    product_id = models.ForeignKey(
        Product,
        db_column='ProductID',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    unit_price = models.DecimalField(
        verbose_name=_('Unit price'),
        db_column='UnitPrice',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4,
        default=None
    )

    quantity = models.SmallIntegerField(
        verbose_name=_('Quantity'),
        db_column='Quantity'
    )

    discount = models.DecimalField(
        verbose_name=_('Discount'),
        db_column='Discount',
        null=True,
        blank=True,
        max_digits=19,
        decimal_places=4,
        default=0,
    )

    created_by = models.ForeignKey(
        User,
        verbose_name=_('Created by'),
        on_delete=models.CASCADE,
        related_name='orders_created',
        blank=True,
        null=True,
    )

    total_amount = models.DecimalField(
        verbose_name=_('Total amount'),
        db_column='TotalAmount',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4,
        default=0
    )

    discounted_total = models.DecimalField(
        verbose_name=_('Discounted total'),
        db_column='DiscountedTotal',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4,
        default=0
    )

    total_price = models.DecimalField(
        verbose_name=_('Total price'),
        db_column='TotalPrice',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4,
        default=0
    )

    objects = OrderDetailsManager()


    def clean(self):
        super().clean()
        if not self.product_id_id:
            raise ValidationError('Product is required.')

        try:
            self.product_id.__class__.objects.get(pk=self.product_id_id)
        except self.product_id.__class__.DoesNotExist:
            raise ValidationError('Invalid product.')

        if self.quantity == 0:
            raise ValidationError('Quantity must be greater than zero.')

        # Check if it's a new instance or an existing one being updated
        if self.pk:
            current_order_details = OrderDetails.objects.get(pk=self.pk)
            current_quantity = current_order_details.quantity
            quantity_difference = self.quantity - current_quantity
        else:
            current_quantity = 0
            quantity_difference = self.quantity

        # Check if there are enough units_in_stock to fulfill the new quantity
        if quantity_difference > self.product_id.units_in_stock:
            raise ValidationError(f"Only {self.product_id.units_in_stock} more units available in stock.")


    def save(self, *args, **kwargs):
        # create new order if order_id is not set
        if not self.order_id:
            order = Order.objects.create()
            self.order_id = order
            order.save()
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'order_details'
        verbose_name_plural = _('Order details')
        ordering = ['-order_id']

    def __str__(self):
        return f'{str(self.order_id)} for {str(self.product_id)}'



