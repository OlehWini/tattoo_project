# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20161020_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_product', models.CharField(max_length=100)),
                ('sale', models.BooleanField()),
                ('price', models.FloatField()),
                ('is_in_stock', models.BooleanField()),
                ('photo', models.FileField(null=True, upload_to=b'', blank=True)),
                ('category', models.ForeignKey(to='main.Category')),
            ],
        ),
    ]
