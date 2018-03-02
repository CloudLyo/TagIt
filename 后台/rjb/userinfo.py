from django.http import HttpResponse
from django.shortcuts import render
from rjb.models import *
import json
import datetime

def info(request):
    try:
        uname = request.session.get('uname')
        if not uname:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'Not login'}))

        puser = User.objects.get(uname = uname)

        ptags = tagsAndFrequence.objects.filter(user = puser)

        faceurl = ''
        pface = Face.objects.filter(owner=puser)
        if pface:
            faceurl = pface[0].pimg.url

        data = {
            'statu_code':'1000',
            'user' : {'uname':puser.uname, 'uemail':puser.uemail, 'usex':puser.usex,
                      'uindentity':puser.uidentity, 'uhonesty':puser.uhonesty,
                      'utel':puser.utel, 'uyear':puser.ubirthday.year,
                      'umonth':puser.ubirthday.month, 'uday':puser.ubirthday.day,
                      'uadmin':puser.uadmin, 'urealname':puser.urealname,
                      'uidcard':puser.uidcard, 'faceurl':faceurl
                      },
            'tags' : []
        }


        for tg in ptags:
            data['tags'].append({'tag':tg.tag, 'frequent':tg.frequent})

        return HttpResponse(json.dumps(data, ensure_ascii=False))

    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))

def modify(request):
    return render(request, 'modify.html')

def do_modify(request):
    try:
        uname = request.session.get('uname')

        usex = int(request.POST.get('sex', -1))
        uidentity = request.POST.get('identity', '')
        uday = int(request.POST.get('day', 1))
        umonth = int(request.POST.get('month', 1))
        uyear = int(request.POST.get('year', 1900))
        utel = request.POST.get('tel', '')
        uidcard = request.POST.get('idcard', '')
        urealname = request.POST.get('realname', '')

        birthday = datetime.date(uyear, umonth, uday)

        if not uname:
            return HttpResponse('not login')

        puser = User.objects.get(uname = uname)
        puser.usex = int(usex)
        puser.uidentity = uidentity
        puser.utel = utel
        puser.ubirthday = birthday
        puser.uidcard = uidcard
        puser.urealname = urealname
        puser.save()

        return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))

def upload_face(request):
    try:
        owner = User.objects.get(uname=request.session.get('uname'))
        img = Face.objects.filter(owner=owner)
        if img:
            img[0].pimg=request.FILES['img']
            img[0].save()
        else:
            Face.objects.create(pimg=request.FILES['img'], owner=owner)
        return HttpResponse(json.dumps({'statu_code': '1000', 'msg': 'ok'}))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code': '4000', 'msg': str(e)}))