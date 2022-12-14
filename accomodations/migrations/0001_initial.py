# Generated by Django 4.0.7 on 2022-10-27 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(blank=True, help_text='Short description of room option.', max_length=200, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Amenity',
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Accomodation Name')),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price Per Night')),
                ('maximum_guests', models.PositiveSmallIntegerField(default=1, verbose_name='Maximum Number of Guests')),
                ('number_of_beds', models.PositiveSmallIntegerField(default=1, verbose_name='Number of beds')),
                ('number_of_bedrooms', models.PositiveSmallIntegerField(default=1, verbose_name='Number of Bedrooms')),
                ('number_of_bathrooms', models.PositiveSmallIntegerField(default=1, verbose_name='Numeber of Bathrooms')),
                ('is_free_breakfast', models.BooleanField(default=False, verbose_name='Free Breakfast')),
                ('is_free_internet', models.BooleanField(default=False, verbose_name='Free Internet')),
                ('is_free_parking', models.BooleanField(default=False, verbose_name='Free Parking')),
                ('amenities', models.ManyToManyField(to='accomodations.amenity')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'db_table': 'rooms',
            },
        ),
    ]
