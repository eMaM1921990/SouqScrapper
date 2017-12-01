# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MANAGED = True


# Create your models here.
class Product(models.Model):
    url = models.URLField()
    sub_collection = models.CharField(max_length=250)
    collection = models.CharField(max_length=250)
    description = models.TextField()
    compare_at_Price = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    discount_amount = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image_1 = models.URLField(null=True,blank=True)
    image_2 = models.URLField(null=True,blank=True)
    image_3 = models.URLField(null=True,blank=True)
    image_4 = models.URLField(null=True,blank=True)
    image_5 = models.URLField(null=True,blank=True)
    variant_colors = models.CharField(max_length=250)
    variant_size = models.CharField(max_length=1024)
    affiliate_code = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    tags = models.TextField()

    class Meta:
        managed = MANAGED
        db_table = 'products'
