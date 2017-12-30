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
    # querySet = Stores.objects.filter(store='Souq')
    #
    # for record in querySet:
    #     scrap.delay(url=record.url, collection='',
    #                 subCollection='',
    #                 isFashion=record.is_fashion, tags=record.tags)

    scapper = SouqUAEScrapper()
    scapper.startScrappingProcessing(
            url='https://uae.souq.com/ae-en/women-rings/rings-284/women/swarovski%7Cmichael-kors%7Cvera-perla%7Cpandora%7Cemporio-armani%7Ckate-spade%7Caldo%7Ccalvin-klein-jewelry%7Cpierre-cardin%7Ccalvin-klein%7Cjuicy-couture/a-t-1780-7/s/?sortby=sr&page=1com/ae-en/women-rings/rings-284/women/swarovski%7Cmichael-kors%7Cvera-perla%7Cpandora%7Cemporio-armani/a-t-1780-7/s/',
        collection='',
        subCollection='',
        tags="Middle East, Souq.com, Women's, Women's Jewellery, Women's Rings",
        isFashion=False

    )

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)
