# Generated by Django 2.2.6 on 2020-02-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
