from random import choice
from django.http import HttpResponse
from rjb.models import Picture
import json

def getPic(request):
    try:
        if request.session.get('uname'):
            obj = choice(Picture.objects.all())
            data = {'pid':str(obj.id), 'url':obj.pimg.url}
            data['statu_code'] = '200'
            data['msg'] = 'ok'
            if(obj):
                return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(json.dumps({'statu_code':'200', 'msg':'Not login'}))
    except BaseException:
        return HttpResponse(json.dumps({'statu_code':'404', 'msg':'serve error'}))


def getpicbyid(request):
    try:
        pid = int(request.POST['pid'])
        res = Picture.objects.filter(id=pid)
        if res:
            return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok', 'url':res[0].pimg.url}))
        else:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'no such picture'}))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'404', 'msg':'serve error'}))