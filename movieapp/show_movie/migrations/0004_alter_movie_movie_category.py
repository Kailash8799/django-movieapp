# Generated by Django 4.1.4 on 2023-01-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_movie', '0003_movie_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_category',
            field=models.CharField(max_length=50),
        ),
    ]