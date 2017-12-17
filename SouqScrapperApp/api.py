from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks import *

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request, froms, tos):
    resp = {}
    resp['status'] = False
    scrapSOUQ.delay(froms, tos)
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)

