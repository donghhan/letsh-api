# Generated by Django 4.2.2 on 2023-06-26 05:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0002_alter_review_check_in_alter_review_communication_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "Review", "verbose_name_plural": "Reviews"},
        ),
        migrations.AlterModelTable(
            name="review",
            table="reviews",
        ),
    ]