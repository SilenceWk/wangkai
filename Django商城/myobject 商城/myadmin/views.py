from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Users,Types,Goods,Detail,Orders
# from django.http import Http404
import time,PIL,os
from PIL import Image


def index(request):
    # raise Http404('请求出错')
    return render(request,'myadmin/index.html')

def usersindex(request,pIndex):
    list = Users.objects.all()

    if request.GET.get('username','')!='':
        list = list.filter(username__contains=request.GET['username'])

    
    p = Paginator(list,4)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    maxnum = p.num_pages

    context = {'userslist':list2,'plist':plist,'pIndex':pIndex,'maxnum':maxnum}
    return render(request,'myadmin/usersindex.html',context)
#跳转到管理员注册页面
def usersadd(request):
    return render(request,'myadmin/usersadd.html')
#执行添加操作
def usersinsert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']

        #密码md5加密
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding='utf8'))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = time.time()
        #保存进数据库
        ob.save()
        context={'info':'添加成功！'}
    except:
        context={'info':'添加失败！'}
    return render(request,'myadmin/info.html',context)

def usersdel(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        #从数据库中删除数据
        ob.delete()
        context = {'info':'删除成功'}
    except:
        context = {'info':'删除失败'}
    return render(request,'myadmin/info.html',context)

def usersedit(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        context = {'user':ob}
        return render(request,'myadmin/edit.html',context)
    except:
        context = {'info':'修改失败'}
    return render(request,'myadmin/info.html',context)

def usersupdate(request):
    try:
        ob = Users.objects.get(id=request.POST['id'])
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
    # return HttpResponse('成功')

        context = {'info':'修改成功'}
    except:
        context = {'info':'修改失败'}
    return render(request,'myadmin/info.html',context)

#==========后台管理员操作
def login(request):
    return render(request,'myadmin/login.html')
def dologin(request):
    verifycode = request.session['verifycode']
    code = request.POST['code']
    #验证时候不区分大小写，都变为小写
    if verifycode.lower() != code.lower():
        context = {'info':'验证码错误！'}
        return render(request,'myadmin/login.html',context)
    try:
        user = Users.objects.get(username=request.POST['username'])
        if user.state == 0:
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'],encoding='utf8'))
            if user.password == m.hexdigest():
                print(m.hexdigest())
                request.session['adminuser'] = user.name
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info':'登陆密码错误'}
        else:
            context = {'info':'用户不是后台管理员'}
    except:
        context = {'info':'登录账号错误'}
    return render(request,'myadmin/login.html',context)
    # return HttpResponse('cuow')
def logout(request):
    del request.session['adminuser']#清除session
    return redirect(reverse('myadmin_login'))
    # return HttpResponse('hello')
def verify(request):
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/myadmin/font/STXIHEI.TTF', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((10, -2), rand_str[0], font=font, fill=fontcolor)
    draw.text((30, -2), rand_str[1], font=font, fill=fontcolor)
    draw.text((60, -2), rand_str[2], font=font, fill=fontcolor)
    draw.text((80, -2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

#================后台商品信息类别管理
def typeindex(request,pIndex):

    list = Types.objects.extra(select={'_has':'concat(path,id)'}).order_by('_has')
    # list = Types.objects.all()
    for ob in list:
        ob.pname = '...'*(ob.path.count(',')-1)
    
    if request.GET.get('name','') != '':
        list = list.filter(name__contains=request.GET.get('name'))

    p = Paginator(list,4)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    maxnum = p.num_pages
    context = {'typeslist':list2,'plist':plist,'pIndex':pIndex,'maxnum':maxnum}
    return render(request,'myadmin/type/index.html',context )

def typeadd(request,tid):
    if tid == '0':
        context = {'pid':0,'path':'0,','name':'根类别'}
    else:
        ob = Types.objects.get(id=tid)
        context = {'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
    return render(request,'myadmin/type/add.html',context)

def typeinsert(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,'myadmin/info.html',context)

def typedel(request,tid):
    try:
        row = Types.objects.filter(pid=tid).count()
        if row>0:
            context = {'info':'删除失败:此类别下还有子类别！'}
            return render(request,'myadmin/info.html',context)
        ob = Types.objects.get(id=tid)
        ob.delete()
        context = {'info':'删除成功!'}
    except:
        context = {'info':'删除失败!'}
    return render(request,'myadmin/info.html',context)

def typeedit(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        context = {'type':ob}
        return render(request,'myadmin/type/edit.html',context)
    except:    
        context = {'info':'没有找到要修改的信息！'}
    return render(request,'myadmin/info.html',context)

def typeupdate(request):
    try:
        ob = Types.objects.get(id=request.POST['id'])
        ob.name = request.POST['name']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败! '}
    return render(request,'myadmin/info.html',context)

#==============后台商品信息管理
def goodsindex(request,pIndex):
    # list = Goods.objects.raw('select g.*,t.name typename from goods g,type t where g.typeid=t.id')
    list = Goods.objects.filter()
    for ob in list:
        ty = Types.objects.get(id=ob.typeid)
        ob.typename = ty.name
    if request.GET.get('goods','') != '':
        list = list.filter(goods__contains=request.GET.get('goods'))
    p = Paginator(list,2)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    maxpage = p.num_pages
    context = {'goodslist':list2,'plist':plist,'pIndex':pIndex,'maxpage':maxpage}
    return render(request,'myadmin/goods/index.html',context)

def goodsadd(request):
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    context = {'typelist':list}
    return render(request,'myadmin/goods/add.html',context)

def goodsinsert(request):
    try:
        # 判断并执行图片上传，缩放等处理
        myfile = request.FILES.get("pic", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        # 以时间戳命名一个新图片名称
        filename= str(time.time())+"."+myfile.name.split('.').pop()
        destination = open(os.path.join("./static/goods/",filename),'wb+')
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        # 执行图片缩放
        im = Image.open("./static/goods/"+filename)
        # 缩放到375*375:
        im.thumbnail((375, 375))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/"+filename, 'jpeg')
        # 缩放到220*220:
        im.thumbnail((220, 220))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/m_"+filename, 'jpeg')
        # 缩放到220*220:
        im.thumbnail((100, 100))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/goods/s_"+filename, 'jpeg')

        # 获取商品信息并执行添加
        ob = Goods()
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.descr = request.POST['descr']
        ob.picname = filename
        ob.state = 1
        ob.addtime = time.time()
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}

    return render(request,"myadmin/info.html",context)

def goodsdel(request,gid):
    try:
        # 获取被删除商品信的息量，先删除对应的图片
        ob = Goods.objects.get(id=gid)
        #执行图片删除
        os.remove("./static/goods/"+ob.picname)   
        os.remove("./static/goods/m_"+ob.picname)   
        os.remove("./static/goods/s_"+ob.picname)
        #执行商品信息的删除 
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

def goodsedit(request,gid):
    try:
        # 获取要编辑的信息
        ob = Goods.objects.get(id=gid)
        # 获取商品的类别信息
        list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
        # 放置信息加载模板
        context = {"typelist":list,'goods':ob}
        return render(request,"myadmin/goods/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/info.html",context)

def goodsupdate(request,gid):
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)
            if not myfile:
                return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
            filename = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open(os.path.join("./static/goods/",filename),'wb+')
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()
            # 执行图片缩放
            im = Image.open("./static/goods/"+filename)
            # 缩放到375*375:
            im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/"+filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((220, 220))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/m_"+filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((100, 100))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goods/s_"+filename, 'jpeg')
            b = True
            picname = filename
        else:
            picname = oldpicname
        ob = Goods.objects.get(id=gid)
        ob.goods = request.POST['goods']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.descr = request.POST['descr']
        ob.picname = picname
        ob.state = request.POST['state']
        ob.save()
        context = {'info':'修改成功！'}
        if b:
            os.remove("./static/goods/m_"+oldpicname) #执行老图片删除  
            os.remove("./static/goods/s_"+oldpicname) #执行老图片删除  
            os.remove("./static/goods/"+oldpicname) #执行老图片删除  
    except:
        context = {'info':'修改失败！'}
        if b:
            os.remove("./static/goods/m_"+picname) #执行新图片删除  
            os.remove("./static/goods/s_"+picname) #执行新图片删除  
            os.remove("./static/goods/"+picname) #执行新图片删除  
    return render(request,"myadmin/info.html",context)


#=====================后台订单浏览
def order(request):
    # print(request.session['adminuser'])
    list = Detail.objects.filter()
    for ob in list:
        wk = Goods.objects.get(id=ob.goodsid)
        ob.picname = wk.picname
    context = {'orderlist':list}
    return render(request,'myadmin/order.html',context)

def look(request):
    gid = request.GET['gid']
    # print(gid)
    list = Orders.objects.filter(id=gid)
    context = {'userinfo':list}
    # print(list)
    return render(request,'myadmin/look.html',context)
def change(request):
    gid = request.GET['gid']
    context = {'gid':gid}
    return render(request,'myadmin/change.html',context)

def zchange(request):
    gid = request.GET['gid']
    print(gid)
    status = request.GET.get('status','')
    if status != '':
        # return HttpResponse('ok')
        ob = Orders.objects.get(id=gid)
        ob.status = status
        print(ob)
        ob.save()
        context = {'info':'修改成功！'}
        return render(request,'myadmin/info.html',context)
    else:
        context = {'info':'您还没有选择订单状态！'}
        return render(request,'myadmin/info.html',context)
    # print(status)