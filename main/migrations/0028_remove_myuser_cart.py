# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20161023_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='cart',
        ),
    ]
