# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20161020_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header_text', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('pubDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dataPublished')),
                ('photo', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text_of_comment', models.TextField()),
                ('comments_pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sur_name', models.CharField(max_length=100)),
                ('years_old', models.IntegerField()),
                ('about', models.TextField()),
                ('his_photo', models.FileField(null=True, upload_to=b'', blank=True)),
                ('experience', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('link_on_works', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_header_text', models.CharField(max_length=100)),
                ('topic_count_of_records', models.IntegerField(default=0)),
                ('topic_pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='topic',
            field=models.ForeignKey(to='main.Topic'),
        ),
    ]
