# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from models import *
from django.conf import settings
import json, re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        name = str(request.POST.get('name'))
        psw = str(request.POST.get('psw'))
        if psw and name:
            if Pone.objects.filter(name = name):
                if Pone.objects.filter(psw = psw):
                    obj = Pone.objects.get(name = name)
                    request.session['user_id'] = obj.id
                    request.session['name'] = obj.name
                    request.session['psw'] = obj.psw
                    return HttpResponseRedirect('/home/')
        return render(request, 'login.html', context = dict(
            data = u"用户名或密码错误^_^",
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
        if Pone.objects.filter(name = name):
            return render(request, 'regist.html', context = dict(
                data = u"用户名已存在^_^",
                msg = False
                ))
        obj = Pone(name = name, psw = psw, phone = phone)
        obj.save()
        return HttpResponseRedirect('/')


def home(request):
    if request.method == "GET":
        user_name = request.session.get('name')
        if user_name:
            if user_name == 'yangjunxia':
                return render(request, 'home.html', context = dict(
                    msg = 'wxy',
                    data = "I Love You"
                    ))
            return render(request, 'home.html', context = dict(
                user_name=user_name,
                msg = True
                ))
        else:
            return HttpResponseRedirect('/')
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
        user_name = request.session.get('name')
        if user_name:
            files_list = Pthree.objects.all().values_list('id', 'name', 'files')
            if files_list:
                return render(request, 'upload.html', context = dict(
                    files_list = files_list,
                    msg = "200"
                    ))
            return render(request, 'upload.html', context = dict(
                content = u"找～找不到了",
                msg = "upload_fail",
                ))
        return render(request, 'login.html', context = dict(
            status=10,
            content="登录超时，请重新登录"
            ))
    elif request.method == "POST":
        uf = request.FILES.get('files')
        if uf:
            ufname = u'%s/%s' % (settings.MEDIA_ROOT, uf.name)
            obj = Pthree()
            obj.name = uf.name
            obj.files = uf
            obj.save()
            with open(ufname, 'wb') as f:
                for x in uf.chunks():
                    f.write(x)
            files_list = Pthree.objects.all().values_list('id', 'name', 'files')
            return render(request, 'upload.html', context = dict(
                files_list=files_list,
                data = u"上传成功",
                msg = "upload_success"
                ))

        return render(request, "upload.html", context = dict(data = u"请先选择文件", msg = "null_fail"))
    return render(request, 'upload.html')


def file_download(request):
    if request.method == "GET":
        f_id = request.GET.get('id')
        fname = str(Pthree.objects.get(id=f_id).files).decode('utf-8')
        name = re.sub(r"(.*?)(?=/)/", "", fname)
        src = u'/Users/wangxvyang/Desktop/media_bs/%s' % fname
        try:
            file = open(src, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % name
            return response
        except EnvironmentError as e:
            return HttpResponse(u"资源不存在")
    return HttpResponse(u"找～找不到了")


def delete_file(request):
    if request.method == "POST":
        f_id = request.POST.get('id')
        fname = str(Pthree.objects.get(id=f_id).files).decode('utf-8')
        my_file = u'/Users/wangxvyang/Desktop/media_bs/%s' % fname
        if os.path.exists(my_file):
            import shutil
            # 删除之前备份
            oldname = my_file
            name = re.sub(r"(.*?)(?=/)/", "", fname)
            newname = u"/Users/wangxvyang/Desktop/beifen/%s" % name
            shutil.copyfile(oldname, newname)
            # 删除文件
            os.remove(my_file)
            #os.unlink(my_file)
            obj = Pthree.objects.get(id=f_id)
            obj.delete()
            return HttpResponse(json.dumps(dict(status=200, content_type='application/json')))
        else:
            return HttpResponse(json.dumps(dict(status=300, content_type='application/json')))
