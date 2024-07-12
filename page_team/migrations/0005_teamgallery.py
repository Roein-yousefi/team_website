# Generated by Django 5.0.6 on 2024-07-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_team', '0004_teamshop_alter_teamnews_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='newas/')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]