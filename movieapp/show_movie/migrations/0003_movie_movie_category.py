# Generated by Django 4.1.4 on 2023-01-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_movie', '0002_alter_movie_movie_issu_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
