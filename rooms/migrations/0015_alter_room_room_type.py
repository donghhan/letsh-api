# Generated by Django 4.2.1 on 2023-06-18 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0014_alter_room_room_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="rooms.roomtype",
                to_field="name",
                verbose_name="Room Type",
            ),
        ),
    ]
