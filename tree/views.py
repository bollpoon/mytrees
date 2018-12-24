from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
#from django.contrib import auth
from django import forms
from django.shortcuts import redirect  

class UserForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=10)
   
def register(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)  #包含用户名和密码
        if form.is_valid():
            #获取表单数据
            username = form.cleaned_data['username']  #cleaned_data类型是字典，里面是提交成功后的信息
            password = form.cleaned_data['password']
            #判断用户是否存在
            user = auth.authenticate(username = username,password = password)
            if user:
                context['userExit']=True
                return render(request, 'register.html', context)
            
            #添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            #添加到session
            request.session['username'] = username
            #调用auth登录
            auth.login(request, user)
            #重定向到首页
            return  render(request,'login.html')
    else:
        context = {'isLogin':False} #将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
        return  render(request,'register.html')

def loginOK(request):
    return render(request,'loginOK.html')

def login(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
 
            #获取的表单数据与数据库进行比较
            user = authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(request,user)
                request.session['username'] = username
                return  redirect("http://localhost:8000")
            else:
                #比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(request, 'login.html')
    else:
        context = {'isLogin': False,'pswd':True}
    return render(request, 'login.html', context)


def circle(request):
    return render(request,'circle.html')

def add(request):
    return render(request,'add.html')
    
def message(request):
    return render(request,'message.html')

def box(request):
    return render(request,'box.html')

def _self(request):
    return render(request,'_self.html')

def friend(request):
    return render(request,'friend.html')
    
def self_opinion(request):
    return render(request,'self_opinion.html')

def interest(request):
    return render(request,'interest.html')

def news(request):
    return render(request,'news.html')

def add_2(request):
    return render(request,'add_2.html')
