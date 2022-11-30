from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from . import utils as const
from .managers import CustomUserManager




class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    user_type = models.PositiveSmallIntegerField(choices=const.USER_TYPE, default=4)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="profile")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_profile', default='user_profile/default_photo.png')

    company_name = models.CharField(
        verbose_name=_('Company name'),
        db_column='CompanyName',
        max_length=40,
        blank=False,
        null=False,
        default=""
    )
    contact_name = models.CharField(
        verbose_name=_('Contact name'),
        db_column='ContactName',
        max_length=30,
        blank=False,
        null=False,
        default=""
    )
    contact_title = models.CharField(
        verbose_name=_('Contact title'),
        db_column='ContactTitle',
        max_length=30,
        blank=False,
        null=False,
        default=""
    )
    address = models.CharField(
        verbose_name=_('Address'),
        db_column='Address',
        max_length=60,
        blank=False,
        null=False,
        default=""
    )
    city = models.CharField(
        verbose_name=_('City'),
        db_column='City',
        max_length=15,
        blank=False,
        null=False,
        default=""
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
        null=False,
        default=""
    )
    country = models.CharField(
        verbose_name=_('Country'),
        db_column='Country',
        max_length=15,
        blank=False,
        null=False,
        default=""
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        db_column='Phone',
        max_length=24,
        blank=False,
        null=False,
        default=""
    )
    fax = models.CharField(
        verbose_name=_('Fax'),
        db_column='Fax',
        max_length=24,
        blank=True,
        null=True
    )
    customer_customer_demo = models.ManyToManyField(
        "inventory.CustomerDemographics",
        verbose_name=_('CustomerCustomerDemos'),
        through='inventory.CustomerCustomerDemo',
        blank=True,
    )

    class Meta:
        db_table = 'customer'
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.user.email
