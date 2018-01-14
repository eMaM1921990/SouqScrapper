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
    task_list = []
    for record in querySet:
        task_list.append(
            scrap.delay(url=record.url, collection='', subCollection='', isFashion=record.is_fashion, tags=record.tags))
        # time.sleep(1500)

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)




@never_cache
@api_view(['GET'])
def push_to_shopify(request):
    resp = {}
    resp['status'] = False
    push_products.delay('Data')
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)