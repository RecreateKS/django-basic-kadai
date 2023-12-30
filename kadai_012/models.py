from django.db import models
from django.urls import reverse

#カテゴリ
class Category(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
          return self.name

#商品
class Product(models.Model):
     name = models.CharField(max_length=200)
     price = models.PositiveIntegerField()
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     img = models.ImageField(blank=True, default='noImage.png')
     detail = models.CharField(max_length=1000)

     #プロダクト名を表示
     def __str__(self):
          return self.name

     
