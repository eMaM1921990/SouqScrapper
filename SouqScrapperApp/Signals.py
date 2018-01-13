import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration
from SouqScrapperApp.models import Product

__author__ = 'eMaM'


@receiver(post_save, sender=Product)
def push_to_shopify(sender, instance, **kwargs):
   if instance:
       # Integration
       shopifyIntegrationInstance = ShopifyIntegration()
       if instance.shopify_id:
           shopifyIntegrationInstance.removeShopifyProduct(id=instance.shopify_id)

       shopifyJson = shopifyIntegrationInstance.addNewProduct(productDict=instance.original_json)
       if shopifyJson:
           # update product
           shopifyIntegrationInstance.updateProduct(product=instance, shopifyJson=shopifyJson)
