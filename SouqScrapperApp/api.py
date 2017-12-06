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
        urlDict = scapper.urls_dict[0]
        scapper.startScrappingProcessing(
            urlDict[scapper.url_key], urlDict[scapper.isFashion_key],
            urlDict[scapper.collection_key], urlDict[scapper.sub_collection_key])
        resp['status'] = True
    except Exception as e:
        resp['desc'] = str(e)

    return Response(resp)
