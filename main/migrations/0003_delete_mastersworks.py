# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_author_master_mastersworks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MastersWorks',
        ),
    ]
