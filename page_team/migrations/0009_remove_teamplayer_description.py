# Generated by Django 5.0.6 on 2024-07-17 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_team', '0008_teamplayer_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayer',
            name='description',
        ),
    ]
