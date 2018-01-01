import requests
from django.conf import settings
import json

from SouqScrapperApp.models import Product

__author__ = 'eMaM'


class ShopifyIntegration():
    def __init__(self):
        self.end_point = settings.PRODUCT_URL.format(settings.API_KEY, settings.API_PASSWORD)
        # self.end_point_update = settings.PRODUCT_UPDATE_URL.format(settings.API_KEY, settings.API_PASSWORD)

    def getShopifySouqProduct(self, productDict):
        # Image
        imageArr = []
        for image in productDict['images']:
            dict = {"src": image.replace('item_XS', 'item_XXL')}
            imageArr.append(dict)

        # Variants
        variants = []
        option_arry = []
        dict = {
            "compare_at_price": productDict['compareAtPrice'],
            "price": productDict['price'],
            "inventory_quantity": productDict['variants']['quantity'],
            "inventory_management": "shopify"
        }

        if len(productDict['variants'].items()) > 1:
            limit = len(productDict['variants'].items()) - 1
            indx = 1
            for var in productDict['variants'].items()[:limit]:
                dict['option' + str(indx)] = var[1]
                option_dict = {
                    "name": var[0],
                    "position": indx,
                    "values": [
                        var[1]
                    ]
                }
                option_arry.append(option_dict)
                indx += 1
        variants.append(dict)

        # data
        data = {
            "product": {
                "title": productDict['title'],
                "body_html": productDict['description'],
                "vendor": productDict['brand'],
                "product_type": productDict['collection'],
                "images": imageArr,
                "metafields": [
                    {
                        "key": "url",
                        "value": productDict['url'],
                        "value_type": "string",
                        "namespace": "global"
                    }
                ],
                "tags": ','.join(productDict['tags']),
                "variants": variants


            }
        }

        if len(option_arry) > 0 :
            data['product']['options'] = option_arry

        return data

    def getShopifyFashionProduct(self, productDict):
        # Image
        imageArr = []
        for image in productDict['images']:
            dict = {"src": image.replace('item_XS', 'item_XXL')}
            imageArr.append(dict)

        # Variants
        variants = []
        dict = {
            "compare_at_price": productDict['price'],
            "price": productDict['compareAtPrice'],
            "inventory_quantity": productDict['quantity'],
            "inventory_management": "shopify"
        }

        # Option Dict
        option_dict = {}
        option_arr = []

        if productDict['variants']['DialColor']:
            dict['option1'] = productDict['variants']['DialColor']
            var_dict = {'name': "Dial Color", 'position': 1, 'values': [productDict['variants']['DialColor']]}
            option_arr.append(var_dict)

        if productDict['variants']['BandColor']:
            dict['option2'] = productDict['variants']['BandColor']
            var_dict = {'name': "Band Color", 'position': 2, 'values': [productDict['variants']['BandColor']]}
            option_arr.append(var_dict)

        variants.append(dict)

        option_dict['options'] = option_arr

        # data
        data = {
            "product": {
                "title": productDict['title'],
                "body_html": productDict['description'],
                "vendor": productDict['brand'],
                "product_type": productDict['collection'],
                "images": imageArr,
                "metafields": [
                    {
                        "key": "url",
                        "value": productDict['url'],
                        "value_type": "string",
                        "namespace": "global"
                    }
                ],
                "tags": ','.join(productDict['tags']),
                "variants": variants,

            }
        }

        if option_arr and len(option_arr) > 0:
            data['product']['options'] = option_arr

        return data

    def addNewProduct(self, productDict, isFashion):
        if not isFashion:
            data = self.getShopifySouqProduct(productDict=productDict)
        else:
            data = self.getShopifyFashionProduct(productDict=productDict)
        try:
            r = requests.post(url=self.end_point, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print productDict['title'] + 'shopfiy status code '+str(r.status_code)
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
