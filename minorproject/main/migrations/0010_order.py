# Generated by Django 3.0.5 on 2021-05-27 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20210525_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address_ordered', models.TextField(max_length=150)),
                ('pincode_ordered', models.CharField(max_length=15)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the Way', 'On the Way'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=50)),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
