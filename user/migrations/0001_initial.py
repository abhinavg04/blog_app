# Generated by Django 5.0.1 on 2024-01-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]