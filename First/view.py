# -*- coding: utf-8 -*-
import json
import datetime
from django.http import HttpResponse
from FirdataModel.models import Article
from .JsdateUtil import CJsonEncoder
def getArticles(request):
    list = Article.objects.all()
    r = []
    resp = {}
    resp['status'] = 0
    datas = []
    resp['msg'] = ''
    for var in list:
        data = {}
        data['title'] = var.title
        data['content'] = var.content
        data['pub_date'] = var.pub_date
        data['update_time'] = var.update_time
        datas.append(data)
    resp['data'] = datas
    r.append(resp)
    return HttpResponse(json.dumps(r,indent=4,cls=CJsonEncoder), content_type="application/json")
