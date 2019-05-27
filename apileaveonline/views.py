from django.shortcuts import render

from django.views.generic import View

from django.http import JsonResponse

import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from managedb import models

# from managedb.models import Policy, Department

# Create your views here.

# def policy(request):
#     if request.method == "POST":

class ReadFromSheet(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        
        return super(ReadFromSheet, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return JsonResponse({'status':True})

    def post(self, request, *args, **kwargs):
        try:
            jsonData = json.loads(request.body.decode("utf-8"))
            print(jsonData)
            
            return JsonResponse({'status':True})
        except:
            
            return JsonResponse({'status':False})

def get_policy(request):
    policys = models.Policy.objects.all()
    idpolycy = policys.values()
    keys = [k for k in policys.values()[0]][1:]
    jsonData = []
    print(policys.values()[0])
    print(keys)
    # print(policys.values()[0])
    for i in range(len(policys)):
        print(keys[0],i)
        jsonData.append([
            [keys[0], str(policys[i].policy_name), idpolycy[i][keys[0]]],
            [keys[1], str(policys[i].dep_name), idpolycy[i][keys[1]]],
            [keys[2], str(policys[i].pos_name), idpolycy[i][keys[2]]],
            [keys[3], str(policys[i].numofleave), idpolycy[i][keys[3]]], 
            ])
    # json.dumps(jsonData)
    print(jsonData)
    return JsonResponse({"policys": jsonData})