#!/Users/mac/.virtualenvs/souqEnv/bin
import os
import sys
import django

from SouqScrapperApp.SouqHelper import SouqHelper
from SouqScrapperApp.SouqUAE import SouqUAEScrapper

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'SouqScrapper/')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'SouqScrapper/SouqScrapper/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()


class CustomScraper(object):
    def __init__(self):
        self.url = ""

    def scrape(self):
        print 'scraping...'

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


if __name__ == '__main__':
    scraper = CustomScraper()
    scraper.scrapSOUQ()
