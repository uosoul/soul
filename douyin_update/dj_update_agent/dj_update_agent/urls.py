"""dj_update_agent URL Configuration

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
from django.shortcuts import HttpResponse, render
import pymysql
from dj_update_agent.utils1 import getUserMsg
from dj_update_agent.test1 import update_agent
import sys
from dj_update_agent.tool_code import *
import os
import time
from concurrent.futures import ProcessPoolExecutor

#  return uid, nickname, unique_id, follower_count, following_count,
#  digg_count, aweme_count, favoriting_count, dongtai_count, address, avatar_url
# Uid 4296519660339635

def update(request):
    print(type(request), request)
    print(request.method)
    if request.method == 'GET':
        return render(request, 'update.html')
    else:
        Uid = int(request.POST.get('Uid'))
        print(Uid)
        brand = request.POST.get('brand')
        print(brand)
        state = update_agent(Uid, brand)
        if state:
            return HttpResponse('Success')
        else:
            return HttpResponse('Fail')



def check(request):

    if request.method == 'GET':
        host_list = ({'ip': '47.93.1.155', 'port': 22, 'username': 'root', 'password': 'Dyanalysis@abc456'},
                     {'ip': '47.111.182.11', 'port': 22, 'username': 'root', 'password': 'Dyanalysis@abc456'},
                     {'ip': '192.168.2.9', 'port': 22, 'username': 'tangy', 'password': '111111'})
                     

        lst = []
        executor = ProcessPoolExecutor(max_workers=3)

        futures = []
        for host in host_list:
            future = executor.submit(f1, host)
            futures.append(future)
        executor.shutdown(True)
        for future in futures:
            lst.extend(future.result())
            print(future.result())
        print(lst)

        return render(request, 'check.html', {'lst': lst})


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^update/', update),
    url(r'^check/', check),
]