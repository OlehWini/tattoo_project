# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20161019_1646'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_article',
        ),
        migrations.DeleteModel(
            name='Master',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
