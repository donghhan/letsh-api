# Generated by Django 4.2.2 on 2023-07-06 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0025_alter_roomtype_room_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="bathroom",
            field=models.PositiveSmallIntegerField(default=1, verbose_name="Bathroom"),
        ),
        migrations.AlterField(
            model_name="room",
            name="bedroom",
            field=models.PositiveSmallIntegerField(default=1, verbose_name="Bedroom"),
        ),
        migrations.AlterField(
            model_name="room",
            name="guest",
            field=models.PositiveSmallIntegerField(
                help_text="Guest should include at least one person, and not exceed more than 100 people.",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="Guest",
            ),
        ),
    ]
