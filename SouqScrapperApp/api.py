from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from SouqScrapperApp.SouqUAE import SouqUAEScrapper

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request):
    resp = {}
    resp['status'] = False

    try:
        scapper = SouqUAEScrapper()
        scapper.startScrappingProcessing(
            'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/round-neck/a-t-6356-6274-6503/s/', False,
            'Men`s T-Shirts', 'Round Neck')
        resp['status'] = True
    except Exception as e:
        resp['desc'] = str(e)

    return Response(resp)
