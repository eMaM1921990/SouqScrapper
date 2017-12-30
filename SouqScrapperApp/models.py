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
    compare_at_Price = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100)
    discount_amount = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100,null=True)
    image_1 = models.URLField(null=True, blank=True)
    image_2 = models.URLField(null=True, blank=True)
    image_3 = models.URLField(null=True, blank=True)
    image_4 = models.URLField(null=True, blank=True)
    image_5 = models.URLField(null=True, blank=True)
    variant_option_one = models.CharField(max_length=250,null=True)
    variant_option_two = models.CharField(max_length=1024,null=True)
    affiliate_code = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    tags = models.TextField()
    shopify_id = models.CharField(max_length=1024, default=None, null=True)
    other_specs = models.TextField()

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
