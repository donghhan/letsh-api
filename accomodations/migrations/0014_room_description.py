# Generated by Django 4.0.7 on 2022-12-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodations', '0013_alter_room_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Room Description'),
        ),
    ]
