# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(height_field=400, upload_to='/news_images', width_field=240),
        ),
    ]