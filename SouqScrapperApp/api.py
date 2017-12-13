from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper

__author__ = 'eMaM'


@never_cache
@api_view(['GET'])
def fetchScrapper(request, froms , tos):
    resp = {}
    resp['status'] = False
    scapper = SouqUAEScrapper()
    souqHelper = SouqHelper()
    for index in range(int(froms),int(tos),1):
        urlDict = souqHelper.urls_dict[index]
        scapper.startScrappingProcessing(
            url=urlDict[souqHelper.url_key],
            isFashion=urlDict[souqHelper.isFashion_key],
            collection=urlDict[souqHelper.collection_key],
            subCollection=urlDict[souqHelper.sub_collection_key],
            tags=urlDict[souqHelper.tags_key])
    resp['status'] = True
    return Response(resp)
