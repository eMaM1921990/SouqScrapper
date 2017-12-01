import requests
from django.conf import settings
import json

__author__ = 'eMaM'


class ShopifyIntegration():
    def __init__(self):
        self.end_point = settings.PRODUCT_URL.format(settings.API_KEY, settings.API_PASSWORD)

    def addNewProduct(self, productDict):

        # Image
        imageArr = []
        for image in productDict['images']:
            dict = {"src": image.replace('item_XS', 'item_L')}
            imageArr.append(dict)

        # Variants
        variants = []
        for size in productDict['variants']['size']:
            dict = {
                "compare_at_price": productDict['price'],
                "price": productDict['compareAtPrice'],
                "option1": productDict['color'],
                "option2": size
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

        r = requests.post(url=self.end_point, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        return r.text
