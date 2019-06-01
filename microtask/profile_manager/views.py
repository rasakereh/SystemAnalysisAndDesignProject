from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(req):
    if req.method == 'POST':
        body = dict(req.POST)
        body = json.loads(list(body.keys())[0])
        print(body)

    return HttpResponse("SUCCESS", content_type="text/plain")