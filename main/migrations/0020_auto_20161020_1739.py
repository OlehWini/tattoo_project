# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20161020_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
