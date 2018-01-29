from __future__ import absolute_import

from celery import shared_task

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration
from SouqScrapperApp.SouqUAE import SouqUAEScrapper
from SouqScrapperApp.models import Product
import json

from SouqScrapperApp.ounass_scrapper import OunassScrapper


def ServiceTemporarilyDownError(object):
    raise Exception('This is not handled!')


@shared_task(max_retries=10)
def scrap(url, collection, subCollection, tags, isFashion):
    scapper = SouqUAEScrapper()
    try:
        scapper.startScrappingProcessing(
            url=url,
            collection=collection,
            subCollection=subCollection,
            tags=tags,
            isFashion=isFashion

        )
    except ServiceTemporarilyDownError:
        print 'error'
        raise scrap.retry()



@shared_task(max_retries=10)
def scrap_ounaas(url, tags):
    ounass_scrapper = OunassScrapper()
    try:
        ounass_scrapper.startScrappingProcessing(
            url=url,
            tags=tags

        )
    except ServiceTemporarilyDownError:
        print 'error'
        raise scrap.retry()


# @shared_task(max_retries=10)
def push_products(result):
    print 'inside push product'
    product_query_set = Product.objects.filter(shopify_id__null=True)
    shopifyIntegrationInstance = ShopifyIntegration()
    for product_row in product_query_set:
        print product_row
        if product_row.shopify_id:
            shopifyIntegrationInstance.removeShopifyProduct(id=product_row.shopify_id)
        #
        product_dict = json.loads(product_row.original_json)

        shopifyJson = shopifyIntegrationInstance.addNewProduct(productDict=product_dict)
        if shopifyJson:
            # update product
            shopifyIntegrationInstance.updateProduct(product=product_row, shopifyJson=shopifyJson)

    return 'done'


@shared_task
def task_one(param, pram):
    print 'test one'
    return param + pram


@shared_task
def task_two():
    print 'test two'
    return 20


@shared_task
def task_three():
    print 'task thee'
    return 100
