# -*- coding: utf-8 -*-
import sys

import stringcase
from django.core.exceptions import ObjectDoesNotExist

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration

reload(sys)
sys.setdefaultencoding('utf8')

import requests
import time
from bs4 import BeautifulSoup
import string
import json

from django.conf import settings

from models import Product
from SouqScrapperApp.tagsLookUps import getPriceTags, getColorTags

__author__ = 'eMaM'


class SouqUAEScrapper():
    def __init__(self):
        self.item_per_page = 60
        self.list_all_item_attribute = '?section=2'
        self.time_out = None
        self.time_wait = 5
        self.currency = 'AED'

    # Open Http connection
    def open_http_connection(self, call_url, page):
        try:
            print 'parsing url ' + call_url
            time.sleep(10)
            scraped_html_page = requests.get(call_url, timeout=self.time_out,
                                             params=dict(page=page))
            print 'parsing url end ' + call_url
            # Check response code
            if scraped_html_page.status_code == 200:
                return scraped_html_page.text
        except Exception as e:
            print str(e)
            return None

    # parse page in soup
    def parsePageSoap(self, page):
        soup = BeautifulSoup(page, "html.parser")
        return soup

    # Start Scrap
    def startScrappingProcessing(self, url, isFashion, collection, subCollection):
        print 'Enter startScrappingProcessing'
        url += self.list_all_item_attribute
        scrappedPage = self.open_http_connection(call_url=url, page=1)
        if scrappedPage:
            if not isFashion:
                self.scrapSouqResults(page=scrappedPage, url=url, collection=collection,
                                      subCollection=subCollection)
            else:
                self.scrapFashionResults(page=scrappedPage, url=url, collection=collection,
                                         subCollection=subCollection)

        print 'Exit startScrappingProcessing'

    # Scrap Fashion page result
    def scrapFashionResults(self, page, url, collection, subCollection):
        jsonData = json.loads(str(page))
        totalPage = jsonData['metadata']['total_pages']
        self.parseProductsList(jsonData['data'], None, collection, subCollection)
        for page in range(2, totalPage, 1):
            # url += self.list_all_item_attribute
            scrappedPage = self.open_http_connection(call_url=url, page=page)
            jsonData = json.loads(scrappedPage)
            self.parseProductsList(jsonData['data'], None, collection, subCollection)

    # Scrap search page result
    def scrapSouqResults(self, page, url, collection, subCollection):
        resultData = self.retrieveSearchAsJson(page=page)
        commonTags = self.retrieveURLTags(page=page)
        # Calc total Page result
        totalPage = self.retrieveTotalPages(resultData['numberOfItems'])
        self.parseProductsList(resultData['itemListElement'], commonTags, collection, subCollection)

        for page in range(2, totalPage, 1):
            # url += self.list_all_item_attribute
            scrappedPage = self.open_http_connection(call_url=url, page=page)
            resultData = self.retrieveSearchAsJson(page=scrappedPage)
            self.parseProductsList(resultData['itemListElement'], commonTags, collection, subCollection)

    def retrieveTotalPages(self, numberOfItems):
        result = float(numberOfItems) / self.item_per_page
        if not result.is_integer():
            result = int(result) + 1
        return int(result)

    def retrieveURLTags(self, page):
        soup = self.parsePageSoap(page=page)
        ulTags = soup.find('ul', attrs={'class': 'refienments-selected'}).contents
        tags = []
        for index, liTag in enumerate(ulTags):
            if liTag.name == 'li':
                tags.append(str(liTag.find('a')['data-name']))
        if len(tags) > 0:
            del tags[len(tags) - 1]
        return tags

    def retrieveSearchAsJson(self, page):
        soup = self.parsePageSoap(page=page)
        body = soup.find('script', attrs={'type': 'application/ld+json'}).text
        resultData = json.loads(body)

        return resultData

    def parseProductsList(self, items, commonTags, collection, subCollection):
        for item in items:
            product = self.retrieveProductDetails(url=item['url'], commonTags=commonTags, collection=collection,
                                                  subCollection=subCollection)
            saved = self.saveProduct(product=product)
            if saved:
                # Integration
                shopifyIntegrationInstance = ShopifyIntegration()
                if saved.shopify_id:
                    shopifyIntegrationInstance.removeShopifyProduct(id=saved.shopify_id)

                shopifyJson = shopifyIntegrationInstance.addNewProduct(productDict=product)
                # update product
                shopifyIntegrationInstance.updateProduct(product=saved, shopifyJson=shopifyJson)

    def retrieveProductImageBySize(self, soup):
        attr = []
        images = soup.find_all(attrs={'class': 'slide'})
        for imageTag in images:
            if imageTag.has_attr('data-thumb'):
                url = str(imageTag['data-thumb'])
                attr.append(url)

        return attr

    def retrieveProductColorsBySize(self, soup):
        attrArry = []
        colors = soup.find(attrs={'class': 'colors-block'}).contents
        for index, color in enumerate(colors):
            if color.name == 'span' and color.has_attr('data-value'):
                attrArry.append(str(color['data-value']))
        return attrArry

    def retrieveProductDescColor(self, soup, product):
        body = soup.find('script', attrs={'type': 'application/ld+json'}).text
        resultData = json.loads(body)
        product['description'] = self.retrieveDescription(soup, resultData)
        if resultData['color']:
            product['color'] = str(resultData['color'])

        brand = str(resultData['brand']['name']).translate(
            string.maketrans("\n\t\r ", "    ")).replace(' ', '')

        product['brand'] = stringcase.sentencecase(brand)

    def retrieveDescription(self, soup, productJson):
        desc = soup.find('div', attrs={'id': 'description-full'})
        if desc:
            desc = desc.text
        if not desc:
            desc = soup.find('div', attrs={'id': 'description-short'}).text
            if desc:
                desc = desc.text
            if not desc:
                desc = str(productJson['description'].encode('utf-8').strip())
        return desc

    def retrieveFashionVariant(self, soup, product):
        productVariant = soup.find('div', attrs={'id': 'productTrackingParams'})
        variants = productVariant['data-variant']
        variantDict = {}
        for variant in str(variants).split(','):
            keys = variant.spilt(":")
            variantDict[keys[0]] = keys[1]

        return variantDict

    def getSizeQuantity(self, url, parsed_page):
        if url:
            page = self.open_http_connection(call_url=url, page=None)
            parsed_page = self.parsePageSoap(page=page)
        return self.extractSizeAvailbleQuantity(parsed_page)

    def extractSizeAvailbleQuantity(self, page):
        body = page.find_all('script', attrs={'type': 'text/javascript'})[5].text
        body = body.replace('var globalBucket =', '')
        body = str(body).translate(string.maketrans("\n\t\r ", "    ")).replace(' ', '')
        resultData = json.loads(body)
        return resultData['Page_Data']['product']['quantity']

    def formatPrice(self, value):
        value = value.replace(self.currency, "")
        value = value.replace(",", '')
        value = value.replace(' ', '')
        value = float(value) * 0.272294
        value = '%.1f' % round(value, 1)
        return value

    def getTagsFronsizes(self, sizeDict):
        sizeArr = []
        for size in sizeDict:
            sizeArr.append(size['name'])
        return sizeArr

    def retrieveProductDetails(self, url, commonTags, collection, subCollection):
        product_page_result = self.open_http_connection(call_url=url, page=None)

        if product_page_result:
            product = {}
            soup = self.parsePageSoap(page=product_page_result)
            productTitleTag = soup.find(attrs={'class': 'product-title'})
            title = str(productTitleTag.find('h1').text)

            compareAtPrice = str(soup.find(attrs={'class': 'price'}).text).translate(
                string.maketrans("\n\t\r ", "    ")).replace(' ', '')
            compareAtPrice = self.formatPrice(compareAtPrice)

            discountAmount = str(soup.find(attrs={'class': 'noWrap'}).text)
            discountAmount = self.formatPrice(discountAmount)

            price = float(compareAtPrice) + float(discountAmount)
            sizes = soup.find_all(attrs={'class': "item-connection"})
            sizes_arr = []
            for index, size in enumerate(sizes):
                dictSize = {}
                dictSize['name'] = str(size.text).translate(string.maketrans("\n\t\r ", "    ")).replace(' ', '')
                if index == 0:
                    dictSize['quantity'] = self.getSizeQuantity(url=None, parsed_page=soup)
                else:
                    hrefTag = size.find('a')
                    dictSize['quantity'] = self.getSizeQuantity(url=str(hrefTag['data-url']), parsed_page=soup)
                sizes_arr.append(dictSize)

            # Get product color and description
            self.retrieveProductDescColor(soup=soup, product=product)

            product['title'] = title
            product['discountAmount'] = discountAmount
            product['compareAtPrice'] = compareAtPrice
            product['price'] = price

            product['collection'] = collection if collection else ''
            product['subCollection'] = subCollection if subCollection else ''
            product['url'] = str(url)
            product['images'] = self.retrieveProductImageBySize(soup)
            product['variants'] = {}
            if 'color' in product:
                product['variants']['size'] = sizes_arr
                product['variants']['colors'] = product['color']
            else:
                product['variants'] = self.retrieveFashionVariant(soup, product)

            tags = []
            # Get Product tags
            tags.append(getPriceTags(price=compareAtPrice))
            # Get Color Tags
            if product['color']:
                tags.append(getColorTags(tag=product['color']))
            # Get Brand Tags
            tags.append(product['brand'])
            # Get Collection tags
            tags.append(product['collection'])

            product['tags'] = tags + commonTags + self.getTagsFronsizes(sizes_arr)
            # print product
            return product

    def saveProduct(self, product):
        try:
            try:
                record = Product.objects.get(title=product['title'])
            except ObjectDoesNotExist as e:
                print str(e)
                record = Product()

            record.title = product['title']
            record.sub_collection = product['subCollection']
            record.collection = product['collection']
            record.description = product['description']
            record.compare_at_Price = product['compareAtPrice']
            record.price = product['price']
            record.discount_amount = product['discountAmount']
            record.url = product['url']
            record.color = product['color']
            try:
                record.image_1 = product['images'][0]
            except Exception as e:
                record.image_1 = None

            try:
                record.image_2 = product['images'][1]
            except Exception as e:
                record.image_2 = None

            try:
                record.image_3 = product['images'][2]
            except Exception as e:
                record.image_3 = None

            try:
                record.image_4 = product['images'][3]
            except Exception as e:
                record.image_4 = None

            try:
                record.image_5 = product['images'][5]
            except Exception as e:
                record.image_5 = None
            record.variant_option_one = product['color']
            size_option = []
            for size in product['variants']['size']:
                size_option.append(size['name'])

            record.variant_option_two = ','.join(size_option)
            record.brand = str(product['brand'])
            record.tags = ','.join(product['tags'])
            record.save()
            return record
        except Exception as e:
            print str(e)
            return None
