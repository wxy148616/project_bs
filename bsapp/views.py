# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.conf import settings
import json, re


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        name = str(request.POST.get('name'))
        psw = str(request.POST.get('psw'))
        if name == 'yangjunxia' and psw == "iloveyou":
            return render(request, 'home.html', context = dict(
                msg = "wxy",
                data = "I Love You!"
                ))
        if psw and name:
            if Pone.objects.filter(name=name):
                if Pone.objects.filter(psw = psw):
                    return render(request, 'home.html', context = dict(
                        name = name,
                        msg = True
                        ))
        return render(request, 'login.html', context = dict(
            data = "用户名或密码错误^_^",
            msg = True
            ))


def regist(request):
    if request.method == "GET":
        return render(request, "regist.html")
    elif request.method == "POST":
        name = str(request.POST.get('name'))
        psw = str(request.POST.get('psw'))
        phone = str(request.POST.get('phone'))
        print name, psw, phone
        if Pone.objects.filter(name=name):
            return render(request, 'login.html', context = dict(
                data = "用户名已存在^_^",
                msg = False
                ))
        obj = Pone(name = name, psw = psw, phone = phone)
        obj.save()
        return render(request, 'login.html')


def index(request):
    if request.method == "GET":
        return render(request, "login.html", context = dict(
            data = "请先登录^_^",
            msg = False
            ))
    elif request.method == "POST":
        content = str(request.POST.get('content'))
        pattern = '^\s*|\s*$'
        content = re.sub(pattern, '', content)
        obj = Ptwo(content=content)
        obj.save()
        data = {"success": 'true', "content": content}
        return HttpResponse(json.dumps(data))


def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method == "POST":
        if request.POST.get('files', ''):
            uf = request.FILES['files']
            ufname = '%s/%s' % (settings.MEDIA_ROOT, uf.name)
            with open(ufname, 'wenjian') as f:
                for x in uf.chunks():
                    f.write(x)
            return render(request, 'upload.html', context = {dict(
                data = "上传成功",
                )})
        return render(request, "upload.html", context = dict(data = "请先选择文件", msg = "success"))
    return render(request, 'upload.html')

