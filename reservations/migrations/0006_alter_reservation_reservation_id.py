# Generated by Django 4.2.1 on 2023-06-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0005_alter_reservation_reservation_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="reservation_id",
            field=models.SlugField(
                default="20230618291DDF",
                editable=False,
                max_length=20,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]