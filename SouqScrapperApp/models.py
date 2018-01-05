# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MANAGED = True


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    old_price = models.CharField(max_length=100, null=True)
    current_price = models.CharField(max_length=100)
    you_save = models.CharField(max_length=100)
    connection_value = models.TextField(null=True)
    images = models.TextField(null=True)
    manufacturer_en = models.CharField(max_length=120, null=True)
    brand = models.CharField(max_length=120)
    tags = models.TextField()
    other_specs = models.TextField()
    original_json = models.TextField()
    shopify_id = models.CharField(max_length=1024, default=None, null=True)
    affiliate_code = models.CharField(max_length=120,null=True,default='?a=1101l22027')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        managed = MANAGED
        db_table = 'products'


class Stores(models.Model):

    tags = models.TextField()
    url = models.TextField()
    is_fashion = models.BooleanField(default=False)
    store = models.CharField(max_length=150, default='Souq')

    def __str__(self):
        return self.store

    def __unicode__(self):
        return self.store

    class Meta:
        managed = MANAGED
        db_table = 'stores'
