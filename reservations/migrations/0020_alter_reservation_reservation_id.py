# Generated by Django 4.2.2 on 2023-06-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0019_alter_reservation_reservation_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="reservation_id",
            field=models.SlugField(
                editable=False,
                max_length=20,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
