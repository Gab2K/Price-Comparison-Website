# Generated by Django 3.2.10 on 2022-03-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
