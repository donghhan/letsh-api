# Generated by Django 4.0.7 on 2022-11-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_rooms_alter_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='rooms',
            new_name='room',
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(verbose_name='Checking in'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(verbose_name='Checking out'),
        ),
    ]
