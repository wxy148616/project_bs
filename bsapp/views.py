# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from bsapp.serializers import BsappSerializer
from django.views.decorators.csrf import csrf_exempt
from pypinyin import lazy_pinyin
from models import *
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
            if Users.objects.filter(name = name):
                if Users.objects.filter(psw = psw):
                    obj = Users.objects.get(name = name)
                    request.session['user_id'] = obj.id
                    request.session['name'] = obj.name
                    request.session['psw'] = obj.psw
                    return HttpResponseRedirect('/home/')
        return render(request, 'login.html', context = dict(
            data = u"用户名或密码错误^_^",
            msg = "301"
            ))


def regist(request):
    if request.method == "GET":
        return render(request, "regist.html")
    elif request.method == "POST":
        name = str(request.POST.get('name'))
        psw = str(request.POST.get('psw'))
        phone = str(request.POST.get('phone'))
        print name, psw, phone
        if Users.objects.filter(name = name):
            return render(request, 'regist.html', context = dict(
                data = u"用户名已存在^_^",
                msg = False
                ))
        obj = Users(name = name, psw = psw, phone = phone)
        obj.save()
        return HttpResponseRedirect('/')


def home(request):
    user_id = request.session.get("user_id")
    if user_id:
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
            user_obj = Users.objects.get(id=user_id)
            content = str(request.POST.get('content'))
            pattern = '^\s*|\s*$'
            content = re.sub(pattern, '', content)
            Contents.objects.create(
                content = content,
                users = user_obj,
                )
            data = {"success": 'true', "content": content}
            return HttpResponse(json.dumps(data))
    return render(request, 'login.html', context = dict(
        status = 10,
        content = u"登录超时，请重新登录"
        ))


def upload(request):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == "GET":
            user_obj = Users.objects.get(id = user_id)
            files_list = user_obj.files_set.all().values_list('id', 'name', 'files').order_by('-id')
            # files_list = Files.objects.all().values_list('id', 'name', 'files').order_by('-id')
            paginator = Paginator(files_list, 5)
            page = request.GET.get('page')
            try:
                customer = paginator.page(page)
            except PageNotAnInteger:
                customer = paginator.page(1)
            except EmptyPage:
                customer = paginator.page(paginator.num_pages)
            user_name = request.session.get('name')
            if user_name:
                if files_list:
                    return render(request, 'upload.html', context = dict(
                        files_list = files_list,
                        cus_list = customer,
                        msg = "200"
                        ))
                return render(request, 'upload.html', context = dict(
                    content = u"找～找不到了",
                    msg = "upload_fail",
                    ))
            return render(request, 'login.html', context = dict(
                status=10,
                content=u"登录超时，请重新登录"
                ))
        elif request.method == "POST":
            uf = request.FILES.get('files')
            name = request.POST.get('name')
            user_id = request.session.get('user_id')
            user_obj = Users.objects.get(id=user_id)
            if uf:
                ufname = os.path.join(settings.MEDIA_ROOT, uf.name)
                with open(ufname, 'wb') as f:
                    for x in uf.chunks():
                        f.write(x)
                Files.objects.create(
                    name = name,
                    files = uf,
                    users = user_obj,
                    )
                return render(request, 'upload.html', context = dict(
                    data = u"上传成功",
                    msg = "upload_success"
                    ))

            return render(request, "upload.html", context = dict(data = u"请先选择文件", msg = "null_fail"))
        return render(request, 'upload.html')
    return HttpResponseRedirect('/')


def file_download(request):
    if request.method == "GET":
        f_id = request.GET.get('id')
        fname = str(Files.objects.get(id=f_id).files).decode('utf-8')
        name = re.sub(r"(.*?)(?=/)/", "", fname)
        src = os.path.join(settings.MEDIA_ROOT, fname)
        try:
            p_name = lazy_pinyin(name)
            name = "".join(p_name)
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
        fname = str(Files.objects.get(id=f_id).files).decode('utf-8')
        my_file = os.path.join(settings.MEDIA_ROOT, fname)
        if os.path.exists(my_file):
            import shutil
            # 删除之前备份
            oldname = my_file
            name = re.sub(r"(.*?)(?=/)/", "", fname)
            newname = os.path.join(settings.MEDIA_ROOT + "/beifen/", name)
            shutil.copyfile(oldname, newname)
            # 删除文件
            os.remove(my_file)
            #os.unlink(my_file)
            obj = Files.objects.get(id=f_id)
            obj.delete()
            return HttpResponse(json.dumps(dict(status=200, content_type='application/json')))
        else:
            return HttpResponse(json.dumps(dict(status=300, content_type='application/json')))


@csrf_exempt
def snippet_list(request):
    if request.method == "GET":
        obj = Users.objects.all()
        serializer = BsappSerializer(obj, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BsappSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)

        return JsonResponse(serializer.errors, status = 400)


@csrf_exempt
def snippet_detail(request, id):
    try:
        obj = Users.objects.get(id = id)
    except Users.DoesNotExist:
        return HttpResponse(status = 400)
    if request.method == 'GET':
        serializer = BsappSerializer(obj)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BsappSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == "DELETE":
        obj.delete()
        return HttpResponse(status = 204)
