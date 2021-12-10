from django.shortcuts import render
#导入请求与相应
from django.http import HttpRequest
from  django.http import HttpResponse
from django.db.models import F
from django.db.models import Q
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



########删除数据###############
# 方式1
# book=Bookinfo.objects.get(id=6)
# book.delete()
# 删除份两种  物理删除（这条记录的数据删除）   逻辑删除（修改标记位，例如订单删除，现实删除，系统仍然存储）
# 方式2
# Bookinfo.objects.filter(id=5).delete()
# Create your views here.


#########查询#######
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
# book=Bookinfo.objects.get(id=1)
# 出现异常的处理：若果不存在，，抛出异常
# try:
#     book=Bookinfo.objects.get(id=1)
# except Bookinfo.DoesNotExist:
#     print("查询结果不存在")
# all查询多个结果。
# books=Bookinfo.objects.all()
# from book.models import Peopleinfo
# Peopleinfo.objects.all()
# count查询结果数量
# Peopleinfo.objects.all().count()
# 计算查询得到的总数据
# Peopleinfo.objects.count()


###过滤查询#####
#
# 实现SQL中的where功能，包括
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

#模型类名.objects.filter(属性名__运算符=值) 获取多个结果
#模型类名.objects.exclude(属性名__运算符=值) 排除 not
#模型类名.objects.get(属性名__运算符=值) 1个结果或异常

#测试
# 查询编号为1的图书
# Bookinfo.objects.get(id=1) 简写
# Bookinfo.objects.get(id__exact=1) 完整表示
# Bookinfo.objects.get(pk=1) primary key 主键值等于1
# Bookinfo.objects.filter(id=1) 返回的是包含一个元素的列表
# 查询书名包含'湖'的图书
# Bookinfo.objects.get(name__contains="湖")
# # 查询书名以'部'结尾的图书
# Bookinfo.objects.get(name__endswith="部")
# # 查询书名为空的图书
# try:
#     Bookinfo.objects.get(name__exact="")
# except Bookinfo.DoesNotExist:
#     print("不存在")
# # 查询编号为1或3或5的图书
# Bookinfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
# Bookinfo.objects.filter(id__gt=3) 大于gt 小于lt 大于等于
# 查询1980年发表的图书
# Bookinfo.objects.filter(pub_date__contains="1980")
# Bookinfo.objects.filter(pub_date__year="1980")
# # 查询1990年1月1日后发表的图书
# Bookinfo.objects.filter(pub_date__gt="1990-01-01")
#日期的合适 yyyy-mm-dd

#属性的比较 引用F属性

# from django.db.models import F
# 以fliter为例
# Bookinfo.objects.filter(readcount__gt=F("commentcount"))
#查找阅读量大于评论量的数据

#Q对象 或者查询
# from django.db.models import Q
# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
# Bookinfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
# 并且
# Bookinfo.objects.filter(Q(readcount__gt=20)&Q(id__lt=3))
#非 阅读量大于20且id大于3
Bookinfo.objects.filter(Q(readcount__gt=20)&~Q(id__lt=3))
#并且查询
#查询阅读；量大于20并且阅读量小于3 的数据

# Bookinfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# Bookinfo.objects.filter(readcount__gt=20,id__lt=3)


######聚合函数####
# 使用aggregate()过滤器调用聚合函数。
# 聚合函数包括：
# Avg平均，Count数量，Max最大，Min最小，Sum求和，
# 被定义在django.db.models中。
# from  django.db.models import Sum,Avg,Count,Min,Max
# 使用方法：
# object.aggregate

# 查询总阅读量
# Bookinfo.objects.aggregate(Sum('readcount'))

#级联查询
# 查询书籍为1的所有人物信息
# 数据里并没有人物信息
# 1对多的查询
# book=Bookinfo.objects.get(id=1)
# book.peopleinfo_set.all()
# ####################小写注意

# 查询人物为1的书籍信息
# 多对一的查询
#查询到人
# person=Peopleinfo.objects.get(id__exact=1)
#人里面的实例化对象的属性
# person.book.name


#关联查询的过滤查询
# 模型类名.objects.filter(关联模型类名小写__字段名__运算符=值)
# 查询图书，要求图书人物为"郭靖"
# Bookinfo.objects.filter(peopleinfo__name__exact="郭靖")
# # 查询图书，要求图书中人物的描述包含"八"
# Bookinfo.objects.filter(peopleinfo__description__contains="八")
# #查询书名为天龙八部的所有人物
# Peopleinfo.objects.filter(book__name__exact="天龙八部")
# #查询图书阅读量大于30的所有人物
# Peopleinfo.objects.filter(book__readcount__gt="30")

########查询集########
# 概念 查询集  ：从数据库中获取结果的集合
# 当调用如下过滤器方法时，Django会返回查询集（而不是简单的列表）：
#
# all()：返回所有数据。
# filter()：返回满足条件的数据。
# exclude()：返回满足条件之外的数据。
# order_by()：对结果进行排序。

# 对查询集的结果可以再次调用过滤器进行过滤度
# 从SQL的角度讲，查询集与select语句等价，过滤器像where、limit、order by子句
# books=Bookinfo.objects.filter(readcount__gt=30).order_by("pub_date")

#查询集的两大特性
# 1 惰性执行
# 创建查询集的时候不访问数据库，在调用数据库的时候才会执行
# 2 缓存
# 使用同一个查询集，第一次使用时会发生数据库的查询，
# 然后Django会把结果缓存下来，
# 再次使用这个查询集时会使用缓存的数据，
# 减少了数据库的查询次数。
# books=BookInfo.objects.all()
#
# [book.id for book in books]
#
# [book.id for book in books]

# 3限制查询集
# 对查询集进行取下标或切片的操作 等同于sql中的limit和offset子句。

# 对查询集进行切片后返回一个新的查询集，不会立即执行查询。
# 如果获取一个对象，直接使用[0]，等同于[0:1].get()，
# 但是如果没有数据，[0]引发IndexError异常，
# [0:1].get()如果没有数据引发DoesNotExist异常。
# >>> books = BookInfo.objects.all()[0:2] 现在还没执行  调用时才执行
# >>> books
# <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>

#4 ####
# 分页
#查询数据
# books = BookInfo.objects.all()
# #导入分页类
# from django.core.paginator import Paginator 导入分页工具
# #创建分页实例
# paginator=Paginator(books,2)  每两个book分为一页
# #获取指定页码的数据
# page_books = paginator.page(1)   读取第一页上的book信息
# #获取分页数据
# total_page=paginator.num_pages 查看总共有多少页