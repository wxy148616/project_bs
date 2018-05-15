# -*- coding: utf-8 -*-
from django.contrib import admin
from bsapp.models import *


class BsappPostAdmin_user(admin.ModelAdmin):
    list_display = ['name', 'psw', 'phone']


admin.site.register(Users, BsappPostAdmin_user)


class BsappPostAdmin_con(admin.ModelAdmin):
    list_display = ['content', 'timestamp']


admin.site.register(Contents, BsappPostAdmin_con)


class BsappPostAdmin_file(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Files, BsappPostAdmin_file)

