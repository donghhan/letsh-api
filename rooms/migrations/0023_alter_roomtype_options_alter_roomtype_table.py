# Generated by Django 4.2.2 on 2023-06-28 08:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0022_roomtype_alter_room_room_type"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="roomtype",
            options={"verbose_name": "Room Type", "verbose_name_plural": "Room Types"},
        ),
        migrations.AlterModelTable(
            name="roomtype",
            table="room_types",
        ),
    ]
