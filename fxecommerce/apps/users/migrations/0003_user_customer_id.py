# Generated by Django 3.2.8 on 2022-11-29 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_customer_customer_id'),
        ('users', '0002_remove_user_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customer_id',
            field=models.ForeignKey(blank=True, db_column='CustomerID', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.customer'),
        ),
    ]