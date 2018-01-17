from celery import group
from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks import *
from models import *
import time

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request):
    resp = {}
    resp['status'] = False


    querySet = Stores.objects.filter(store='Souq')
    scapper = SouqUAEScrapper()
    for record in querySet:
            # scrap.delay(url=record.url, collection='', subCollection='', isFashion=record.is_fashion, tags=record.tags)


        scapper.startScrappingProcessing(
            url=record.url,
            collection='',
            subCollection='',
            tags="UAE, Qatar, Bahrain, Oman, Kuwait, Saudi Arabia, Souq.com, Women's, Women's Jewellery, Women's Rings",
            isFashion=True

        )


    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"


    return Response(resp)





@never_cache
@api_view(['GET'])
def push_to_shopify(request):
    resp = {}
    resp['status'] = False
    push_products('test')
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)



@never_cache
@api_view(['GET'])
def check_job_group(request):
    job = group([
        task_one.subtask((1,1)),
        task_two.subtask()
    ])

    result = job.apply_async()
    if result.ready() and result.successful():
        # push_products.delay('Begining')
        pass
    resp = {}
    resp['status'] = False
    return Response(resp)