# Generated by Django 4.1.4 on 2022-12-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
