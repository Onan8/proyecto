# Generated by Django 5.0.7 on 2024-08-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradeMark', models.CharField(max_length=50)),
                ('vehicleModel', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('numberDoors', models.IntegerField()),
                ('parking', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
                ('vehicleType', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='vehicles/')),
            ],
        ),
    ]
