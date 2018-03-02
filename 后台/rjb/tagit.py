from django.http import HttpResponse
from django.shortcuts import render
from random import choice
from rjb.models import *
import json
import time

MIN_SUPPORT = 1
NEEDED_TAGS = 2

def tag(request):
    try:
        pit = choice(Picture.objects.filter(finished=False))

        imgid = pit.id
        purl = pit.pimg.url

        tags = ptagsInfo.objects.filter(pic = pit)

        data = {'url':purl, 'pid':imgid, 'tags': []}
        for tg in tags:
            data['tags'].append({'tag':tg.tag, 'frequent':tg.frequent})
        data['statu_code'] = '1000'
        return HttpResponse(json.dumps(data, ensure_ascii=False))

    except BaseException:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':'serve error'}))

def tag_it(request):
    try:
        user_name = request.session.get('uname')
        if not user_name:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'not login'}))

        pid = int(request.POST['pid'])
        tags = request.POST['tag']
        tags = map(str.strip, tags.split(','))
        puser = User.objects.get(uname = user_name)
        ppic = Picture.objects.get(id = pid)

        for tag in tags:
            tagHistroy.objects.create(hid=pid, htag=tag, user=puser)
            pt = ptagsInfo.objects.filter(tag = tag, pic = ppic)
            if pt:
                pt[0].frequent += 1
                pt[0].save()
            else:
                ptagsInfo.objects.create(tag = tag, frequent = 1, pic = ppic)

            tf = tagsAndFrequence.objects.filter(tag = tag, user = puser)
            if tf:
                tf[0].frequent += 1
                tf[0].save()
            else:
                tagsAndFrequence.objects.create(tag = tag, frequent = 1,user = puser)

        tmptags = sorted(ptagsInfo.objects.filter(pic=ppic), key=lambda x: x.frequent,  reverse=True)
        if len(tmptags) > NEEDED_TAGS and tmptags[NEEDED_TAGS - 1].frequent >= MIN_SUPPORT:
            ppic.finished = True
            data = {'picture_name':ppic.pimg.name, 'finish_time':time.ctime()}
            data['labels'] = []
            for i in tmptags[:NEEDED_TAGS]:
                data['labels'].append(i.tag)
            ppic.result = json.dumps(data, ensure_ascii=False)
        ppic.save()

        return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))

    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))

def tags_by_id(request):
    try:
        id = int(request.GET['pid'])
        ppic = Picture.objects.get(id = id)
        tags = ptagsInfo.objects.filter(pic=ppic)
        data = {}
        data['tags'] = []
        for t in tags:
            data['tags'].append(t.tag)
        data['statu_code'] = '1000'
        data['msg'] = 'ok'
        return HttpResponse(json.dumps(data, ensure_ascii=False))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':'serve error'}))

def del_tags(request):
    try:
        user_name = request.session.get('uname')
        if not user_name:
            return HttpResponse(json.dumps({'statu_code':'1001', 'msg':'not login'}))
        pid = request.POST['pid']
        tags = request.POST['tags']
        tags = list(map(str.strip, tags.split(',')))
        picture_object = Picture.objects.get(id=pid)
        user_object = User.objects.get(uname=user_name)

        for tg in tags:
            ts_object = tagHistroy.objects.get(user=user_object, htag=tg, hid=pid)
            tf_object = tagsAndFrequence.objects.get(user=user_object, tag=tg)
            pt_object = ptagsInfo.objects.get(pic=picture_object, tag=tg)
            ts_object.delete()
            if tf_object.frequent > 1:
                tf_object.frequent -= 1
                tf_object.save()
            else:
                tf_object.delete()

            if pt_object.frequent > 1:
                pt_object.frequent -= 1
                pt_object.save()
            else:
                pt_object.delete()
        return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok'}))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))

def search_by_tag(requests):
    try:
        tag = requests.GET['tag']
        p_info = ptagsInfo.objects.filter(tag=tag)
        ret = {'statu_code':'1000', 'msg':'ok'}
        ret['pic'] = []
        for p in p_info:
            ret['pic'].append({'pid':p.pic_id, 'frequent':p.frequent})
        return HttpResponse(json.dumps(ret))
    except BaseException as e:
        return json.dumps({'statu_code':'4000', 'msg':str(e)})

def get_result(requests):
    try:
        user_name = requests.session.get('uname')
        pics = Picture.objects.filter(owner__uname=user_name, finished=True)
        data = []
        for info in pics:
            data.append(info.result)
        return HttpResponse(json.dumps({'statu_code':'1000', 'msg':'ok', 'ans':data}, ensure_ascii=False))
    except BaseException as e:
        return HttpResponse(json.dumps({'statu_code':'4000', 'msg':str(e)}))