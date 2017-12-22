from django.db import models

# Create your models here.
class Users(models.Model):
    # id = models.IntegerField()
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.IntegerField()

    def tousers(self):
        return {'id':self.id,'username':self.username,'name':self.name,'password':self.password,'sex':self.sex,'phone':self.phone,'code':self.code,'address':self.address,'email':self.email}

    class Meta:
        db_table='users'
class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'type'

class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField()

    class Meta:
        db_table = "goods"  # 更改表名
    
    def toDict(self):
        return {'id':self.id,'goods':self.goods,'price':self.price,'picname':self.picname,'m':self.num,'descr':self.descr}

class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.CharField(max_length=11)
    total = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        db_table = "orders"  # 更改表名

class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    num = models.IntegerField()
    
    class Meta:
        db_table = "detail"  # 更改表名