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
        url='https://fashion.souq.com/ae-en/search?campaign_id=3797&tag_id=4012&filters%5Bmanufacturer_en%5D%5B%5D=anne+klein&filters%5Bmanufacturer_en%5D%5B%5D=guess&filters%5Bmanufacturer_en%5D%5B%5D=casio&filters%5Bmanufacturer_en%5D%5B%5D=fossil&filters%5Bmanufacturer_en%5D%5B%5D=michael+kors&filters%5Bmanufacturer_en%5D%5B%5D=bebe&filters%5Bmanufacturer_en%5D%5B%5D=swarovski&filters%5Bmanufacturer_en%5D%5B%5D=marc+jacobs&filters%5Bmanufacturer_en%5D%5B%5D=calvin+klein%09&filters%5Bmanufacturer_en%5D%5B%5D=dkny&filters%5Bmanufacturer_en%5D%5B%5D=balmain&filters%5Bmanufacturer_en%5D%5B%5D=tissot&filters%5Bmanufacturer_en%5D%5B%5D=tommy+hilfiger&filters%5Bmanufacturer_en%5D%5B%5D=gucci&filters%5Bmanufacturer_en%5D%5B%5D=toywatch&filters%5Bmanufacturer_en%5D%5B%5D=kate+spade&filters%5Bmanufacturer_en%5D%5B%5D=seiko&filters%5Bmanufacturer_en%5D%5B%5D=marc+by+marc+jacobs&filters%5Bmanufacturer_en%5D%5B%5D=steve+madden&filters%5Bmanufacturer_en%5D%5B%5D=juicy+couture',
        collection='',
        subCollection='',
        tags="Middle East, Souq.com, Women's, Women's Jewellery, Women's Rings",
        isFashion=True

    )

    resp['status'] = True
    resp['desc'] = "Shopify will be update once this process done"
    return Response(resp)
