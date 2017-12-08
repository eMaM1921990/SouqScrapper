from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request):
    resp = {}
    resp['status'] = False
    scapper = SouqUAEScrapper()
    souqHelper = SouqHelper()
    urlDict = souqHelper.urls_dict[0]

    scapper.startScrappingProcessing(
        url=urlDict[souqHelper.url_key],
        isFashion=urlDict[souqHelper.isFashion_key],
        collection=urlDict[souqHelper.collection_key],
        subCollection=urlDict[souqHelper.sub_collection_key],
        tags=urlDict[souqHelper.tags_key])
    resp['status'] = True
    resp['desc'] = str(e)
    return Response(resp)
