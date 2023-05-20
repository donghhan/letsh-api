# Generated by Django 4.2.1 on 2023-05-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_roomamenity_icon_roomamenity_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="amenity",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="rooms",
                to="rooms.roomamenity",
                verbose_name="Amenities",
            ),
        ),
    ]