# Generated by Django 4.0.7 on 2022-11-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(error_messages={'null': 'You should provide your first name.'}, max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(error_messages={'null': 'You should provide your last name.'}, max_length=100, verbose_name='Last Name'),
        ),
    ]
