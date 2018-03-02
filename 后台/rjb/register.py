from django.http import HttpResponse
from django.shortcuts import render
from rjb.models import User
import json
import datetime

def register(request):
    return render(request, 'register.html')

def do_register(request):
    try:
        uname = request.POST.get('uname')
        upwd_1 = request.POST.get('upwd_1')
        upwd_2 = request.POST.get('upwd_2')
        uemail = request.POST.get('uemail')

        if User.objects.filter(uname=uname):
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'same name'}))
        if(upwd_1 != upwd_2):
            return HttpResponse(json.dumps({'statu_code':'1002', 'msg':'different passward'}))
    
        User.objects.create(uname = uname, upwd = upwd_1, uemail = uemail,
                            uidentity = '', usex = -1, uhonesty = 1.0, ubirthday = datetime.date(1900, 1, 1),
                            utel='', uadmin = (uname == 'admin'), uidcard="", urealname=""
                            )

        return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))
    except BaseException:
        return HttpResponse(json.dumps({'statu_code':'404', 'msg':'serve error'}))