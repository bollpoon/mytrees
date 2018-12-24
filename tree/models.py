from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#个人
class T_user(models.Model):
    SEX_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )#性别
    account = models.CharField(max_length=12,unique = True)#账号
    password = models.CharField(max_length=10)#密码
    card_pass = models.CharField(max_length=10)#银行卡密码
    name = models.CharField(max_length=20)#名字
    name_second = models.CharField(max_length=20)#昵称
    self_ID = models.CharField(max_length=18,unique = True)#身份证号
    phone = models.CharField(max_length=11)#电话
    email = models.CharField(max_length=200)#邮箱
    address = models.CharField(max_length=200)#居住地址
    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,    
                                related_name='tree_posts')
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sex = models.CharField(max_length=10,choices=SEX_CHOICES)
    
    class Meta:
           ordering = ('-publish',)
		
    def __str__(self):
        return self.account
    
class T_card(models.Model): 
    account = models.ForeignKey(to="T_user", to_field="account",
                                on_delete=models.CASCADE)
    card = models.CharField(max_length = 20)#银行卡账号
    def __str__(self):
        return self.card
    


