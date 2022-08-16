# https://simpleisbetterthancomplex.com/tips/2016/10/17/django-tip-18-translations.html
# usage of ugettext_lazy
from django.utils.translation import gettext_lazy as _
from django.db import models


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
        db_index=True,
        blank=False,
        help_text=_("format: required. Max_length: 100")
    )
    description = models.TextField(
        verbose_name=_('Description'),
        db_column='Description',
        max_length=150,
        blank=False,
        help_text=_("format: required. Max_length: 150")
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        db_column='Image',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'category'
        verbose_name_plural = _("Product categories")

    def __str__(self):
        return self.category_name


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
    description = models.TextField(
        verbose_name=_('Description'),
        db_column='Description',
        null=False,
        blank=False,
        max_length=255,
        help_text=_('format: required, max_length: 255')
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
        blank=True,
        null=False
    )
    unit_price = models.DecimalField(
        verbose_name=_('Unit price'),
        db_column='UnitPrice',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4
    )
    units_in_stock = models.SmallIntegerField(
        verbose_name=_('Units in Stock'),
        db_column='UnitsInStock',
        blank=True,
        null=True
    )
    units_on_order = models.SmallIntegerField(
        verbose_name=_('Units on Order'),
        db_column='UnitsOnOrder',
        blank=True,
        null=True
    )
    reorder_level = models.SmallIntegerField(
        verbose_name=_('Reorder level'),
        db_column='ReorderLevel',
        blank=True,
        null=True
    )
    discontinued = models.IntegerField(
        _('Discontinued'),
        db_column='Discontinued'
    )

    class Meta:
        db_table = 'product'
        verbose_name_plural = _("Products")


class Supplier(models.Model):
    pass

    class Meta:
        db_table = 'supplier'
        verbose_name_plural = _("Suppliers")