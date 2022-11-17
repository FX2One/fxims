# Generated by Django 3.2.8 on 2022-11-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(db_column='CategoryID', primary_key=True, serialize=False, verbose_name='Category ID')),
                ('category_name', models.CharField(db_column='CategoryName', db_index=True, help_text='format: required. Max_length: 100', max_length=100, verbose_name='Category name')),
                ('description', models.TextField(db_column='Description', help_text='format: required. Max_length: 150', max_length=150, verbose_name='Description')),
                ('image', models.ImageField(blank=True, db_column='Image', upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(db_column='CustomerID', max_length=5, primary_key=True, serialize=False, verbose_name='Customer ID')),
                ('company_name', models.CharField(db_column='CompanyName', max_length=40, verbose_name='Company name')),
                ('contact_name', models.CharField(db_column='ContactName', max_length=30, verbose_name='Contact name')),
                ('contact_title', models.CharField(db_column='ContactTitle', max_length=30, verbose_name='Contact title')),
                ('address', models.CharField(db_column='Address', max_length=60, verbose_name='Address')),
                ('city', models.CharField(db_column='City', max_length=15, verbose_name='City')),
                ('region', models.CharField(blank=True, db_column='Region', max_length=15, null=True, verbose_name='Region')),
                ('postal_code', models.CharField(db_column='PostalCode', max_length=10, verbose_name='Postal code')),
                ('country', models.CharField(db_column='Country', max_length=15, verbose_name='Country')),
                ('phone', models.CharField(db_column='Phone', max_length=24, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=24, null=True, verbose_name='Fax')),
            ],
            options={
                'verbose_name_plural': 'Customers',
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerDemographics',
            fields=[
                ('customer_type_id', models.CharField(db_column='CustomerTypeID', max_length=5, primary_key=True, serialize=False, verbose_name='Customer Type_ID')),
                ('customer_desc', models.TextField(db_column='CustomerDesc', null=True, verbose_name='Customer description')),
            ],
            options={
                'db_table': 'customerdemographics',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(db_column='EmployeeID', primary_key=True, serialize=False, verbose_name='Employee id')),
                ('last_name', models.CharField(db_column='LastName', db_index=True, max_length=20, verbose_name='Last name')),
                ('first_name', models.CharField(db_column='FirstName', max_length=10, verbose_name='First name')),
                ('title', models.CharField(db_column='Title', max_length=30, verbose_name='title')),
                ('title_of_courtesy', models.CharField(blank=True, db_column='TitleOfCourtesy', max_length=25, verbose_name='Title of Courtesy')),
                ('birth_date', models.DateField(blank=True, db_column='BirthDate', null=True, verbose_name='Birth date')),
                ('hire_date', models.DateField(blank=True, db_column='HireDate', null=True, verbose_name='Hire date')),
                ('address', models.CharField(db_column='Address', max_length=60, verbose_name='address')),
                ('city', models.CharField(db_column='City', max_length=15, verbose_name='City')),
                ('region', models.CharField(blank=True, db_column='Region', max_length=15, null=True, verbose_name='Region')),
                ('postal_code', models.CharField(db_column='PostalCode', db_index=True, max_length=10, verbose_name='Postal code')),
                ('country', models.CharField(db_column='Country', max_length=15, verbose_name='Country')),
                ('home_phone', models.CharField(db_column='HomePhone', max_length=24, verbose_name='Home phone')),
                ('extension', models.CharField(db_column='Extension', max_length=4, verbose_name='Extension')),
                ('photo', models.ImageField(blank=True, db_column='Photo', upload_to='', verbose_name='Photo')),
                ('notes', models.TextField(blank=True, db_column='Notes', verbose_name='Notes')),
                ('photo_path', models.CharField(blank=True, db_column='PhotoPath', max_length=255, verbose_name='Photo path')),
                ('slug', models.SlugField(unique=True)),
                ('reports_to', models.ForeignKey(blank=True, db_column='ReportsTo', null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.employee')),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(db_column='OrderID', primary_key=True, serialize=False, verbose_name='Order ID')),
                ('order_date', models.DateField(blank=True, db_column='OrderDate', db_index=True, null=True, verbose_name='Order date')),
                ('required_date', models.DateField(blank=True, db_column='RequiredDate', null=True, verbose_name='Required_date')),
                ('shipped_date', models.DateField(blank=True, db_column='ShippedDate', db_index=True, null=True, verbose_name='Shipped date')),
                ('freight', models.DecimalField(blank=True, db_column='Freight', decimal_places=4, max_digits=19, null=True, verbose_name='Freight')),
                ('ship_name', models.CharField(db_column='ShipName', max_length=40, verbose_name='Ship name')),
                ('ship_address', models.CharField(db_column='ShipAddress', max_length=60, verbose_name='Ship address')),
                ('ship_city', models.CharField(db_column='ShipCity', max_length=15, verbose_name='Ship city')),
                ('ship_region', models.CharField(blank=True, db_column='ShipRegion', max_length=15, null=True, verbose_name='Ship region')),
                ('ship_postal_code', models.CharField(db_column='ShipPostalCode', db_index=True, max_length=10, verbose_name='Ship postal code')),
                ('ship_country', models.CharField(db_column='ShipCountry', max_length=15, verbose_name='Shipped country')),
                ('customer_id', models.ForeignKey(blank=True, db_column='CustomerID', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
                ('employee_id', models.ForeignKey(blank=True, db_column='EmployeeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.employee')),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.PositiveSmallIntegerField(db_column='RegionID', primary_key=True, serialize=False, verbose_name='Region id')),
                ('region_description', models.CharField(db_column='RegionDescription', max_length=50, verbose_name='Region description')),
            ],
            options={
                'verbose_name_plural': 'Regions',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('shipper_id', models.AutoField(db_column='ShipperID', primary_key=True, serialize=False, verbose_name='Shipper ID')),
                ('company_name', models.CharField(db_column='CompanyName', max_length=40, verbose_name='Company name')),
                ('phone', models.CharField(db_column='Phone', max_length=24, verbose_name='Phone')),
            ],
            options={
                'verbose_name_plural': 'Shippers',
                'db_table': 'shipper',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(db_column='SupplierID', primary_key=True, serialize=False, verbose_name='Supplier ID')),
                ('company_name', models.CharField(db_column='CompanyName', max_length=40, verbose_name='Company name')),
                ('contact_name', models.CharField(db_column='ContactName', max_length=30, verbose_name='Contact name')),
                ('contact_title', models.CharField(db_column='ContactTitle', max_length=30, verbose_name='Contact title')),
                ('address', models.CharField(db_column='Address', max_length=60, verbose_name='Address')),
                ('city', models.CharField(db_column='City', max_length=15, verbose_name='City')),
                ('region', models.CharField(blank=True, db_column='Region', max_length=15, null=True, verbose_name='Region')),
                ('postal_code', models.CharField(db_column='PostalCode', max_length=10, verbose_name='Postal code')),
                ('country', models.CharField(db_column='Country', max_length=15, verbose_name='Country')),
                ('phone', models.CharField(db_column='Phone', max_length=24, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=24, null=True, verbose_name='Fax')),
                ('homepage', models.TextField(blank=True, db_column='HomePage', null=True, verbose_name='HomePage')),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('territory_id', models.CharField(db_column='TerritoryID', max_length=20, primary_key=True, serialize=False, verbose_name='Territory id')),
                ('territory_description', models.CharField(db_column='TerritoryDescription', max_length=50, verbose_name='Territory description')),
                ('region_id', models.ForeignKey(db_column='RegionID', on_delete=django.db.models.deletion.CASCADE, to='inventory.region')),
            ],
            options={
                'verbose_name_plural': 'Territories',
                'db_table': 'territory',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(db_column='ProductID', primary_key=True, serialize=False, verbose_name='Product ID')),
                ('product_name', models.CharField(db_column='ProductName', db_index=True, help_text='format: required. max_length: 100', max_length=100, verbose_name='Product name')),
                ('quantity_per_unit', models.CharField(db_column='QuantityPerUnit', max_length=20, verbose_name='Quantity per Unit')),
                ('unit_price', models.DecimalField(blank=True, db_column='UnitPrice', decimal_places=4, max_digits=19, null=True, verbose_name='Unit price')),
                ('units_in_stock', models.SmallIntegerField(blank=True, db_column='UnitsInStock', null=True, verbose_name='Units in Stock')),
                ('units_on_order', models.SmallIntegerField(blank=True, db_column='UnitsOnOrder', null=True, verbose_name='Units on Order')),
                ('reorder_level', models.SmallIntegerField(blank=True, db_column='ReorderLevel', null=True, verbose_name='Reorder level')),
                ('discontinued', models.BooleanField(db_column='Discontinued', verbose_name='Discontinued')),
                ('slug', models.SlugField(unique=True)),
                ('category_id', models.ForeignKey(blank=True, db_column='CategoryID', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
                ('supplier_id', models.ForeignKey(blank=True, db_column='SupplierID', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(db_column='UnitPrice', decimal_places=4, max_digits=19, verbose_name='Unit price')),
                ('quantity', models.SmallIntegerField(db_column='Quantity', verbose_name='Quantity')),
                ('discount', models.FloatField(db_column='Discount', verbose_name='Discount')),
                ('order_id', models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.CASCADE, to='inventory.order')),
                ('product_id', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
            options={
                'verbose_name_plural': 'Order details',
                'db_table': 'order_details',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_details',
            field=models.ManyToManyField(blank=True, through='inventory.OrderDetails', to='inventory.Product', verbose_name='Products'),
        ),
        migrations.AddField(
            model_name='order',
            name='ship_via',
            field=models.ForeignKey(blank=True, db_column='ShipVia', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.shipper'),
        ),
        migrations.CreateModel(
            name='EmployeeTerritory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(db_column='EmployeeID', on_delete=django.db.models.deletion.CASCADE, to='inventory.employee')),
                ('territory_id', models.ForeignKey(db_column='TerritoryID', on_delete=django.db.models.deletion.CASCADE, to='inventory.territory')),
            ],
            options={
                'verbose_name_plural': 'Employee territories',
                'db_table': 'employee_territories',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='territories',
            field=models.ManyToManyField(blank=True, through='inventory.EmployeeTerritory', to='inventory.Territory', verbose_name='Territories'),
        ),
        migrations.CreateModel(
            name='CustomerCustomerDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
                ('customer_type_id', models.ForeignKey(db_column='CustomerTypeID', on_delete=django.db.models.deletion.CASCADE, to='inventory.customerdemographics')),
            ],
            options={
                'verbose_name_plural': 'CustomerCustomerDemos',
                'db_table': 'customer_customer_demo',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_customer_demo',
            field=models.ManyToManyField(blank=True, through='inventory.CustomerCustomerDemo', to='inventory.CustomerDemographics', verbose_name='CustomerCustomerDemos'),
        ),
    ]
