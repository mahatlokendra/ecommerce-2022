# Generated by Django 2.2.12 on 2022-02-15 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
