# Generated by Django 5.0.2 on 2024-12-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatics', '0002_alter_documentcontent_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='courses',
            field=models.ManyToManyField(blank=True, to='informatics.course'),
        ),
    ]
