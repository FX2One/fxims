# https://simpleisbetterthancomplex.com/tips/2016/10/17/django-tip-18-translations.html
# usage of ugettext_lazy
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(
        _('Category ID'),
        db_column='CategoryID',
        primary_key=True
    )
    category_name = models.CharField(
        _('Category name'),
        db_column='CategoryName',
        max_length=15,
        db_index=True
    )
    description = models.TextField(
        _('Description'),
        db_column='Description',
        blank=True,
        null=True
    )
    image = models.ImageField(
        _('Image'),
        db_column='Image',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'categories'