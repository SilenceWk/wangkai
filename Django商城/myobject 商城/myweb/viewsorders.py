from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myweb.models import Users,Types,Goods,Orders,Detail
# from django.views.decorators.csrf import csrf_exempt
import time

# @csrf_exempt
def ordersform(request):
    ids = request.GET['gids']
    if ids == '':
        return HttpResponse('请选择要结账的商品!')
    gids = ids.split(',')
    shoplist = request.session['shoplist']
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        total += shoplist[sid]['price']*shoplist[sid]['m']
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    # print(request.session['orderlist'])
    # print(request.session['shoplist'])
    # print(request.session['total'])
    # return HttpResponse('ok')
    return render(request,'myweb/ordersconform.html')

# @csrf_exempt
def ordersfirm(request):
    # print(request.session['orderslist'])
    return render(request,'myweb/ordersconfirm.html')

# @csrf_exempt
def ordersinsert(request):
    orders = Orders()
    orders.uid = request.session['vipuser']['id']
    orders.address = request.POST['address']
    orders.linkman = request.POST['linkman']
    orders.code = request.POST['code']
    orders.phone = request.POST['phone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    orderlist = request.session['orderlist']
    shoplist = request.session['shoplist']
    for shop in orderlist.values():
        del shoplist[str(shop['id'])]
        # print(shop)
        # print(request.session['shoplist'])
        # print(shoplist[str(shop['id'])])
        # print(shoplist)
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()
    del request.session['orderlist']
    del request.session['total']
    request.session['shoplist'] = shoplist
    # print(request.session.keys())
    return redirect(reverse('ordersinfo'))
    
def ordersinfo(request):
    # list = Detail.objects.filter()
    # print(request.session['vipuser'])
    memeda = request.session['vipuser']['id']
    list = Orders.objects.filter(uid=memeda)
    for order in list:
        de = Detail.objects.filter(orderid=order.id)
        order.detaillist = de
        time1 = order.addtime
        time2 = time.localtime(time1)
        time3 = time.asctime(time2)
        order.addtime = time3
        print(time3)
        # print(de)
        for wk in de:
            od = Goods.objects.get(id=wk.goodsid)
            wk.picname = od.picname
            od = Orders.objects.get(id=wk.orderid)
            wk.status = od.status
            # print(wk.picname)
            # print(wk.__dict__)
    # for i in list:
        # print(i.__dict__)

    # for ob in list:
    #     ty = Goods.objects.get(id=ob.goodsid)
    #     ob.typicname = ty.picname
    #     wk = Orders.objects.get(id=ob.orderid)
    #     ob.wkaddtime = wk.addtime
    context = {'orderlist':list}
    # print(request.session['shoplist'])
    return render(request,'myweb/ordersinfo.html',context)