# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(default='', verbose_name='电影标签', max_length=50)),
                ('value', models.IntegerField(verbose_name='标签值', default=0)),
                ('count', models.IntegerField(verbose_name='数量', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(default='', verbose_name='用户名', max_length=50)),
                ('sumfilm', models.IntegerField(verbose_name='看过电影数', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(default='', verbose_name='电影名称', max_length=50)),
                ('longtime', models.IntegerField(verbose_name='电影时长', default=0, null=True)),
                ('contry', models.CharField(default='', verbose_name='国家', max_length=100, null=True)),
                ('director', models.CharField(default='', verbose_name='导演', max_length=100, null=True)),
                ('actor', models.CharField(default='', verbose_name='演员', max_length=200, null=True)),
                ('prize', models.CharField(default='', verbose_name='得奖', max_length=200, null=True)),
                ('classfiy', models.IntegerField(verbose_name='分类', default=0)),
                ('time', models.IntegerField(verbose_name='播放次数', default=0, null=True)),
                ('url', models.CharField(verbose_name='链接', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='all_film',
            field=models.ManyToManyField(to='video.video'),
        ),
        migrations.AddField(
            model_name='tags',
            name='video',
            field=models.ManyToManyField(to='video.video'),
        ),
    ]
