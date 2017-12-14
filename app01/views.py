from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
# Create your views here.
from rbac import models
import re
from rbac.service.init_permission import init_permission
class BasePagPermission(object):
    def __init__(self, code_list):
        self.code_list = code_list

    def has_add(self):
        if "add" in self.code_list:
            return True

    def has_del(self):
        if "del" in self.code_list:
            return True

    def has_edit(self):
        if "edit" in self.code_list:
            return True


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.UserInfo.objects.filter(name=username, password=password).first()
        if user:
            init_permission(user, request)
            return redirect("/userinfo/")
        else:
            return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def userinfo(request):
    pagpermission = BasePagPermission(request.permission_code_url)  # 实例化
    # print("code......", request.permission_code_url)
    data_list = [
        {"id": 1, "name": "haiyan1"},
        {"id": 2, "name": "haiyan2"},
        {"id": 3, "name": "haiyan3"},
        {"id": 4, "name": "haiyan4"},
        {"id": 5, "name": "haiyan5"},
    ]
    #print("data_list",data_list)
    #print("pagpermission",pagpermission)
    return render(request, "userinfo.html", {"data_list": data_list, "pagpermission": pagpermission})


def userinfo_add(request):
    if request.method == "GET":
        return render(request,"userinfo_add.html")
    else:
        return redirect("/userinfo/")


def userinfo_del(request, nid):
    return HttpResponse("删除用户")


def userinfo_edit(request, nid):
    return HttpResponse("编辑用户")


def order(request):
    pagpermission = BasePagPermission(request.permission_code_url)  # 实例化
    print("code......", request.permission_code_url)
    return render(request,"order.html",{"pagpermission":pagpermission})


def order_add(request):
    return HttpResponse("添加订单")


def order_del(request, nid):
    return HttpResponse("删除订单")


def order_edit(request, nid):
    return HttpResponse("编辑订单")
