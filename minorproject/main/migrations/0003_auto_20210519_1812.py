# Generated by Django 3.0.8 on 2021-05-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_productpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='NULL', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='keyingr',
            field=models.TextField(default='NULL', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufracturer',
            field=models.CharField(default='NULL', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='productdescription',
            field=models.TextField(default='NULL', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='safetyinfo',
            field=models.TextField(default='NULL', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meduses',
            field=models.TextField(default='NULL', max_length=80, null=True),
        ),
    ]
