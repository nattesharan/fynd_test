# Generated by Django 2.2 on 2020-08-16 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_99_popularity', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0, message='The value should be in between 0 to 100'), django.core.validators.MaxValueValidator(100, message='The value should be in between 0 to 100')])),
                ('director', models.CharField(max_length=512)),
                ('imdb_score', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0, message='The value should be in between 0 to 10'), django.core.validators.MaxValueValidator(10, message='The value should be in between 0 to 10')])),
                ('name', models.CharField(max_length=512)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('genre', models.ManyToManyField(to='api.Genre')),
            ],
        ),
    ]
