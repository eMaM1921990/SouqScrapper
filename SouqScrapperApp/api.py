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
            'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImNhc3VhbCB3YXRjaCJdfX0%3D', True,
            'Men`s T-Shirts', 'Round Neck')
        resp['status'] = True
    except Exception as e:
        print str(e)
        resp['desc'] = str(e)

    return Response(resp)
