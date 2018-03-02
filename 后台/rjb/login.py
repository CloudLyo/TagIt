#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from rjb.models import User
import json

def login(request):
    return render(request, 'login.html')

def do_login(request):
    try:
        name = request.POST['name']
        pwd = request.POST['pwd']

        qres = None
        try:
            qres = User.objects.get(uname = name)
        except BaseException:
            return HttpResponse(json.dumps({'statu_code':'1002', 'msg':'can not fine the user'}))

        if qres and qres.upwd == pwd:
            request.session['uname'] = qres.uname
            return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))
        else:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'error password'}))
    except BaseException:
        return HttpResponse(json.dumps({'statu code':'4000', 'msg':'serve error'}))

def do_logout(request):
    try:
        del request.session['uname']
    except BaseException:
        pass
    return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))
