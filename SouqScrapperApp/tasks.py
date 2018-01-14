from __future__ import absolute_import

from celery import shared_task

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration
from SouqScrapperApp.SouqUAE import SouqUAEScrapper
from SouqScrapperApp.models import Product


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
def push_products(input):
        product_query_set = Product.objects.all()
        shopifyIntegrationInstance = ShopifyIntegration()
        for product_row in product_query_set:
            try:
                if product_row.shopify_id:
                    shopifyIntegrationInstance.removeShopifyProduct(id=product_row.shopify_id)

                shopifyJson = shopifyIntegrationInstance.addNewProduct(productDict=product_row.original_json)
                if shopifyJson:
                    # update product
                    shopifyIntegrationInstance.updateProduct(product=product_row, shopifyJson=shopifyJson)

            except Exception as e:
                print str(e)


@shared_task(max_retries=10)
def check_task_status(tasks):
    completed_tasks = []
    for task in tasks:
        if task.ready():
            completed_tasks.append(task)

    # remove completed tasks
    tasks = list(set(tasks) - set(completed_tasks))
    if len(tasks) > 0:
        check_task_status.delay(tasks)

    else:
        print 'check_status_'
        # push_products.delay()



@shared_task(max_retries=10)
def task_test(param):
    return 10