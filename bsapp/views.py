# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Pone, Ptwo
import json, re


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        name = str(request.POST.get('name'))
        psw = str(request.POST.get('psw'))
        if psw and name:
            if Pone.objects.filter(name=name):
                if Pone.objects.filter(psw = psw):
                    return render(request, 'home.html')
        return HttpResponse('用户名或密码错误')


def regist(request):
    if request.method == "GET":
        return render(request, "regist.html")
    elif request.method == "POST":
        name = str(request.POST.get('name'))
        psw = str(request.POST.get('psw'))
        phone = str(request.POST.get('phone'))
        print name, psw, phone
        if Pone.objects.filter(name=name):
            return HttpResponse('用户名已存在')
        obj = Pone(name = name, psw = psw, phone = phone)
        obj.save()
        return render(request, 'login.html')



def index(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        obj = str(request.POST.get('content'))
        pattern = '^\s*|\s*$'
        r = re.sub(pattern, '', obj)
        print r
        ret = {"success": 'true', "content": r}
        return HttpResponse(json.dumps(ret))


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))