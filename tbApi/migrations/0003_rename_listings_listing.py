# Generated by Django 4.2.1 on 2023-05-22 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbApi', '0002_rename_listing_listings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]
