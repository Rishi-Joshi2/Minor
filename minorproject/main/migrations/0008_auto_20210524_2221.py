# Generated by Django 3.0.5 on 2021-05-24 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cust_id',
            new_name='cus_id',
        ),
    ]
