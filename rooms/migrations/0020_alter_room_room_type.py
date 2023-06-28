# Generated by Django 4.2.2 on 2023-06-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0019_alter_room_room_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.CharField(
                choices=[
                    ("Hotel", "Hotel"),
                    ("Apartment", "Apartment"),
                    ("Condominium", "Condominium"),
                    ("Villa", "Villa"),
                    ("Resort", "Resort"),
                    ("Castle", "Castle"),
                    ("Beach House", "Beach House"),
                    ("Luxe", "Luxe"),
                    ("Cabin", "Cabin"),
                    ("Cheateau", "Chateau"),
                    ("Mansion", "Mansion"),
                    ("Farm", "Farm"),
                ],
                default="Hotel",
                max_length=255,
                verbose_name="Room Type",
            ),
        ),
    ]
