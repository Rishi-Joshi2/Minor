# Generated by Django 3.0.5 on 2021-05-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210527_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the Way', 'On the Way'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Order Placed', 'Order Placed')], default='Order Placed', max_length=50),
        ),
    ]