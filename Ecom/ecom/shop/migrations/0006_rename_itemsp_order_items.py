# Generated by Django 3.2.4 on 2021-07-11 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_items_order_itemsp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='itemsp',
            new_name='items',
        ),
    ]
