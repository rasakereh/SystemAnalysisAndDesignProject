from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
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
        

        user = User(username=username,
                        password=body['password'],
                        email=body['email'],
                        first_name=body['firstName'],
                        last_name=body['lastName'])
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
        matches = Profile.objects.filter(Q(username = body['username'])|Q(password = body['password'])).all()
        if len(matches) != 1:
            raise PermissionDenied
        match = serializers.serialize("json", matches[0])

        return HttpResponse(match, content_type="application/json")
