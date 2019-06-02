from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from profile_manager.models import Profile

import json

@csrf_exempt
def register(req):
    if req.method == 'POST':
        body = dict(req.POST)
        body = json.loads(list(body.keys())[0])
        username = body['username']
        email = body['email']
        nationalid = body['nationalid']
        
        user = User.objects.filter(username=body['username'])
        if len(user) == 1:
            return HttpResponse("username", content_type="text/plain")

        user = User.objects.filter(email=body['email'])
        if len(user) == 1:
            return HttpResponse("email", content_type="text/plain")
        
        user = Profile.objects.filter(phone_num=body['phoneNum'])
        if len(user) == 1:
            return HttpResponse("phone number", content_type="text/plain")
        

        user = User.objects.create_user(username, body['email'], body['password'])
        user.first_name=body['firstName'],
        user.last_name=body['lastName'])
        user.save()
        profile = Profile(user=user,
                phone_num=body['phoneNum'],
                city=body['city'],
                country=body['country'],
                gender=body['gender'])

        profile.save()
        return HttpResponse("SUCCESS", content_type="text/plain")

    return HttpResponse("NOT A FORM", content_type="text/plain")
    
def login(req):
    if req.method == 'POST':
        body = dict(req.POST)
        body = json.loads(list(body.keys())[0])
        
        match = authenticate(username=body['username'], password=body['password'])
        if match is None:
            return HttpResponseForbidden()
        match = serializers.serialize("json", match)

        return HttpResponse(match, content_type="application/json")
    
    return HttpResponseBadRequest()
