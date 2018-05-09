# -*- coding: utf-8 -*-
from django.contrib import admin
from bsapp.models import *


class BsappPostAdmin_one(admin.ModelAdmin):
    list_display = ['name', 'psw', 'phone']


admin.site.register(Pone, BsappPostAdmin_one)


class BsappPostAdmin_two(admin.ModelAdmin):
    list_display = ['content', 'timestamp']


admin.site.register(Ptwo, BsappPostAdmin_two)


class BsappPostAdmin_three(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Pthree, BsappPostAdmin_three)

