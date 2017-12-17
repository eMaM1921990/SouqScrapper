from __future__ import absolute_import


from celery import shared_task

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper


@shared_task
def scrapSOUQ(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(froms), int(tos)):
        urlDict = helper.urls_dict[index]
        scapper.startScrappingProcessing(
            url=urlDict[helper.url_key],
            isFashion=urlDict[helper.isFashion_key],
            collection=urlDict[helper.collection_key],
            subCollection=urlDict[helper.sub_collection_key],
            tags=urlDict[helper.tags_key])
