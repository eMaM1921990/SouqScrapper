import json
import time

import requests
from bs4 import BeautifulSoup

from SouqScrapperApp.utils import normalizeBrand, formatPrice, getColorTags

__author__ = 'eMaM'


class NassScrapper():
    def __init__(self):
        self.time_out = None
        self.time_wait = 5
        self.currency = 'AED'
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.product_url = 'https://www.nass.com{}'
        self.product_image_url = 'https:{}'
        self.affiliate_url = 'https://tayer.ae/?a=362&c=326&p=r&s1=&ckmrdr={}'

    def startScrappingProcessing(self, url, tags):
        print('[Naas] start Scrapping Processing -- {} '.format(url))
        page_html = self.open_http_connection(call_url=url, page=0)
        if page_html:
            self.retrieve_result(page_html=page_html, url=url, tags=tags)

        print('[Naas]  end Scrapping Processing -- {} '.format(url))


    # Open Http connection
    def open_http_connection(self, call_url, page, headers=None):
        try:
            # print('Begin: Call URL -- {} '.format(call_url))
            time.sleep(self.time_wait)
            scraped_html_page = requests.get(call_url, timeout=self.time_out,
                                             params=dict(P=page), headers=headers)
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
        product_title_tag = href_tag.find('div',attrs={'class':'product-title'})
        if product_title_tag:
            product_title_strong_tag = product_title_tag.find('strong')
            if product_title_strong_tag:
                product['title'] = str(product_title_strong_tag['title'])
                product['brand'] = normalizeBrand(str(product_title_strong_tag.text))

        # product price
        product_price_tag = href_tag.find('span',attrs={'class':'w-product-price'})
        if product_price_tag:
            product['price'] = formatPrice(int(href_tag['data-price']))

        # product price discount
        price_discount_tag = href_tag.find('span',attrs={'class':'disc-price'})
        if price_discount_tag:
            product['compare_price'] = formatPrice(str(price_discount_tag.text))
        else:
            product['compare_price'] = 0

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