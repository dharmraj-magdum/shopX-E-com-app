# Generated by Django 4.2 on 2023-06-01 18:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
