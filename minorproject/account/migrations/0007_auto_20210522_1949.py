# Generated by Django 3.0.5 on 2021-05-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210522_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address1',
            field=models.TextField(default='Please provide your address', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address2',
            field=models.TextField(blank=True, default='Please provide your address', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode1',
            field=models.CharField(default='Please provide your pincode', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode2',
            field=models.CharField(blank=True, default='Please provide your pincode', max_length=15, null=True),
        ),
    ]