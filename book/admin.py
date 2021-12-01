from django.contrib import admin
#导入模型
from book.models import Bookinfo,Peopleinfo
#注册模型
admin.site.register(Bookinfo)
admin.site.register(Peopleinfo)
# Register your models here.
