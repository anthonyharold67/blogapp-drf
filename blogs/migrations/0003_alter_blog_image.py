# Generated by Django 4.0.6 on 2022-11-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]
