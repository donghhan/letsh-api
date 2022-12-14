# Generated by Django 4.0.7 on 2022-11-13 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_name'),
        ('accomodations', '0008_alter_room_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category'),
            preserve_default=False,
        ),
    ]
