from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks import *

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request, froms, to):
    resp = {}
    resp['status'] = False
    scrapFirstQuarter.delay(0, 25)
    scrapSecondQuarter.delay(25,50)
    scrapThirdQuarter.delay(51,75)
    scrapForthQuarter.delay(76,100)
    scrapFiveQuarter.delay(101,125)
    scrapSixQuarter.delay(126,150)
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)

