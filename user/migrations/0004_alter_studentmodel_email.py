# Generated by Django 5.0.1 on 2024-02-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_productmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]