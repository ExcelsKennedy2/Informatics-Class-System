# Generated by Django 5.0.2 on 2024-12-30 16:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informatics', '0007_alter_event_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textcontent',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
