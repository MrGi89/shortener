# Generated by Django 2.2 on 2020-07-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='slug',
            field=models.SlugField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='url',
            field=models.URLField(max_length=500, unique=True),
        ),
    ]
