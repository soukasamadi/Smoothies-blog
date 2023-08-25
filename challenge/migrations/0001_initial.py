# Generated by Django 3.2.20 on 2023-08-25 22:03

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('goal', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField(blank=True)),
                ('review', models.TextField(max_length=200)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
