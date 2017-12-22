from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myweb.models import Users,Types,Goods
# from django.http import Http404
import time,PIL,os
from PIL import Image

#公共信息加载函数
def loadinfo():
    context={}
    context['type0list'] = Types.objects.filter(pid=0)
    return context

#网站首页
def index(request):
    context = loadinfo()
    # list = Goods.objects.filter()
    #商品点击量排序
    list = Goods.objects.raw('select * from goods order by clicknum desc limit 9 ' )
    context['goodslist'] = list
    # print(request.session['shoplist'])
    # print(len(request.session['shoplist'].keys()))
    fz = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=',1,'))
    context['fz'] = fz
    
    sm = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=',2,'))
    context['sm'] = sm
    
    dy = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=',19,'))
    context['dy'] = dy
    return render(request,"myweb/index.html",context)

#商品列表页
def list(request):
    context = loadinfo()
    list = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        tid = str(request.GET.get('tid',''))
        list = list.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
    context['goodslist'] = list
    fz = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=',1,'))
    context['fz'] = fz
    
    sm = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=',2,'))
    context['sm'] = sm
    
    dy = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=',19,'))
    context['dy'] = dy
    return render(request,"myweb/list.html",context)

#商品详情页
def detail(request,gid):
    context = loadinfo()
    ob = Goods.objects.get(id=gid)
    context['goods'] = ob
    ob.clicknum += 1
    ob.save()
    return render(request,"myweb/detail.html",context)

def login(request):
    # print(request.session)
    return render(request,'myweb/login.html')

def dologin(request):
    try:
        user = Users.objects.get(username=request.POST['user'])
        if user.state == 1 or user.state == 0:
            # 验证密码
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['password'],encoding="utf8"))
            if user.password == m.hexdigest():
                # request.session['username'] = user.name
                request.session['vipuser'] = user.tousers()
                # print(request.session['vipuser'])
                # print(request.session['vipuser']['username'])
                return redirect(reverse('index'))
            else:
                context = {'info':'登录密码错误！'}
        else:
            context = {'info':'此用户已被禁用,请联系管理员!'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"myweb/login.html",context)

def logout(request):
    # for i in request.session:
    #     print(i)
    del request.session['vipuser']
    return redirect(reverse('login'))

def register(request):
    context = loadinfo()
    return render(request,"myweb/register.html",context)

def person(request):
    user = Users.objects.get(name=request.session['vipuser']['name'])
    context = {'user':user}
    return	render(request,'myweb/person.html',context)
def doregister(request):
    import hashlib
    m = hashlib.md5() 
    m.update(bytes(request.POST['password'],encoding="utf8"))
    n = hashlib.md5() 
    n.update(bytes(request.POST['cpassword'],encoding="utf8"))

    try:
        import re
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        phone = request.POST['phone']
        email = request.POST['email']
        if re.match(r'\w{2,6}',name):
            if re.match(r'^[a-zA-Z0-9_-]{4,16}$',username):
                if re.match(r'\w{6,15}',password):
                    if m.hexdigest() == n.hexdigest():
                        if re.match(r'^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$',phone):
                            if re.match(r'^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$',email):
                                context = {'info':'恭喜您注册成功,可以登录!'}
                                ob = Users()
                                ob.name = name
                                ob.username = username
                                ob.password = m.hexdigest()
                                # ob.cpassword = cpassword
                                ob.phone = phone
                                ob.email = email
                                ob.save()
                                return render(request,'myweb/register.html',context)
                            else:
                                context = {'info':'邮箱不合法!'}
                        else:
                            context = {'info':'手机号不合法!'}
                    else:
                        context = {'info':'两次密码不同,请确认'}
                else:
                    context = {'info':'密码不合法!'}
            else:
                context = {'info':'账号不合法!'}
        else:
            context = {'info':'姓名不合法!'}
        return render(request,'myweb/register.html',context)
    except:
        context = {'info':'用户名已存在!'}
    return render(request,'myweb/register.html',context)

#======================购物车
def cart(request):
    context = loadinfo()
    if 'shoplist' not in request.  session:
        request.session['shoplist'] = {}
    return render(request,'myweb/cart.html',context)
def cart_add(request,sid):
    # for i in request.session:
    #     print(i)
    goods = Goods.objects.get(id=sid)
    shop = goods.toDict()
    # request.session['shop'] = goods.toDict()
    # print(request.session['shop'])
    shop['m'] = int(request.POST['m'])
    # print(request.POST['m'])
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    if sid in shoplist:
        shoplist[sid]['m']+= shop['m']
    else:
        shoplist[sid] = shop
    # print(shop)
    # context = {'shop':shop}
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart'))

def cart_del(request,gid):
    shoplist = request.session['shoplist']
    del shoplist[gid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart'))
def cart_clear(request):
    del request.session['shoplist']
    return render(request,'myweb/cart.html')

def cart_change(request):
    context = loadinfo()
    shoplist = request.session['shoplist']
    # a = request.GET['a']
    # print(a)
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num<1:
        num = 1
    shoplist[shopid]['m'] = num
    request.session['shoplist'] = shoplist
    return render(request,'myweb/cart.html',context)