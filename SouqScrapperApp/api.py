from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks import *
from models import *
from ounass_scrapper import *
import time

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request):
    resp = {}
    resp['status'] = False
    querySet = Stores.objects.filter(store='Souq')
    # scapper = SouqUAEScrapper()
    for record in querySet:
            scrap.delay(url=record.url, collection='', subCollection='', isFashion=record.is_fashion, tags=record.tags)

    # scapper.startScrappingProcessing(
    #     url='https://fashion.souq.com/ae-en/watches-for-her/t/4012?q=eyJzIjoiYmVzdCIsImYiOnsibWFudWZhY3R1cmVyX2VuIjpbImFubmUga2xlaW4iLCJiYWxtYWluIiwiYmViZSIsImNhbHZpbiBrbGVpblx0IiwiY2FzaW8iLCJka255IiwiZm9zc2lsIiwiZ3VjY2kiLCJndWVzcyIsImp1aWN5IGNvdXR1cmUiLCJrYXRlIHNwYWRlIiwibWFyYyBieSBtYXJjIGphY29icyIsIm1hcmMgamFjb2JzIiwibWljaGFlbCBrb3JzIiwic2Vpa28iLCJzdGV2ZSBtYWRkZW4iLCJzd2Fyb3Zza2kiLCJ0aXNzb3QiLCJ0b21teSBoaWxmaWdlciIsInRveXdhdGNoIl19fQ%3D%3D',
    #     collection='',
    #     subCollection='',
    #     tags="UAE, Qatar, Bahrain, Oman, Kuwait, Saudi Arabia, Souq.com, Women's, Women's Accessories, Women's Watches",
    #     isFashion=True
    #
    # )

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)



@never_cache
@api_view(['GET'])
def fetchScrapperMissed(request,id):
    resp = {}
    resp['status'] = False
    record = Stores.objects.get(id=id)
    scrap.delay(url=record.url, collection='', subCollection='', isFashion=record.is_fashion, tags=record.tags)
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)


@never_cache
@api_view(['GET'])
def fetch_ounass_scrapper(request):
    resp = {}
    resp['status'] = False
    querySet = Stores.objects.filter(store='Ounaas')
    for store in querySet:
        scrap_ounaas.delay(url=store.url, tags=store.tags)

    # ounass_scrapper = OunassScrapper()
    # ounass_scrapper.startScrappingProcessing(url='https://www.ounass.ae/jewellery/fine-jewellery/rings/',tags='UAE, Ounaas, Womens, Womens Jewellery, Fine Jewellery, Womens Rings ')
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)