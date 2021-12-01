from django.db import models
'''
模型类继承自modle.model
系统自动为我们添加一个主键id
字段的定义
    字段名=models.类型（选项）
    字段名其实就是数据表的字段名
    字段名不要使用Python 以及数据库的关键字
    char(m)
    varchar(m)
    m就是选项
'''
class Bookinfo(models.Model):
    #继承自model 方便增删改查操作
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    # pass
class Peopleinfo(models.Model):
    #继承自model 方便增删改查操作
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    #外键约束，人物属于哪本书
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
