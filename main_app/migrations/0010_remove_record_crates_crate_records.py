# Generated by Django 4.0.5 on 2022-06-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_crate_alter_artist_id_alter_record_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='crates',
        ),
        migrations.AddField(
            model_name='crate',
            name='records',
            field=models.ManyToManyField(to='main_app.record'),
        ),
    ]
