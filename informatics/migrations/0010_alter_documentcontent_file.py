# Generated by Django 5.0.2 on 2025-03-04 15:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informatics', '0009_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcontent',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='file'),
        ),
    ]
