from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks import *

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request):
    resp = {}
    resp['status'] = False
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for url in helper.urls_dict:
        scrap.delay(url=url[helper.url_key], collection=url[helper.collection_key],
                    subCollection=url[helper.sub_collection_key],
                    isFashion=url[helper.isFashion_key], tags=url[helper.tags_key])

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)
