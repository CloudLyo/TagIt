from django.http import HttpResponse
from django.shortcuts import render
from rjb.models import *
import json

def showImg(request):
    if(request.session.get('uname') == 'admin'):
        pit = Picture.objects.all()
        urls = [x.pimg.url for x in pit]
        ptags = []
        for i in pit:
            ptags.append(ptagsInfo.objects.filter(pic = i))

        return render(request, 'showImg.html', {'urls':zip(urls, ptags)})
    else:
        return HttpResponse(json.dumps({'statu_code':'200', 'msg':'Not admin'}))
