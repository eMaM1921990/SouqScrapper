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
    scrapFirstQuarterSouq.delay()
    scrapSecondQuarterSouq.delay()
    scrapThirdQuarterSouq.delay()
    scrapFourthQuarterSouq.delay()
    scrapFiveQuarterSouq.delay()
    scrapSixQuarterSouq.delay()
    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)

