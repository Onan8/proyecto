# Generated by Django 5.1 on 2024-08-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('age', models.IntegerField()),
                ('number_employee', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('number_id', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('schedule', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
