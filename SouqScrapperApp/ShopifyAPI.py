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
        for size in productDict['variants']['size']:
            dict = {
                "compare_at_price": productDict['price'],
                "price": productDict['compareAtPrice'],
                "option1": productDict['color'],
                "option2": size['name'],
                "inventory_quantity": size['quantity'],
                "inventory_management": "shopify"
            }
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
                "variants": variants,
                "options": [
                    {
                        "name": "Color",
                        "position": 1,
                        "values": [
                            productDict['color']
                        ]
                    },
                    {
                        "name": "Size",
                        "position": 2,
                        "values": productDict['variants']['size']
                    }
                ]

            }
        }

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
            "option1": productDict['variants']['DialColor'],
            "option2": productDict['variants']['BandColor'],
            "inventory_quantity": productDict['quantity'],
            "inventory_management": "shopify"
        }
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
                "variants": variants,
                "options": [
                    {
                        "name": "Dial Color",
                        "position": 1,
                        "values": [
                            productDict['variants']['DialColor']
                        ]
                    },
                    {
                        "name": "Band Color",
                        "position": 2,
                        "values": productDict['variants']['BandColor']
                    }
                ]

            }
        }

        return data

    def addNewProduct(self, productDict, isFashion):
        if not isFashion:
            data = self.getShopifySouqProduct(productDict=productDict)
        else:
            data = self.getShopifyFashionProduct(productDict=productDict)

        r = requests.post(url=self.end_point, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        # update variant Image
        self.updateProductVarirant(r.text)
        return r.text

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
