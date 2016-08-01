# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20160613_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='video',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='all_film',
        ),
        migrations.RemoveField(
            model_name='video',
            name='classfiy',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='filmid',
            field=models.CharField(verbose_name='看过的电影ID', null=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='video.tags'),
        ),
    ]
