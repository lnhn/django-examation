from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    major=models.CharField(max_length=5)

    def __str__(self):
        return self.major

class People(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,verbose_name='姓名')
    age=models.CharField(max_length=200,verbose_name='年龄')
    sex=models.CharField(max_length=10,verbose_name="性别")
    phone=models.CharField(max_length=11,verbose_name="手机")
    major=models.ForeignKey(Major,verbose_name='专业',on_delete=models.CASCADE)
    prof=models.BooleanField(verbose_name='专家')

    def __str__(self):
        return self.name


