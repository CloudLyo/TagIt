from django.http import HttpResponse
from django.shortcuts import render
from rjb.models import *
import json

def history(request):
    try:
        uname = request.session.get('uname')

        if not uname:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'not login'}))

        puser = User.objects.get(uname=uname)

        res = tagHistroy.objects.filter(user=puser)

        data = {'statu_code':'1000', 'msg':'ok'}
        data['history'] = {}
        htags = {}
        for his in res:
            if his.hid in htags.keys():
                htags[his.hid].add(his.htag)
            else:
                htags[his.hid] = set()
                htags[his.hid].add(his.htag)

        for k, v in htags.items():
            data['history'][k] = list(v)
        return HttpResponse(json.dumps(data, ensure_ascii=False))
    except Exception as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))
