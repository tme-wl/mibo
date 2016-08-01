from django.db import models


class tags(models.Model):
    '''电影标签表'''
    name = models.CharField('电影标签',max_length=50,default='')
    value = models.IntegerField("标签值",default=0)
    count = models.IntegerField("数量",default=0)


class video(models.Model):
    '''电影信息表'''
    name = models.CharField('电影名称',max_length=50,default='')
    longtime=models.IntegerField('电影时长',default=0,null=True)
    contry=models.CharField('国家',max_length=100,default='',null=True)
    director=models.CharField('导演',max_length=100,default='',null=True)
    actor=models.CharField('演员',max_length=200,default='',null=True)
    prize=models.CharField('得奖',max_length=200,default='',null=True)
    time=models.IntegerField('播放次数',default=0,null=True)
    videourl=models.CharField('电影链接',max_length=500)
    paperurl=models.CharField('海报链接',max_length=500)
    tags=models.ManyToManyField(tags)

class userinfo(models.Model):
    '''用户信息表'''
    name=models.CharField('用户名',max_length=50,default='')
    sumfilm=models.IntegerField('看过电影数',default=0)
    filmid=models.CharField('看过的电影ID',max_length=500,default='',null=True)