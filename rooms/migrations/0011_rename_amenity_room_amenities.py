# Generated by Django 4.2.1 on 2023-05-24 07:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0010_alter_room_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="amenity",
            new_name="amenities",
        ),
    ]