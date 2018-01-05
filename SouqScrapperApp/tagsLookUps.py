__author__ = 'eMaM'


def getColorTags(tag):
    if tag == 'Multi Color':
        return 'Multi-Coloured'
    if tag == 'Optic White':
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
    if price > 500:
        return ',$500+,'


def formatPrice(value):
    value = value.replace("AED", "")
    value = value.replace(",", '')
    value = value.replace(' ', '')
    value = float(value) * 0.272245
    # value = '%.1f' % round(value, 1)
    return value
