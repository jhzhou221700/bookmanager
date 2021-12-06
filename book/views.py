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
"""
#3个参数
1 请求
2 模板名字 因为定义了templates的路径 此处从templates往下写即可
3  内容
"""
from  book.models import Bookinfo,Peopleinfo
def index(request):
    # return HttpResponse("ok")
    context={
        "name":"马上双十一，点击有惊喜"
    }
    return render(request,'book/index.html',context=context)
#使用python manage 。py shell 进行操作数据 作用 ：所见即所得 快速验证增删改查的结构
# 最终的代码仍需在视图函数中编写bo
#1 获取对象>>> from book.models import Bookinfo
    # >>> Bookinfo.objects.all()
#######增加数据###########
# from book.models import Bookinfo
# #方式1
# book=Bookinfo(
#     name="Django",
#     pub_date="2000-1-1",
#     readcount="10",
# )
#调用完后使用book.save()进行保存
# #######

#方式2
# Bookinfo.objects.create(
#     name="测试方法",
#     pub_date="2000-1-1",
#     readcount="10",
# )


##修改数据##
# 方式1
#select * from bookinfo where id=6
# Bookinfo.objects.get(id=6)
# book.name="查询方法"
# book.save()


#方式2
#get方法后面没有update
# Bookinfo.objects.filter(id=6).update(name="过滤方法")
# Create your views here.
