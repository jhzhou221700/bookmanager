from django.shortcuts import render
#导入请求与相应
from django.http import HttpRequest
from  django.http import HttpResponse
#定义视图函数
"""
视图函数的要求
1、视图函数的参数为接受请求
2、视图必须返回响应
"""
def index(request):
    # return HttpResponse("ok")
    context={
        "name":"马上双十一，点击有惊喜"
    }
    return render(request,'book/index.html',context=context)

#3个参数
"""
1 请求
2 模板名字 因为定义了templates的路径 此处从templates往下写即可
3  内容
"""
# Create your views here.
