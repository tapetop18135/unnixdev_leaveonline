from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import Profile, Remainleavedays, Suppervisor
from managedb.models import  Department, Position, Policy, Policytype
from managedbtrans.models import  History
from django.contrib.auth.models import User

from django.core import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# def index(request):
#     jsonSess = sessionResult(request)
#     # return JsonResponse({"index":"True" , "auth_":jsonSess}, safe=False)
#     return render(request, 'account/index.html', {"index":"True" , "auth_":jsonSess})


# def sessionResult(request):
#     json_auth = {
#         "status_login" : False,
#         "user" : None,
#         "email" : None
#     }
#     if request.session.keys():
#         user_id = request.session['_auth_user_id']
#         user_obj = User.objects.get(pk=user_id)
#         json_auth['user'] = user_obj.username
#         json_auth['email'] = user_obj.email
#         json_auth["status_login"] = True
#         return json_auth
#     else: 
#         return json_auth


@csrf_exempt
def login(request):
    if(request.method == "POST"):
        user_id = request.POST['id']
        user_pass = request.POST['password']
        user = authenticate(request, username=user_id, password=user_pass)
        if user:
            auth_login(request, user)
            return redirect('/user/')
        else:
            return JsonResponse({"singin":"fail"}, safe=False)
            # return render(request, 'account/failform.html')
        
    elif(request.method == "GET"):
        print("loginForm")
        return render(request, 'account/loginform.html')
    
def logout(request):
    auth_logout(request)
    return render(request, 'account/loginform.html')


@csrf_exempt
def register(request):
    if(request.method == 'POST'):
        
        # print(request.body)
        jsonreq = json.loads(request.body.decode("utf-8"))
        print(jsonreq)
        # return JsonResponse({"status":"finish"}, safe=False)
        if (User.objects.filter(username=jsonreq["nameuser"]) or User.objects.filter(email=jsonreq["email"])):
            return JsonResponse({"status":"error"}, safe=False)
        else:
            user_object = User(
                username=jsonreq["nameuser"], 
                password= make_password(jsonreq["password"]),
                email=jsonreq["email"],
            )
            user_object.save()
            profile_object = Profile(
                user_id=user_object.id,
                dep_name_id=jsonreq["department"],
                pos_name_id=jsonreq["position"],
            )
            profile_object.save()
            insertToRemainpol(jsonreq, user_object.id)

            if(jsonreq["position"]  == 1 or jsonreq["position"]  == 3):
                supervisor = Suppervisor(
                    dep_name_id=jsonreq["department"],
                    sup_name_id = user_object.id,
                )
                supervisor.save()

            return JsonResponse({"status":"finish"}, safe=False)
            
    else:
        dep = Department.objects.all().values('id', 'dep_name')
        pos = Position.objects.all().values('id', 'pos_name')
        response_data = {
            "status": "active",
            "position" : list(pos),
            "department" : list(dep),
        }
        return JsonResponse(response_data, safe=False)

def registerPage(request):
    return render(request, "account/registerForm.html")


def insertToRemainpol(jsonreq, user_id):
    type_policy = list(Policytype.objects.all().values('id','policy_name'))

    for i in range(0,len(type_policy)):
            # check Dep and Pos is not all
        policy_obj0 = Policy.objects.filter(
            policy_name_id=type_policy[i]['id'],
            dep_name_id=int(jsonreq['department']), 
            pos_name_id=int(jsonreq['position'])
        ).values('id','numofleave')
            # check Dep and Pos is all
        policy_obj1 = Policy.objects.filter(
            policy_name_id=type_policy[i]['id'],
            dep_name_id=1, # 1 is all
            pos_name_id=1  # 1 is all
        ).values('id','numofleave')
            # check Dep is no all but Pos is all
        policy_obj2 = Policy.objects.filter(
            policy_name_id=type_policy[i]['id'],
            dep_name_id=int(jsonreq['department']),
            pos_name_id=1 # 1 is all
        ).values('id','numofleave')
        if(policy_obj1):
            policy_obj = policy_obj1[0]
        elif(policy_obj2):
            policy_obj = policy_obj2[0]
        elif(policy_obj0):
            policy_obj = policy_obj0[0]
        else:
            continue

        remain_object = Remainleavedays(
            user_id=user_id,
            policy_id=policy_obj['id'],
            remain_days=policy_obj['numofleave'],
        )
        remain_object.save()

