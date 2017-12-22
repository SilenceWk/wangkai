from django.shortcuts import render

from django.http import HttpResponse

def test(request):
    # return HttpResponse('OK')
    return render(request,'myweb/test.html')

def test1(request):
    user = str(request.POST['username'])
    import re
    if re.match(r'\w{4,8}',user):
    	if request.POST['password'] == request.POST['cpassword']:
    		context = {'info':'可用登录'}
    	else:
    		context = {'info':'两次密码不一样'}
    else:
    	context = {'info':'账号不合规则'}
    return render(request,'myweb/test.html',context)
    