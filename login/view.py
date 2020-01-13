from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from .models import user
from django.contrib.auth.hashers import make_password, check_password

from django.views.decorators.csrf import csrf_exempt


class UserForm ( forms.Form ):
    username = forms.CharField ( label='用户名', max_length=10 )
    password = forms.CharField ( label='密码', widget=forms.PasswordInput () )


# 处理登录的方法
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render ( request, 'login.html' )

    if request.method == 'POST':
        data = UserForm ( request.POST )
        if data.is_valid ():
            # 获取到表单提交的值
            username = data.cleaned_data['username']
            password = data.cleaned_data['password']
            # 把表单中取到的值和数据库里做对比

            try:
                use = user.objects.get ( u_name=username )
                if password == use.u_password:
                    response = HttpResponseRedirect ( '/index/' )
                    return response
                else:
                    response = HttpResponseRedirect ( '/login/' )
                    return response
            except:
                response = HttpResponseRedirect ( '/login/' )
                return response
        else:
            response = HttpResponseRedirect ( '/login/' )
            return response


def logout(request):  # 退出登录的方法
    if request.method == 'GET':
        response = HttpResponseRedirect ( '/login/' )
        return response


def index(request):
    if request.method == 'GET':
        return render ( request, 'index.html' )