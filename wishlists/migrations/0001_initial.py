# Generated by Django 4.2.2 on 2023-06-30 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("rooms", "0024_alter_room_room_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_date",
                    models.DateField(auto_now_add=True, verbose_name="Created Date"),
                ),
                (
                    "updated_date",
                    models.DateField(auto_now=True, verbose_name="Updated Date"),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Wishlist name"),
                ),
                (
                    "room",
                    models.ManyToManyField(related_name="wishlists", to="rooms.room"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlists",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Wishlist",
                "verbose_name_plural": "Wishlists",
                "db_table": "wishlists",
            },
        ),
    ]
