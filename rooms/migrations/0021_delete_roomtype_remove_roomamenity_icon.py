# Generated by Django 4.2.2 on 2023-06-28 07:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0002_delete_roomtypethumbnail"),
        ("rooms", "0020_alter_room_room_type"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RoomType",
        ),
        migrations.RemoveField(
            model_name="roomamenity",
            name="icon",
        ),
    ]
