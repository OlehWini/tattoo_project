# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_text', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('pubDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dataPublished')),
            ],
        ),
    ]