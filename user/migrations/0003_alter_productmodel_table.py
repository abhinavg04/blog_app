# Generated by Django 5.0.1 on 2024-01-31 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_productmodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productmodel',
            table='Product',
        ),
    ]