import requests
from django.conf import settings
import json

from SouqScrapperApp.models import Product
from SouqScrapperApp.tagsLookUps import formatPrice

__author__ = 'eMaM'


class ShopifyIntegration():
    def __init__(self):
        self.end_point = settings.PRODUCT_URL.format(settings.API_KEY, settings.API_PASSWORD)
        # self.end_point_update = settings.PRODUCT_UPDATE_URL.format(settings.API_KEY, settings.API_PASSWORD)

    def getShopifySouqProduct(self, product_dict):
        # Image
        imageArr = []
        for image in product_dict['images']:
            imageArr.append({"src": image['xxlarge_url_picture']})

        # Options
        option_arr = []
        if product_dict['connections']:
            for k, v in (product_dict['connections']).iteritems():
                option_dict = {'title': str(v['title'])}
                # Append options
                for k1, v1 in (v['connectedValues']).iteritems():
                    option_dict['value'] = []
                    option_dict['value'].append(v1['value'])
                option_arr.append(option_dict)

        shopify_option_arr = []
        if option_arr and len(option_arr) > 0:
            for index, option in enumerate(option_arr):
                dict = {
                    "name": option['title'],
                    "position": index + 1,
                }
                option_val_arr = []
                for option_value in option['value']:
                    option_val_arr.append(str(option_value))
                dict['values'] = option_val_arr
                shopify_option_arr.append(dict)

        # Prepare variants
        variants = []
        if shopify_option_arr:
            option_1_arry = shopify_option_arr[0]
            try:
                option_2_arry = shopify_option_arr[1]
            except Exception:
                option_2_arry = None
            variants = self.generate_product_variants(option_1_array=option_1_arry, option_2_array=option_2_arry,product_dict=product_dict)


        # data
        data = {
            "product": {
                "title": product_dict['title'],
                "body_html": product_dict['description'],
                "vendor": str(product_dict['manufacturer_en']) if product_dict['manufacturer_en'] else str(product_dict['seller']['name']),
                "product_type": product_dict['name_type_item'],
                "images": imageArr,
                "metafields": [
                    {
                        "key": "url",
                        "value": product_dict['url'],
                        "value_type": "string",
                        "namespace": "global"
                    }
                ],
                "tags": product_dict['tags'],
                "variants": variants

            }
        }

        if shopify_option_arr and len(shopify_option_arr) > 0:
            data['product']['options'] = shopify_option_arr

        if variants and len(variants):
            data['product']['variants'] = variants

        return data


    def addNewProduct(self, productDict):
        data = self.getShopifySouqProduct(product_dict=productDict)
        try:
            r = requests.post(url=self.end_point, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print productDict['title'] + 'shopfiy status code ' + str(r.status_code)
            # update variant Image
            self.updateProductVarirant(r.text)
            return r.text
        except Exception as e:
            print r.content
            return None

    def removeShopifyProduct(self, id):
        end_point_update = settings.PRODUCT_UPDATE_URL.format(settings.API_KEY, settings.API_PASSWORD, id)
        r = requests.delete(url=end_point_update, headers={'Content-Type': 'application/json'})
        # if json.loads(r.text.)
        return r.text

    def updateProduct(self, product, shopifyJson):
        try:
            object = Product.objects.get(id=product.id)
            object.shopify_id = json.loads(str(shopifyJson))['product']['id']
            object.save()
        except Exception as e:
            print str(e)

    def updateProductVarirant(self, shopifyJson):
        image_id = json.loads(str(shopifyJson))['product']['images'][0]['id']
        variants = json.loads(str(shopifyJson))['product']['variants']
        for variant in variants:
            end_point_update = settings.PRODUCT_VARIANT_URL.format(settings.API_KEY, settings.API_PASSWORD,
                                                                   variant['id'])
            data = {
                "variant": {
                    "id": variant['id'],
                    "image_id": image_id
                }
            }
            r = requests.put(url=end_point_update, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    def generate_product_variants(self, option_1_array, option_2_array, product_dict):
        variants = []
        if option_2_array:
            for k,v in option_1_array.iteritems():
                for k1,v1 in option_2_array.iteritems():
                    if k == 'values' and k1 == 'values':
                        variants.append({'option1':  v[0],
                                         'option2':  v1[0],
                                         'compare_at_price':formatPrice(product_dict['price']['current_price']),
                                         'price':formatPrice(product_dict['price']['old_price']),
                                         'inventory_quantity':str(product_dict['available_quantity']),
                                         'inventory_management':"shopify"})
        else:
            for k,v in option_1_array.iteritems():
                if k == 'values':
                    variants.append({'option1': v[0],
                                     'compare_at_price':formatPrice(product_dict['price']['current_price']),
                                     'price':formatPrice(product_dict['price']['old_price']),
                                     'inventory_quantity':str(product_dict['available_quantity']),
                                     'inventory_management':"shopify"})
        return variants