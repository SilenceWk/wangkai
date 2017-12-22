from django.conf.urls import url
from django.contrib import admin
from . import views
from . import viewstest
from . import viewsorders

urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^list/$', views.list,name='list'),
    url(r'^detail/(?P<gid>[0-9]+)$', views.detail,name='detail'),

    #=============前台登录界面
    url(r'^login/$', views.login,name='login'),
    url(r'^dologin/$', views.dologin,name='dologin'),
    url(r'^person/$', views.person,name='person'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^register/$', views.register,name='register'),
    url(r'^doregister/$', views.doregister,name='doregister'),

    # #=========================测试
    # url(r'^test/', viewstest.test,name='test'),
    # url(r'^test1/', viewstest.test1,name='test1'),
    #===============购物车
    url(r'^cart/$', views.cart,name='cart'),
    url(r'^cart/add/(?P<sid>[0-9]+)$', views.cart_add, name='cart_add'), # 添加购物车
    url(r'^cart/del/(?P<gid>[0-9]+)$', views.cart_del, name='cart_del'), # 删除购物车的一种商品
    url(r'^cart/clear$', views.cart_clear, name='cart_clear'), # 清空购物车
    url(r'^cart/change$', views.cart_change, name='cart_change'), # 更改购物车中的商品

    #=================订单路由=========
    url(r'^ordersform/$', viewsorders.ordersform,name='ordersform'),
    url(r'^ordersfirm/$', viewsorders.ordersfirm,name='ordersfirm'),
    url(r'^ordersinsert/$', viewsorders.ordersinsert,name='ordersinsert'),
    url(r'^ordersinfo/$', viewsorders.ordersinfo,name='ordersinfo'),


]
