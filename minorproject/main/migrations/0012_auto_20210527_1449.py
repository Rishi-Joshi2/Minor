# Generated by Django 3.0.5 on 2021-05-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210527_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
