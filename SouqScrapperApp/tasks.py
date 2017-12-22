from __future__ import absolute_import

from celery import shared_task

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper


def ServiceTemporarilyDownError(object):
    raise Exception('This is not handled!')


@shared_task(max_retries=10)
def scrapFirstQuarter(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    try:
        for index in range(int(froms), int(tos)):
            urlDict = helper.urls_dict[index]
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])
    except ServiceTemporarilyDownError:
        raise scrapFirstQuarter.retry()

    return True


@shared_task(max_retries=10)
def scrapSecondQuarter(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    try:
        for index in range(int(froms), int(tos)):
            urlDict = helper.urls_dict[index]
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])
    except ServiceTemporarilyDownError:
        raise scrapSecondQuarter.retry()
    return True


@shared_task(max_retries=10)
def scrapThirdQuarter(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    try:
        for index in range(int(froms), int(tos)):
            urlDict = helper.urls_dict[index]
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])
    except ServiceTemporarilyDownError:
        raise scrapThirdQuarter.retry()
    return True


@shared_task(max_retries=10)
def scrapForthQuarter(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    try:
        for index in range(int(froms), int(tos)):
            urlDict = helper.urls_dict[index]
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])
    except ServiceTemporarilyDownError:
        raise scrapForthQuarter.retry()
    return True


@shared_task(max_retries=10)
def scrapFiveQuarter(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    try:
        for index in range(int(froms), int(tos)):
            urlDict = helper.urls_dict[index]
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])
    except ServiceTemporarilyDownError:
        raise scrapFiveQuarter.retry()
    return True


@shared_task(max_retries=10)
def scrapSixQuarter(froms, tos):
    scapper = SouqUAEScrapper()
    helper = SouqHelper()
    try:
        for index in range(int(froms), int(tos)):
            urlDict = helper.urls_dict[index]
            scapper.startScrappingProcessing(
                url=urlDict[helper.url_key],
                isFashion=urlDict[helper.isFashion_key],
                collection=urlDict[helper.collection_key],
                subCollection=urlDict[helper.sub_collection_key],
                tags=urlDict[helper.tags_key])
    except ServiceTemporarilyDownError:
        raise scrapSixQuarter.retry()
    return True
