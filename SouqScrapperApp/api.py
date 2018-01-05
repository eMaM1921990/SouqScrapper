from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks import *
from models import *

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request):
    resp = {}
    resp['status'] = False
    querySet = Stores.objects.filter(store='Souq')

    for record in querySet:
        scrap.delay(url=record.url, collection='',
                    subCollection='',
                    isFashion=record.is_fashion, tags=record.tags)

    # scapper = SouqUAEScrapper()
    # scapper.startScrappingProcessing(
    #     url='https://fashion.souq.com/ae-en/watches-for-her/t/4012?q=eyJzIjoiYmVzdCIsImYiOnsibWFudWZhY3R1cmVyX2VuIjpbImFubmUga2xlaW4iLCJiYWxtYWluIiwiYmViZSIsImNhbHZpbiBrbGVpblx0IiwiY2FzaW8iLCJka255IiwiZm9zc2lsIiwiZ3VjY2kiLCJndWVzcyIsImp1aWN5IGNvdXR1cmUiLCJrYXRlIHNwYWRlIiwibWFyYyBieSBtYXJjIGphY29icyIsIm1hcmMgamFjb2JzIiwibWljaGFlbCBrb3JzIiwic2Vpa28iLCJzdGV2ZSBtYWRkZW4iLCJzd2Fyb3Zza2kiLCJ0aXNzb3QiLCJ0b21teSBoaWxmaWdlciIsInRveXdhdGNoIl19fQ%3D%3D',
    #     collection='',
    #     subCollection='',
    #     tags="UAE, Qatar, Bahrain, Oman, Kuwait, Saudi Arabia, Souq.com, Women's, Women's Jewellery, Women's Rings",
    #     isFashion=True
    #
    # )

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)
