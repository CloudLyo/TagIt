import json
from django.shortcuts import render
from django.http import HttpResponse
from rjb.models import Picture, User


def upload(request):
    return render(request, "upload.html")

def uploadImg(request):
    try:
        owner = User.objects.get(uname=request.session.get('uname'))
        if owner.uadmin:
            img = Picture(pimg = request.FILES['img'], owner = owner, finished = False,
                          result = '')
            img.save()
            return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))
    
        else:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'Not admin'}))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))