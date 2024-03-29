# Generated by Django 4.2.2 on 2023-06-26 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0003_alter_category_name"),
        ("rooms", "0017_alter_roomtype_cover_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="rooms",
                to="categories.category",
                verbose_name="Category",
            ),
        ),
    ]
