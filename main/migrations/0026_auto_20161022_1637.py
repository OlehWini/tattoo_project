# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20161022_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mashines',
            name='product_ptr',
        ),
        migrations.DeleteModel(
            name='Mashines',
        ),
    ]
