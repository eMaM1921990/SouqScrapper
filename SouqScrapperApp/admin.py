# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from SouqScrapperApp.models import Product



# Resources
class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        skip_unchanged = True




class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'collection', 'sub_collection', 'title', 'color',
                    'brand']

    list_per_page = 10
    search_fields = ('id', 'collection','sub_collection','color')

    resource_class = ProductResource

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


admin.site.register(Product, ProductAdmin)
