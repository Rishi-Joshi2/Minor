# Generated by Django 3.0.8 on 2021-05-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productpic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]