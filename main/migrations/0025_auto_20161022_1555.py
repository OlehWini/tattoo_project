# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mashines',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Product')),
                ('motor', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('frame', models.CharField(max_length=100)),
                ('where_made', models.CharField(max_length=100)),
            ],
            bases=('main.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.TextField(default=datetime.datetime(2016, 10, 22, 15, 55, 16, 539994, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
