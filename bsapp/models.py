# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    name = models.CharField(max_length = 30)
    psw = models.CharField(max_length = 16)
    age = models.IntegerField(blank = True, null=True)
    qq = models.IntegerField(blank = True, null=True)
    phone = models.IntegerField(blank = True, null=True)
    email = models.EmailField(blank = True, null=True)
    gender = models.CharField(max_length = 10, blank = True, null=True)

    def __unicode__(self):
        return self.name


class Contents(models.Model):
    content = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now = True)
    users = models.ForeignKey(Users)

    def __unicode__(self):
        return self.content


class Files(models.Model):
    name = models.CharField(max_length = 30, null = True)
    files = models.FileField(u'文件', upload_to = './files')
    users = models.ForeignKey(Users)

    def __unicode__(self):
        return self.name




