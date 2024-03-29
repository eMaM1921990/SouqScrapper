# -*- coding: utf-8 -*-
import json
import time

import requests
from bs4 import BeautifulSoup

from SouqScrapperApp.ShopifyAPI import ShopifyIntegration
from SouqScrapperApp.models import Product
from SouqScrapperApp.utils import formatPrice, getColorTags, getPriceTags, normalizeBrand

__author__ = 'eMaM'


class OunassScrapper():
    def __init__(self):
        self.time_out = None
        self.time_wait = 5
        self.currency = 'AED'
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.product_url = 'https://www.ounass.ae{}'
        self.product_image_url = 'https:{}'
        self.affiliate_url = 'https://tayer.ae/?a=362&c=326&p=r&s1=&ckmrdr={}'

    def startScrappingProcessing(self, url, tags):
        print('[Ounass] start Scrapping Processing -- {} '.format(url))
        page_html = self.open_http_connection(call_url=url, page=0)
        if page_html:
            self.retrieve_result(page_html=page_html, url=url, tags=tags)

        print('[Ounass]  end Scrapping Processing -- {} '.format(url))

    # Open Http connection
    def open_http_connection(self, call_url, page, headers=None):
        try:
            # print('Begin: Call URL -- {} '.format(call_url))
            time.sleep(self.time_wait)
            scraped_html_page = requests.get(call_url, timeout=self.time_out,
                                             params=dict(p=page), headers=headers)
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
        div_tag = soup_page.find('div', attrs={'class': 'pagination-wrapper'})
        if div_tag:
            href_tag = div_tag.find('a')
            pagination_json = json.loads(href_tag['data-pagination'])
            return pagination_json['totalPages']
        return 1

    # Retrieve products list
    def retrieve_result(self, page_html, url, tags):
        soap_page = self.parsePageSoap(page=page_html)
        totalPage = self.get_total_page(soup_page=soap_page)
        if totalPage > 8:
            totalPage = 8

        self.parse_products(soup_page=soap_page, tags=tags)

        for page in range(2, totalPage, 1):
            page_html = self.open_http_connection(call_url=url, page=page)
            soap_page = self.parsePageSoap(page=page_html)
            self.parse_products(soup_page=soap_page, tags=tags)

    # Parse Retrieve Products
    def parse_products(self, soup_page, tags):
        product_items_div_tag = soup_page.find_all('div', attrs={'class': 'product-item-wrapper'})
        if product_items_div_tag:
            for product_item_tag in product_items_div_tag:
                # build product structure
                product = self.build_product_info(product_item_tag=product_item_tag, tags=tags)
                # save product to database
                saved_product = self.saveProduct(product=product)

                if saved_product:
                    # Build shopify structure
                    product_shopify = self.build_product_for_shopify(product=product)

                    if product_shopify:
                        shopifyIntegrationInstance = ShopifyIntegration()

                        # check if call is UPDATE or ADD
                        if saved_product.shopify_id:

                            # Update exist product
                            shopifyIntegrationInstance.update_product_at_shopify(product=product_shopify,
                                                                                 id=saved_product.shopify_id)
                        else:

                            # Add new producr
                            shopifyJson = shopifyIntegrationInstance.add_product_to_shopify(products=product_shopify)

                            if shopifyJson:
                                # update product
                                shopifyIntegrationInstance.updateProduct(product=saved_product, shopifyJson=shopifyJson)

    # Build Product
    def build_product_info(self, product_item_tag, tags):
        product = {}
        href_tag = product_item_tag.find('a')
        product['url'] = self.product_url.format(str(href_tag['href']))

        # product title
        product['title'] = str(href_tag['data-name'])
        product['brand'] = normalizeBrand(str(href_tag['data-brand']))

        # product price
        product['price'] = formatPrice(int(href_tag['data-price']))
        product['compare_price'] = formatPrice(
            str(href_tag['data-original_price']) if href_tag['data-original_price'] else 0)

        # product color
        product['color'] = str(href_tag['data-variant']) if href_tag['data-variant'] else None

        # product size
        product_size_arr = []
        sizes_tags = href_tag.find('ul', attrs={'class': 'sizes'})
        if sizes_tags:
            sizes_li = sizes_tags.contents
            for size in sizes_li:
                if size.name == 'li':
                    product_size_arr.append(str(size.text))

        product['sizes'] = product_size_arr

        # Get Deep Info

        self.get_deep_product_info(product=product, url=product['url'])

        # Tags
        product['tags'] = tags

        # Color Tags
        if product['color']:
            product['tags'] += ',' + getColorTags(product['color'])

        # Price Tag
        product['tags'] += self.get_product_price_tags(product=product)

        # Brand Tags
        if product['brand']:
            product['tags'] += product['brand']+','

        # Size Tags
        if len(product['sizes']) > 0:
            product['tags'] += ','.join(product['sizes'])

        return product

    # Get Deep product info
    def get_deep_product_info(self, product, url):
        page_html = self.open_http_connection(call_url=url, page=None)
        soap_page = self.parsePageSoap(page=page_html)

        # Add product image
        product['images'] = self.get_product_images(soap_page=soap_page)
        # Add Desc
        product['desc'] = self.get_description(soap_page=soap_page)

    # Get product Images
    def get_product_images(self, soap_page):
        images_arr = []
        figures_tag = soap_page.find_all('figure', attrs={'class': 'media_image'})
        if figures_tag:
            for figure in figures_tag:
                href_tag = figure.find('a')
                if href_tag:
                    images_arr.append(self.product_image_url.format(str(href_tag['href'])))

        return images_arr

    # Get Other Info
    def get_description(self, soap_page):
        desc_html = ''
        accordion_tag = soap_page.find('div', attrs={'class': 'product-information-tabs'})
        if accordion_tag:

            # Editor's Advice
            decs_tag = accordion_tag.find('div', attrs={'class': 'product-information-tabs-description'})
            if decs_tag:
                desc_html += "<h5> Editor's Advice</h5>"
                desc_html += decs_tag.text

            # Size And Fit
            size_fit_tag = accordion_tag.find('div', attrs={'class': 'product-information-tabs-sizeAndFit'})
            if size_fit_tag:
                desc_html += "<p> </p><h5> Size And Fit</h5>"
                for size in size_fit_tag.contents:
                    if size.name == 'p':
                        desc_html += '<p>'+size.text+'</p>'


            # Design Details
            design_tag = accordion_tag.find('div', attrs={'class': 'product-information-tabs-designDetails'})
            if design_tag:
                desc_html += "<p> </p><h5> Design Details</h5>"
                for desgin in design_tag.contents:
                    if desgin.name == 'p':
                        desc_html += '<p>'+desgin.text+'</p>'

        return desc_html

    # Get Price Tag
    def get_product_price_tags(self, product):
        current_price = product['price']
        old_price = product['compare_price']
        if old_price == 0:
            old_price = current_price

        if current_price < old_price:
            return getPriceTags(current_price)
        return getPriceTags(old_price)

    # Save Product
    def saveProduct(self, product):
        try:
            record = Product()
            if Product.objects.filter(title=str(product['title'])).exists():
                record = Product.objects.filter(title=str(product['title']))[0]
            record.title = str(product['title'])
            record.description = product['desc']
            record.current_price = product['price']
            record.old_price = product['compare_price']
            record.you_save = 0 if product['compare_price'] == 0 else product['compare_price'] - product['price']
            record.url = product['url']
            record.images = product['images']
            sizes = []
            sizes = sizes + product['sizes']
            sizes.append(product['color'])
            record.connection_value = ','.join(sizes)

            record.manufacturer_en = product['brand']
            record.brand = product['brand']
            record.tags = product['tags']
            record.other_specs = ''
            record.original_json = json.dumps(product, ensure_ascii=False)

            record.save()
            return record
        except Exception as e:
            print('Error during save proudct {}  cause {} '.format(product['title'], str(e)))
            return None

    # Build product for Shopify
    def build_product_for_shopify(self, product):

        # Images
        images = []
        if len(product['images']) > 0:
            for image in product['images']:
                images.append({'src': image})

        # Option
        shopify_option_arr = []
        if product['color']:
            dict = {
                "name": 'Color',
                "position": 1,
                "values": [product['color']]
            }
            shopify_option_arr.append(dict)

        if len(product['sizes']) > 0:
            index = 1
            dict = {
                "name": 'Size',
                "position": index + 1,
                "values": product['sizes']
            }
            shopify_option_arr.append(dict)

        # Prepare variants
        variants = []
        if len(product['sizes']) > 0:
            for size in product['sizes']:
                variants.append({'option1': product['color'],
                                 'option2': size,
                                 'price': product['price'],
                                 'compare_at_price': product['compare_price'],
                                 'inventory_quantity': 1,
                                 'inventory_management': "shopify"})


        else:
            variants.append({'option1': product['color'],
                             'price': product['price'],
                             'compare_at_price': product['compare_price'],
                             'inventory_quantity': 1,
                             'inventory_management': "shopify"})

        data = {
            "product": {
                "title": product['title'],
                "body_html": product['desc'],
                "vendor": product['brand'],
                "images": images,
                "metafields": [
                    {
                        "key": "url",
                        "value": self.affiliate_url.format(product['url']),
                        "value_type": "string",
                        "namespace": "global"
                    },
                    {
                        "key": "store",
                        "value": 'Ounass',
                        "value_type": "string",
                        "namespace": "global"
                    }
                ],
                "tags": product['tags']

            }
        }

        if len(shopify_option_arr) > 0:
            data['product']['options'] = shopify_option_arr

        if variants and len(variants):
            data['product']['variants'] = variants

        return data
