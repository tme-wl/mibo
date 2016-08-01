# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20160613_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='paperurl',
            field=models.CharField(max_length=500, default=datetime.datetime(2016, 7, 6, 4, 23, 8, 797902, tzinfo=utc), verbose_name='海报链接'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='videourl',
            field=models.CharField(max_length=500, default='', verbose_name='电影链接'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Manu',
        ),
    ]
