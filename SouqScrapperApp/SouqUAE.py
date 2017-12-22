# -*- coding: utf-8 -*-
import sys

import bs4

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration
import requests
import time
from bs4 import BeautifulSoup
import string
import json

from models import Product
from SouqScrapperApp.tagsLookUps import getPriceTags, getColorTags
import logging
logger = logging.getLogger(__name__)


reload(sys)
sys.setdefaultencoding('utf8')


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
            print('Begin: Call URL -- {} '.format(call_url))
            time.sleep(5)
            scraped_html_page = requests.get(call_url, timeout=self.time_out,
                                             params=dict(page=page))
            print('Finish: Call URL -- {} '.format(call_url))
            # Check response code
            if scraped_html_page.status_code == 200:
                return scraped_html_page.text
        except Exception as e:
            print('Error during call URL  {} cause {}'.format(call_url,str(e)))
            return None

    # parse page in soup
    def parsePageSoap(self, page):
        soup = BeautifulSoup(page, "html.parser")
        return soup

    # Start Scrap
    def startScrappingProcessing(self, url, isFashion, collection, subCollection, tags):
        print('Begin: startScrappingProcessing -- {} '.format(url))
        url += self.list_all_item_attribute
        scrappedPage = self.open_http_connection(call_url=url, page=1)
        if scrappedPage:
            if not isFashion:
                self.scrapSouqResults(page=scrappedPage, url=url, collection=collection,
                                      subCollection=subCollection, tags=tags)
            else:
                self.scrapFashionResults(page=scrappedPage, url=url, collection=collection,
                                         subCollection=subCollection, tags=tags)

        print('End: startScrappingProcessing -- {} '.format(url))

    # Scrap Fashion page result
    def scrapFashionResults(self, page, url, collection, subCollection, tags):
        jsonData = json.loads(str(page))
        totalPage = jsonData['metadata']['total_pages']
        self.parseProductsList(jsonData['data'], None, collection, subCollection, tags, isFashion=True)
        totalPage = 3
        for page in range(2, totalPage, 1):
            print('Fashion page -- {}'.format(str(page)))
            # url += self.list_all_item_attribute
            scrappedPage = self.open_http_connection(call_url=url, page=page)
            jsonData = json.loads(str(scrappedPage))
            self.parseProductsList(jsonData['data'], None, collection, subCollection, tags, isFashion=True)

    # Scrap search page result
    def scrapSouqResults(self, page, url, collection, subCollection, tags):
        resultData = self.retrieveSearchAsJson(page=page)
        commonTags = self.retrieveURLTags(page=page)
        # Calc total Page result
        totalPage = self.retrieveTotalPages(resultData['numberOfItems'])
        print('Find {} For {}  Pages for URL {} '.format(str(resultData['numberOfItems']),totalPage,url))
        self.parseProductsList(resultData['itemListElement'], commonTags, collection, subCollection, tags)
        totalPage = 3
        for page in range(2, totalPage, 1):

            print('SOUQ page -- {}'.format(str(page)))
            # url += self.list_all_item_attribute
            scrappedPage = self.open_http_connection(call_url=url, page=page)
            resultData = self.retrieveSearchAsJson(page=str(scrappedPage))
            self.parseProductsList(resultData['itemListElement'], commonTags, collection, subCollection, tags)

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

    def parseProductsList(self, items, commonTags, collection, subCollection, tags, isFashion=False):
        for item in items:
            print('scrap product {} '.format(str(item['name'])))
            product = self.retrieveProductDetails(url=item['url'], commonTags=commonTags, collection=collection,
                                                  subCollection=subCollection, otherTags=tags, isFashion=isFashion)
            saved = self.saveProduct(product=product, isFashion=isFashion)
            print('product scrapped {}   statues {}'.format(item['name'],saved))
            if saved:
                # Integration
                shopifyIntegrationInstance = ShopifyIntegration()
                if saved.shopify_id:
                    shopifyIntegrationInstance.removeShopifyProduct(id=saved.shopify_id)

                shopifyJson = shopifyIntegrationInstance.addNewProduct(productDict=product, isFashion=isFashion)
                if shopifyJson:
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

    def retrieveProductColors(self, soup):
        attrArry = []
        colors = soup.find(attrs={'class': 'colors-block'}).contents
        for index, color in enumerate(colors):
            if color.name == 'span' and color.has_attr('data-value'):
                attrArry.append(str(color['data-value']))
        return attrArry

    def retrieveProductDescAndColor(self, soup, product):
        body = soup.find('script', attrs={'type': 'application/ld+json'}).text
        resultData = json.loads(body)
        product['description'] = self.retrieveDescription(soup, resultData)
        if resultData['color']:
            product['color'] = str(resultData['color'])

        brand = str(resultData['brand']['name']).translate(
            string.maketrans("\n\t\r ", "    "))

        product['brand'] = brand
        # product['title'] = str(resultData['name']).translate(string.maketrans("\n\t\r ", "    ")).replace(' ', '')

    def retrieveDescription(self, soup, productJson):

        descriptionFullTag = soup.find('div', attrs={'id': 'description-full'})
        descriptionShortTag = soup.find('div', attrs={'id': 'description-short'})
        defaultDesc = str(productJson['description'].encode('utf-8').strip())

        if descriptionFullTag:
            desc = ''
            descriptionFullTagList = descriptionFullTag.contents
            for tag in descriptionFullTagList:
                if type(tag) is not bs4.element.NavigableString:
                    desc += str(tag)
            return desc

        elif descriptionShortTag:
            desc = ''
            descriptionShortTagList = descriptionShortTag.contents
            for tag in descriptionShortTagList:
                if type(tag) is not bs4.element.NavigableString:
                    desc += str(tag)
            return desc

        return defaultDesc

    def retrieveFashionVariant(self, soup, product):
        productExtra = soup.find_all('script', attrs={'type': 'text/javascript'})[5].text
        productExtra = productExtra.replace('var globalBucket =', '')
        productExtra = str(productExtra).translate(string.maketrans("\n\t\r ", "    ")).replace(' ', '')
        resultData = json.loads(productExtra)
        variants = resultData['Page_Data']['product']['variant']
        quantity = resultData['Page_Data']['product']['quantity']
        variantDict = {}
        variantDict['quantity'] = quantity
        variantDict['quantity'] = quantity
        for variant in str(variants).split(','):
            keys = variant.split(":")
            variantDict[keys[0]] = keys[1]

        return variantDict

    def getSizeQuantity(self, url, parsed_page):
        if url:
            page = self.open_http_connection(call_url=url, page=None)
            parsed_page = self.parsePageSoap(page=page)

        pageData = self.retrievePageData(parsed_page)
        return pageData['product']['quantity']

    def retrievePageData(self, page):
        body = page.find_all('script', attrs={'type': 'text/javascript'})[5].text
        body = body.replace('var globalBucket =', '')
        body = str(body).translate(string.maketrans("\n\t\r ", "    ")).replace(' ', '')
        resultData = json.loads(body)
        return resultData['Page_Data']

    def formatPrice(self, value):
        value = value.replace(self.currency, "")
        value = value.replace(",", '')
        value = value.replace(' ', '')
        value = float(value) * 0.272245
        # value = '%.1f' % round(value, 1)
        return value

    def getTagsFronsizes(self, sizeDict):
        sizeArr = []
        for size in sizeDict:
            sizeArr.append(size['name'])
        return sizeArr

    def retrieveProductDetails(self, url, commonTags, collection, subCollection, otherTags, isFashion=False):
        product_page_result = self.open_http_connection(call_url=url, page=None)

        if product_page_result:
            if not isFashion:
                return self.retrieveSouqProduct(product_page_result, commonTags, collection, subCollection, otherTags,
                                                isFashion, url)
            else:
                return self.retrieveFashionProduct(product_page_result, commonTags, collection, subCollection,
                                                   otherTags, isFashion, url)

    def retrieveSouqProduct(self, product_page_result, commonTags, collection, subCollection, otherTags, isFashion,
                            url):
        product = {}
        soup = self.parsePageSoap(page=product_page_result)
        # Retrieve Page Data


        pageData = self.retrievePageData(page=soup)

        productTitleTag = soup.find(attrs={'class': 'product-title'})
        product['title'] = str(productTitleTag.find('h1').text)

        product['collection'] = collection if collection else ''
        product['subCollection'] = subCollection if subCollection else ''
        product['url'] = str(url)
        product['images'] = self.retrieveProductImageBySize(soup)
        product['isFashion'] = isFashion

        # Price
        price = self.formatPrice(str(pageData['product']['price']))
        discountAmount = str(soup.find(attrs={'class': 'noWrap'}).text)
        discountAmount = self.formatPrice(discountAmount)
        compareAtPrice = float(price) + float(discountAmount)
        product['discountAmount'] = discountAmount
        product['compareAtPrice'] = compareAtPrice if discountAmount > 0  else None
        product['price'] = price

        # Get product color and description
        self.retrieveProductDescAndColor(soup=soup, product=product)

        sizes = soup.find_all(attrs={'class': "item-connection"})
        sizes_arr = []
        for index, size in enumerate(sizes):
            dictSize = {}
            dictSize['name'] = str(size.text).translate(string.maketrans("\n\t\r ", "    ")).replace(' ', '')
            dictSize['quantity'] = self.getSizeQuantity(url=None, parsed_page=soup)
            #if index == 0:
            #    dictSize['quantity'] = self.getSizeQuantity(url=None, parsed_page=soup)
            #else:
            #    hrefTag = size.find('a')
            #    dictSize['quantity'] = self.getSizeQuantity(url=str(hrefTag['data-url']), parsed_page=soup)
            sizes_arr.append(dictSize)

        # Crap Variant
        product['variants'] = {}
        if not isFashion:
            product['variants']['size'] = sizes_arr
            product['variants']['colors'] = product['color']
        else:
            product['variants'] = self.retrieveFashionVariant(soup, product)

        # Get other specs
        product['specs'] = (soup.find('div', attrs={'id': 'specs-full'}).contents)[1]

        # Tags
        tags = []

        # add other tags
        if otherTags:
            tags.append(otherTags)

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

    def retrieveFashionProduct(self, product_page_result, commonTags, collection, subCollection, otherTags, isFashion,
                               url):
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

        # Get product color and description
        self.retrieveProductDescAndColor(soup=soup, product=product)

        # Get other specs
        product['specs'] = (soup.find('div', attrs={'id': 'specs-full'}).contents)[1]

        product['title'] = title
        product['discountAmount'] = discountAmount
        product['compareAtPrice'] = compareAtPrice if discountAmount > 0  else 0
        product['price'] = price

        product['collection'] = collection if collection else ''
        product['subCollection'] = subCollection if subCollection else ''
        product['url'] = str(url)
        product['images'] = self.retrieveProductImageBySize(soup)
        product['isFashion'] = isFashion
        product['variants'] = {}

        variants = self.retrieveFashionVariant(soup, product)
        product['variants']['DialColor'] = variants['DialColor']
        product['variants']['BandColor'] = variants['BandColor']
        product['quantity'] = variants['quantity']

        tags = []

        # add other tags
        if otherTags:
            tags.append(otherTags)

        # Get Product tags
        tags.append(getPriceTags(price=compareAtPrice))
        # Get Color Tags

        tags.append(getColorTags(tag=variants['DialColor']))

        tags.append(getColorTags(tag=variants['BandColor']))
        # Get Brand Tags
        tags.append(product['brand'])
        # Get Collection tags
        tags.append(product['collection'])

        product['tags'] = tags
        # print product
        return product

    def saveProduct(self, product, isFashion):
        try:
            record = Product()
            if Product.objects.filter(title=product['title']).exists():
                record = Product.objects.filter(title=product['title'])[0]
            record.title = product['title']
            record.sub_collection = product['subCollection']
            record.collection = product['collection']
            record.description = product['description']
            record.compare_at_Price = product['compareAtPrice']
            record.price = product['price']
            record.discount_amount = product['discountAmount']
            record.url = product['url']
            if not isFashion:
                record.color = product['color']
            else:
                record.color = product['variants']['DialColor'] + ',' + product['variants']['BandColor']
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

            if not isFashion:
                record.variant_option_one = product['color']
            else:
                record.variant_option_one = product['variants']['DialColor']

            if not isFashion:
                size_option = []
                for size in product['variants']['size']:
                    size_option.append(size['name'])

                record.variant_option_two = ','.join(size_option)
            else:
                record.variant_option_two = product['variants']['BandColor']

            record.brand = str(product['brand'])
            record.tags = ','.join(product['tags'])
            record.other_specs = str(product['specs'])
            record.save()
            return record
        except Exception as e:

            print('Error during save proudct {}  cause {} '.format(product['title'],str(e)))
            return None
