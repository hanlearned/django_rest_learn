from django.db import models

# Create your models here.
"""
    图书： 一本书可以有多个作者， 一本书只有一个出版社。
    作者： 一个作者可以出多本书。
    出版社：一个出版社可以出多本书。
"""


class Book(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=32, verbose_name="书名")
    price = models.FloatField(verbose_name="价格")
    author = models.ManyToManyField(to="Author")
    publish_time = models.DateField(null=True, verbose_name="出版时间")
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE,
                                verbose_name="出版社")

    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=32, verbose_name="名称")
    address = models.CharField(max_length=32, verbose_name="住址")
    SEX_CHOICE = (("男", 1), ("女", 0))  # 枚举
    sex = models.SmallIntegerField(choices=SEX_CHOICE, verbose_name="性别")
    introduction = models.TextField(verbose_name="作者简介")

    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)


class Publish(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=32, verbose_name="名称")
    address = models.CharField(max_length=32, verbose_name="位置")

    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
