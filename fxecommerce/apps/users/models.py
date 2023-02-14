from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import utils as const
from .managers import CustomUserManager, EmployeeManager
from django.template.defaultfilters import slugify
import uuid
from django.urls import reverse


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    user_type = models.PositiveSmallIntegerField(choices=const.USER_TYPE, default=1)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="employee")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_profile', default='user_profile/employee/example_photo.png')

    last_name = models.CharField(
        verbose_name=_('Last name'),
        db_column='LastName',
        max_length=20,
        blank=False,
        null=False,
        db_index=True
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        db_column='FirstName',
        max_length=10,
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_('title'),
        db_column='Title',
        max_length=30,
        blank=False,
        null=False
    )
    title_of_courtesy = models.CharField(
        verbose_name=_('Title of Courtesy'),
        db_column='TitleOfCourtesy',
        max_length=25,
        blank=True,
        null=False
    )
    birth_date = models.DateField(
        verbose_name=_('Birth date'),
        db_column='BirthDate',
        blank=True,
        null=True
    )
    hire_date = models.DateField(
        verbose_name=_('Hire date'),
        db_column='HireDate',
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_('address'),
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
        null=False,
        db_index=True
    )
    country = models.CharField(
        verbose_name=_('Country'),
        db_column='Country',
        max_length=15,
        blank=False,
        null=False
    )
    home_phone = models.CharField(
        verbose_name=_('Home phone'),
        db_column='HomePhone',
        max_length=24,
        blank=False,
        null=False
    )
    extension = models.CharField(
        verbose_name=_('Extension'),
        db_column='Extension',
        max_length=4,
        blank=False,
        null=False
    )
    photo = models.ImageField(
        verbose_name=_('Photo'),
        db_column='Photo',
        blank=True,
        upload_to='employee/'
    )
    notes = models.TextField(
        verbose_name=_('Notes'),
        db_column='Notes',
        blank=True,
        null=False
    )
    reports_to = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        db_column='ReportsTo',
        on_delete=models.PROTECT,
    )
    photo_path = models.CharField(
        verbose_name=_('Photo path'),
        db_column='PhotoPath',
        max_length=255,
        blank=True,
        null=False
    )
    territories = models.ManyToManyField(
        'inventory.Territory',
        verbose_name=_('Territories'),
        through='inventory.EmployeeTerritory',
        blank=True,
    )

    slug = models.SlugField(
        null=True,
        unique=True
    )

    objects = EmployeeManager()

    def get_absolute_url(self):
        return reverse('users:employee_detail', kwargs={'slug': self.slug})

    def clean(self):
        if Customer.objects.filter(user__email=self.user.email).exists() or Employee.objects.filter(user__email=self.user.email).exists():
            raise ValidationError("The email is already in use")

    def save(self, *args, **kwargs):
        generate_uuid = uuid.uuid4()
        slug_uuid = generate_uuid.hex
        self.slug = slugify(slug_uuid)
        super(Employee, self).save(*args, **kwargs)


    class Meta:
        db_table = 'employee'
        verbose_name_plural = _('Employees')
        ordering = ['first_name']


    def __str__(self):
        return self.user.email


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name="customer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_profile', default='user_profile/customer/example_photo.png')


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
    customer_customer_demo = models.ManyToManyField(
        "inventory.CustomerDemographics",
        verbose_name=_('CustomerCustomerDemos'),
        through='inventory.CustomerCustomerDemo',
        blank=True
    )

    def clean(self):
        if Customer.objects.filter(user__email=self.user.email).exists() or Employee.objects.filter(user__email=self.user.email).exists():
            raise ValidationError("The email is already in use")


    class Meta:
        db_table = 'customer'
        verbose_name_plural = _("Customers")


    def __str__(self):
        return self.user.email

