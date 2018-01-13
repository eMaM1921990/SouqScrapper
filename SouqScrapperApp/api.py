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
        url='https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/t--shirts/boohoo%7Cforever-21%7Carmani-jeans%7Cnike%7Cguess%7Cvero-moda%7Ckoovs%7Ckoton%7Cnew-look%7Cshein%7Cf--and--f%7Ctokyo-laundry%7Cpuma%7Csuperdry%7Cjuicy-couture%7Cmcq-by-alexander-mcqueen%7Cpepe-jeans%7Cthe-north-face%7Cgianfranco-ferre%7Cu.s.-polo-assn.%7Cmissguided%7Cfrench-connection%7Cpolice%7Chugo-boss%7Ctommy-hilfiger%7Cadidas-originals%7Clacoste%7Cmarie-claire/a-t-6356-6274-7/s/',
        collection='',
        subCollection='',
        tags="UAE, Qatar, Bahrain, Oman, Kuwait, Saudi Arabia, Souq.com, Women's, Women's Jewellery, Women's Rings",
        isFashion=True

    )

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)
