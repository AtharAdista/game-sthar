# Generated by Django 4.2.5 on 2023-10-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_amount_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='platform',
            field=models.TextField(max_length=255),
        ),
    ]
