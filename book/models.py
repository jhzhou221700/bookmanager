from django.db import models
'''
1.模型类继承自modle.model
系统自动为我们添加一个主键id
2.字段的定义
    2.1属性名
    字段名=models.类型（选项）
    属性名其实就是数据表的字段名
    属性名不要使用Python 以及数据库mysql的关键字
    2.2 mysql的类型
    char(m)
    varchar(m)
    m就是选项
    decimal 货币类型
    不要使用连续的下划线
    2.3 选项 是否有默认值，是否唯一，是否为null
        charfield必须设置字段最大长度值
        verbose_name 主要是admin站点使用
        null
        default
        unique
    creat table "qquser"(
    id int
    name varchar(10) not null default "")
3.改变表的名称
    默认表的名称是：子应用名_类名 （都是小写）
    修改表的名字：
    flask 先定义表 再定义模型 不需要执行迁移了
'''
#继承自modles.modle
class Bookinfo(models.Model):
    #继承自model 方便增删改查操作
    name=models.CharField(max_length=10,unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_deleate=models.BooleanField(default=False)
    #在数据库中重写表的名字
    class Meta:
        db_table="bookinfo"
        # verbose_name="数据管理"
        # #用于站点管理
    def __str__(self):
        return self.name
    # pass
class Peopleinfo(models.Model):
    #继承自model 方便增删改查操作
    #定义一个有序字典
    GENDER__CHOICE=(
        (1,"male"),
        (0,"female")
    )
    name=models.CharField(max_length=10,unique=True)
    #性别从哪里选
    gender=models.SmallIntegerField(choices=GENDER__CHOICE,default=1)

    despriction=models.CharField(max_length=100,null=True)
    is_delete=models.BooleanField(default=False)
    # 外键约束，人物属于哪本书
    # 关于外键 系统自动为外键添加id
    #外键的级联操作
    #主表 一对多 一
    #从表 多

    #主键的一条数据如果删除了，从 表有关联的数据如何处理？
    #设置set_null
    #抛出异常，不让删除 protect
    #级联设置  从表随主表一起消失 cascade,此处设置为级联操作
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
