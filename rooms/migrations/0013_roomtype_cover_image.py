# Generated by Django 4.2.1 on 2023-06-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0012_roomtype_alter_room_room_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="roomtype",
            name="cover_image",
            field=models.URLField(
                blank=True,
                help_text="Cover image that will be used for image carousel in the home page.",
                null=True,
                verbose_name="Cover Image",
            ),
        ),
    ]
