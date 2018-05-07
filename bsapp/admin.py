# -*- coding: utf-8 -*-
from django.contrib import admin
from bsapp.models import Ptwo


# Register your models here.
class BsappPostAdmin(admin.ModelAdmin):
    list_display = ['content', 'timestamp']


admin.site.register(Ptwo, BsappPostAdmin)