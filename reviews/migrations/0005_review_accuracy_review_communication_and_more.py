# Generated by Django 4.0.7 on 2022-10-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_room_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='accuracy',
            field=models.CharField(choices=[(1, 'Awful'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Excellent')], default=3, max_length=10),
        ),
        migrations.AddField(
            model_name='review',
            name='communication',
            field=models.CharField(choices=[(1, 'Awful'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Excellent')], default=3, max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='cleanliness',
            field=models.CharField(choices=[(1, 'Awful'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Excellent')], default=3, max_length=10),
        ),
    ]
