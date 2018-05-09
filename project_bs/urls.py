"""project_bs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bsapp import views as bs_views

urlpatterns = [
    url(r'^$', bs_views.login, name = 'login'),
    url(r'^regist/', bs_views.regist, name = 'regist'),
    url(r'^home/', bs_views.index, name = 'home'),
    url(r'^ceshi/', bs_views.upload, name = 'ceshi'),
    url(r'^admin/', admin.site.urls),
]
