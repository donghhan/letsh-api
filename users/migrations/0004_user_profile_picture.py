# Generated by Django 4.2.1 on 2023-05-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.URLField(
                blank=True, null=True, verbose_name="Profile picture"
            ),
        ),
    ]
