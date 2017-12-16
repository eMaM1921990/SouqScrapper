from celery.task import task

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper

__author__ = 'eMaM'

@task
def scrapSOUQ():
    scapper = SouqUAEScrapper()
    souqHelper = SouqHelper()
    for dict in souqHelper.urls_dict:
        urlDict = dict
        scapper.startScrappingProcessing(
            url=urlDict[souqHelper.url_key],
            isFashion=urlDict[souqHelper.isFashion_key],
            collection=urlDict[souqHelper.collection_key],
            subCollection=urlDict[souqHelper.sub_collection_key],
            tags=urlDict[souqHelper.tags_key])
