import base64
import collections

import requests
import stringcase

__author__ = 'eMaM'


def getColorTags(tag):
    if tag.lower() == 'Multi Color'.lower():
        return 'Multi-Coloured'

    if tag.lower() == 'MultiColour'.lower():
        return 'Multicoloured'

    if tag.lower() == 'Optic White'.lower():
        return 'White'
    return tag


def getPriceTags(price):
    price = float(price)
    if price < 50:
        return ',Under $50,'
    if price >= 50 and price < 100:
        return ',$50- $100,'
    if price >= 100 and price < 250:
        return ',$100 -$250,'

    if price >= 250 and price < 500:
        return ',$250-$500,'
    if price >= 500 and price < 1000:
        return ',$500-$1000,'
    if price > 1000:
        return ',Above $1000,'


def formatPrice(value):
    if type(value) == str:
        value = value.replace("AED", "")
        value = value.replace("Was", "")
        value = value.replace(",", '')
        value = value.replace(' ', '')
    value = float(value) * 0.272245
    # value = '%.1f' % round(value, 1)
    return value


def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)



def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data



def normalizeBrand(keyword):
    final_word = ''
    keywordArr = keyword.split(' ')
    for key in keywordArr:
        final_word += stringcase.sentencecase(key).replace(' ','') + ' '

    return final_word


