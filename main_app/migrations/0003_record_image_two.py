# Generated by Django 3.1.3 on 2022-06-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_tracklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image_two',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]