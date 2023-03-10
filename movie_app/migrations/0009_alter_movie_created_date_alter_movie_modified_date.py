# Generated by Django 4.1.4 on 2023-01-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения'),
        ),
    ]
