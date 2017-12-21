from __future__ import absolute_import

from celery import task
from celery.backends.database import retry

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper


@task(bind=True, soft_time_limit=60 * 60 * 24, time_limit=60 * 60 * 24, default_retry_delay=300, max_retries=5)
def scrapFirstQuarterSouq(input):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(0), int(25)):
        urlDict = helper.urls_dict[index]
        try:
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])

        except Exception as e:
            print("maybe do some clenup here....")
            retry(e)


@task(bind=True, soft_time_limit=60 * 60 * 24, time_limit=60 * 60 * 24, default_retry_delay=300, max_retries=5)
def scrapSecondQuarterSouq(input):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(26), int(50)):
        urlDict = helper.urls_dict[index]
        try:
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])

        except Exception as e:
            print("maybe do some clenup here....")
            retry(e)


@task(bind=True, soft_time_limit=60 * 60 * 24, time_limit=60 * 60 * 24, default_retry_delay=300, max_retries=5)
def scrapThirdQuarterSouq(input):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(51), int(75)):
        urlDict = helper.urls_dict[index]
        try:
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])

        except Exception as e:
            print("maybe do some clenup here....")
            retry(e)


@task(bind=True, soft_time_limit=60 * 60 * 24, time_limit=60 * 60 * 24, default_retry_delay=300, max_retries=5)
def scrapFourthQuarterSouq(input):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(76), int(100)):
        urlDict = helper.urls_dict[index]
        try:
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])

        except Exception as e:
            print("maybe do some clenup here....")
            retry(e)


@task(bind=True, soft_time_limit=60 * 60 * 24, time_limit=60 * 60 * 24, default_retry_delay=300, max_retries=5)
def scrapFiveQuarterSouq(input):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(101), int(125)):
        urlDict = helper.urls_dict[index]
        try:
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])

        except Exception as e:
            print("maybe do some clenup here....")
            retry(e)


@task(bind=True, soft_time_limit=60 * 60 * 24, time_limit=60 * 60 * 24, default_retry_delay=300, max_retries=5)
def scrapSixQuarterSouq(input):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    for index in range(int(126), int(150)):
        urlDict = helper.urls_dict[index]
        try:
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])

        except Exception as e:
            print("maybe do some clenup here....")
            retry(e)
