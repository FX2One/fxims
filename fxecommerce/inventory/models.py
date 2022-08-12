# https://simpleisbetterthancomplex.com/tips/2016/10/17/django-tip-18-translations.html
# usage of ugettext_lazy
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class Category(models.Model):
    id = models.AutoField(
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
        helptext=_("format: required,max-100")
    )
    description = models.TextField(
        verbose_name=_('Description'),
        db_column='Description',
        max_length=150,
        blank=False,
        null=False,
        helptext=_("format: required,max-150")
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        db_column='Image',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_name
