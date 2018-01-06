# -*- coding: utf-8 -*-
import sys
from wsgiref import headers

import bs4
from celery import shared_task

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration
import requests
import time
from bs4 import BeautifulSoup
import string
import json

from models import Product
from SouqScrapperApp.tagsLookUps import getPriceTags, getColorTags, formatPrice
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
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.product_url = 'https://uae.souq.com/ae-en/search_results.php?action=quickView&is_unit=false&id={}'

    # Open Http connection
    def open_http_connection(self, call_url, page, headers=None):
        try:
            # print('Begin: Call URL -- {} '.format(call_url))
            time.sleep(5)
            scraped_html_page = requests.get(call_url, timeout=self.time_out,
                                             params=dict(page=page), headers=headers)
            # print('Finish: Call URL -- {} '.format(call_url))
            # Check response code
            if scraped_html_page.status_code == 200:
                return scraped_html_page.text
        except Exception as e:
            print('Error during call URL  {} cause {}'.format(call_url, str(e)))
            return None

    # parse page in soup
    def parsePageSoap(self, page):
        soup = BeautifulSoup(page, "html.parser")
        return soup

    # Retrieve Total Page Number
    def get_total_page(self, soup_page):
        total_tag = soup_page.find('li', attrs={'class': 'total'})
        if total_tag:
            extracted_number = int(filter(str.isdigit, str(total_tag.text)))
            return extracted_number
        return 1

    # Retrieve products
    def get_products_ids_from_page(self, soup_page):
        product_ids = []
        product_item_card_tags = soup_page.find_all('div', attrs={'class': 'single-item'})
        if product_item_card_tags:
            # its souq now
            for product_item in product_item_card_tags:
                href_tag = product_item.find('a', attrs={'class': 'quickViewAction'})
                if href_tag:
                    data_tem_id = href_tag['data-id']
                    if data_tem_id:
                        product_ids.append(data_tem_id)

        else:
            products_item_card_tags = soup_page.find_all('div', attrs={'class': 'block-grid-large'})
            if products_item_card_tags:
                for product_item in products_item_card_tags:
                    href_tag = product_item.find('a', attrs={'class': 'imgShowQuickView'})
                    data_tem_id = href_tag['data-item_id']
                    if data_tem_id:
                        product_ids.append(data_tem_id)

        return product_ids

    def get_product_details(self, id):
        page_html = self.open_http_connection(call_url=self.product_url.format(id), headers=self.headers, page=None)
        if page_html:
            product_json = json.loads(page_html)
            return product_json
        return None

    # Start Scrap

    def startScrappingProcessing(self, url, isFashion, collection, subCollection, tags):
        print('Begin: startScrappingProcessing -- {} '.format(url))
        url += self.list_all_item_attribute
        page_html = self.open_http_connection(call_url=url, page=1)
        if page_html:
            self.scrap_souq_results(page_html=page_html, url=url, tags=tags)

        print('End: startScrappingProcessing -- {} '.format(url))

    # Scrap search page result
    def scrap_souq_results(self, page_html, url, tags):
        soap_page = self.parsePageSoap(page=page_html)
        totalPage = self.get_total_page(soup_page=soap_page)
        if totalPage > 5:
            totalPage = 5

        self.parse_products_list(soup_page=soap_page, tags=tags)
        for page in range(2, totalPage, 1):
            page_html = self.open_http_connection(call_url=url, page=page)
            soap_page = self.parsePageSoap(page=page_html)
            self.parse_products_list(soup_page=soap_page, tags=tags)

    def parse_products_list(self, soup_page, tags):
        product_ids = self.get_products_ids_from_page(soup_page=soup_page)
        for id in product_ids:
            product_json = self.get_product_details(id=id)
            tags = ''
            tags += self.get_product_price_tags(product_json)
            tags += self.get_variants_tags(product_json)
            tags += self.get_brand_tags(product_json)
            product_json['tags'] = tags
            product_json['specs'] = self.get_other_specs(product_json)
            if product_json['manufacturer_en'] != 'Other' or product_json['manufacturer_en'] != 'other':
                saved = self.saveProduct(product=product_json)
                print('product scrapped {}   statues {}'.format(product_json['title'], saved))
                if saved:
                    # Integration
                    shopifyIntegrationInstance = ShopifyIntegration()
                    if saved.shopify_id:
                        shopifyIntegrationInstance.removeShopifyProduct(id=saved.shopify_id)

                    shopifyJson = shopifyIntegrationInstance.addNewProduct(productDict=product_json)
                    if shopifyJson:
                        # update product
                        shopifyIntegrationInstance.updateProduct(product=saved, shopifyJson=shopifyJson)

    def get_product_price_tags(self, product):
        current_price = formatPrice(product['price']['current_price'])
        old_price = formatPrice(product['price']['old_price'])
        if current_price < old_price:
            return getPriceTags(current_price)
        return getPriceTags(old_price)

    def get_variants_tags(self, product):
        tags = []
        if product['connections']:
            for k, v in (product['connections']).iteritems():
                for k1, v1 in (v['connectedValues']).iteritems():
                    tags.append(getColorTags(str(v1['value'])))
        return ','.join(tags)

    def get_brand_tags(self, product):
        tags = ''
        if product['manufacturer_en']:
            tags += ',{}'.format(str(product['manufacturer_en']))
        elif product['seller']['name']:
            tags += ',{}'.format(str(product['seller']['name']))
        return tags

    def get_other_specs(self, product):
        page_html = self.open_http_connection(call_url=str(product['url']), page=None)
        soap_page = self.parsePageSoap(page=page_html)
        specsTag = soap_page.find('div', attrs={'id': 'specs-full'})
        if specsTag:
            specs = (specsTag.contents)[1]
        else:
            specsTag = soap_page.find('div', attrs={'id': 'specs-short'})
            if specsTag:
                specs = (specsTag.contents)[1]
        return specs

    def saveProduct(self, product):
        try:
            record = Product()
            if Product.objects.filter(title=str(product['title'])).exists():
                record = Product.objects.filter(title=str(product['title']))[0]
            record.title = str(product['title'])
            record.description = str(product['description'])
            record.current_price = formatPrice(product['price']['current_price'])
            record.old_price = formatPrice(product['price']['old_price'])
            record.you_save = formatPrice(product['price']['you_save'])
            record.url = str(product['url'])
            record.images = str(product['images'])
            if product['connections']:
                record.connection_value = str(product['connections'])

            record.manufacturer_en = str(product['manufacturer_en'])
            record.brand = str(product['manufacturer_en']) if product['manufacturer_en'] else str(
                product['seller']['name'])
            record.tags = product['tags']
            record.other_specs = str(product['specs'])
            record.original_json = str(product)
            record.save()
            return record
        except Exception as e:

            print('Error during save proudct {}  cause {} '.format(product['title'], str(e)))
            return None
