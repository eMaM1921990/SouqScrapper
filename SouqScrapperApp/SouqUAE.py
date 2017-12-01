# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import requests
import time
from bs4 import BeautifulSoup
import string
import json

from django.conf import settings

from models import Product
from SouqScrapperApp.tagsLookUps import getPriceTags, getColorTags

__author__ = 'eMaM'


class SouqUAEScrapper():
    def __init__(self):
        self.item_per_page = 60
        self.list_all_item_attribute = '?section=2'
        self.time_out = None
        self.time_wait = 5
        self.currency = 'AED'
        self.collection_key = 'collections'
        self.sub_collection_key = 'sub_collection'
        self.isFashion_key = 'isFashion'
        self.url_key = 'url'
        self.urls_dict = [
            {self.collection_key: 'Men`s T-Shirts', self.sub_collection_key: 'Round Neck', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/round-neck/a-t-6356-6274-6503/s/'},
            {self.collection_key: 'Men`s T-Shirts', self.sub_collection_key: 'V Neck', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/l/v-neck/a-t-6356-6274-6315-6503/s/'},
            {self.collection_key: 'Men`s T-Shirts', self.sub_collection_key: 'Shirt Neck', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/l/shirt-neck/a-t-6356-6274-6315-6503/s/'},
            {self.collection_key: 'Men`s Vests', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tank-tops/men/tank-tops/a-6356-6274/s/'},
            {self.collection_key: 'Men`s Shorts', self.sub_collection_key: 'Bermuda Shorts', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/bermuda-short/a-t-6356-6335/s/'},
            {self.collection_key: 'Men`s Shorts', self.sub_collection_key: 'Drawstring Shorts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/drawstring-short/a-t-6356-6335/s/'},
            {self.collection_key: 'Men`s Shorts', self.sub_collection_key: 'Cargo Shorts', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/cargo-short/a-t-6356-6335/s/'},
            {self.collection_key: 'Men`s Jeans', self.sub_collection_key: 'Slim Fit', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/slim-fit/a-t-6356  6314/s/'},
            {self.collection_key: 'Men`s Jeans', self.sub_collection_key: 'Straight', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/straight/a-t-6356-6314/s/'},
            {self.collection_key: 'Men`s Jeans', self.sub_collection_key: 'Skinny', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/skinny/a-t-6356-6314/s/'},
            {self.collection_key: 'Men`s Jeans', self.sub_collection_key: 'Ripped', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/ripped/a-t-6356-6314/s/'},
            {self.collection_key: 'Men`s Coats, Jackets & Hoodies', self.sub_collection_key: 'Zip Up Hoodie',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/zip-up-hoodie/a-t-6356-6309/s/'},
            {self.collection_key: 'Men`s Coats, Jackets & Hoodies', self.sub_collection_key: 'Puffer Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/puffer-jacket/a-t-6356-6309/s/'},
            {self.collection_key: 'Men`s Coats, Jackets & Hoodies', self.sub_collection_key: 'Bomber Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/bomber-jacket/a-t-6356-6309/s/'},
            {self.collection_key: 'Men`s Shirts', self.sub_collection_key: 'Full Sleeve', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/shirts/full-sleeve/a-t-6356-6274-6490/s/'},
            {self.collection_key: 'Men`s Shirts', self.sub_collection_key: 'Short Sleeve', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/shirts/short-sleeve/a-t-6356-6274-6490/s/'},
            {self.collection_key: 'Men`s Suits', self.sub_collection_key: 'Tuxedo', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/suits/suits-486/men/tuxedo/a-t-6356-6332/s/'},
            {self.collection_key: 'Men`s Suits', self.sub_collection_key: 'Business Suit', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/suits/suits-486/men/business-suit/a-t-6356-6332/s/'},
            {self.collection_key: 'Men`s Underwear', self.sub_collection_key: 'Boxers', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/underwear/underwear-489/men/boxers/a-t-6356-6337/s/'},
            {self.collection_key: 'Men`s Underwear', self.sub_collection_key: 'Briefs', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/underwear/underwear-489/men/briefs/a-t-6356-6337/s/'},
            {self.collection_key: 'Men`s Sportswear', self.sub_collection_key: 'Sports Tops', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-tops/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Sportswear', self.sub_collection_key: 'Sports Shorts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-shorts/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Sportswear', self.sub_collection_key: 'Sports Pants',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-pants/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Sportswear', self.sub_collection_key: 'Sports Jackets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-jackets/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Sportswear', self.sub_collection_key: 'Sports Vests',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-vests/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Swimwear', self.sub_collection_key: 'Swim Shorts', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/men/swim-shorts/a-t-6356-6435/s/'},
            {self.collection_key: 'Men`s Swimwear', self.sub_collection_key: 'Swim Trunks', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/men/swim-trunk/a-t-6356-6435/s/'},
            {self.collection_key: 'Men`s Belts', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-belt/belts-557%7Caccessories-466/a-t/s/'},
            {self.collection_key: 'Men`s Cufflinks', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: "https://uae.souq.com/ae-en/cufflinks/men%60s-jewelry-292%7Caccessories-466/cufflinks/a-t-6313/s/"},
            {self.collection_key: 'Men`s Hats', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-cap-or-hat/hats---and---caps-566/men/baseball---and---snapback-hat/a-t-6356-6573/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Bifold Wallets', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/bifold-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Card & Id Cases',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/card---and---id-cases/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Trifold Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/trifold-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Zip Around Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/zip-around-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Flap Wallets', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/flap-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Clip Wallet', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/clip-wallet/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Wallets', self.sub_collection_key: 'Travel & Document Holders',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/travel---and---document-holders/a-t-6356-5700/s/'},
            {self.collection_key: 'Men`s Watches', self.sub_collection_key: 'Casual Watch', self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImNhc3VhbCB3YXRjaCJdfX0%3D'},
            {self.collection_key: 'Men`s Watches', self.sub_collection_key: 'Dress Watch', self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImRyZXNzIHdhdGNoIl19fQ%3D%3D'},
            {self.collection_key: 'Men`s Watches', self.sub_collection_key: 'Sport Watch', self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbInNwb3J0IHdhdGNoIl19fQ%3D%3D'},
            {self.collection_key: 'Men`s Ties', self.sub_collection_key: 'Neck Tie', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/ties/accessories-466/men/neck-ties/a-t-6356-6334/s/'},
            {self.collection_key: 'Men`s Ties', self.sub_collection_key: 'Bow Tie', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/ties/accessories-466/men/bow-ties/a-t-6356-6334/s/'},
            {self.collection_key: 'Men`s Rings, Necklaces & Bracelets', self.sub_collection_key: 'Rings',
             self.isFashion_key: False, self.url_key: 'https://uae.souq.com/ae-en/men/rings-284/men/a-t-1780/s/'},
            {self.collection_key: 'Men`s Rings, Necklaces & Bracelets', self.sub_collection_key: 'Necklaces',
             self.isFashion_key: False, self.url_key: 'https://uae.souq.com/ae-en/men/men/necklaces-285/a-1780 t/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Square', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/square/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Aviator', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/aviator/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Rectangle', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/rectangle/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Oval', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/oval/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Wayfarer', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/wayfarer/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Wrap Around', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/wrap-around/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Round', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/round/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Rimless', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/rimless/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Sunglasses', self.sub_collection_key: 'Half Frame', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/half-frame/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Men`s Flip-Flops', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/flip-flops/men/a-6356/s/'},
            {self.collection_key: 'Men`s Trainers ', self.sub_collection_key: 'Casual Trainers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sneakers/casual---and---dress-shoes-481/fashion-sneakers/men/a-t-6453-6356/s/'},
            {self.collection_key: 'Men`s Trainers ', self.sub_collection_key: 'Athletic Trainers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/athletic-shoes/athletic-shoes-534/men/a-t-6356/s/'},
            {self.collection_key: 'Men`s Sandals ', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sandals/men/sandals-479/a-6356-t/s/'},
            {self.collection_key: 'Men`s Formal Shoes ', self.sub_collection_key: 'Loafers & Moccasins',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dress-shoes-men/men/loafers---and---moccasian/a-6356-6453/s/'},
            {self.collection_key: 'Oxfords & Wingtips ', self.sub_collection_key: 'Loafers & Moccasins',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dress-shoes-men/men/oxfords---and---wingtip/a-6356-6453/s/'},
            {self.collection_key: 'Oxfords & Wingtips ', self.sub_collection_key: 'Slip-Ons', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dress-shoes-men/men/slip-on/a-6356-6453/s/'},
            {self.collection_key: 'Men`s Boots ', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/boots/boots-469/men/a-t-6356/s/'},
            {self.collection_key: 'Men`s Holdalls', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/duffle-bag/duffle-bags-559/men/a-t-6356/s/'},
            {self.collection_key: 'Men`s Backpacks', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/backpacks/men/a-6356/l/'},
            {self.collection_key: 'Men`s Briefcases & Work Bags', self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/briefcase/men/briefcases/a-6356-6328/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Blouses', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/blouses/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'T-Shirts', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/t--shirts/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Shirts', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/shirts/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Crop Tops', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/crop-tops/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Pull Over Tops', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/pullover-tops/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Long Line Tops', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/long-line-tops/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Hoodies & Sweatshirts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/hoodies---and---sweatshirts/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Cami & Strappy Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/cami---and---strappy-tops/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Tank Tops', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/tank-tops/a-t-6356-6274/s/'},
            {self.collection_key: 'Women`s Trousers & Leggings', self.sub_collection_key: 'Trousers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/pants/pants-477/women/trousers/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Trousers & Leggings', self.sub_collection_key: 'Leggings',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/pants/pants-477/women/leggings/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Shorts', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482/women/a-t-6356/s/'},
            {self.collection_key: 'Women`s Jeans', self.sub_collection_key: 'Skinny', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/skinny/a-t-6356-5700-6314/s/'},
            {self.collection_key: 'Women`s Jeans', self.sub_collection_key: 'Slim Fit', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/slim-fit/a-t-6356-5700-6314/s/'},
            {self.collection_key: 'Women`s Jeans', self.sub_collection_key: 'Straight', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/straight/a-t-6356-5700-6314/s/'},
            {self.collection_key: 'Women`s Jeans', self.sub_collection_key: 'Ripped', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/ripped/a-t-6356-5700-6314/s/'},
            {self.collection_key: 'Women`s Dresses', self.sub_collection_key: 'Bodycon', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dresses/dresses-465/women/bodycon/a-t-6356-6269/s/'},
            {self.collection_key: 'Women`s Dresses', self.sub_collection_key: 'A-Line', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dresses/dresses-465/women/a-line/a-t-6356-6269/s/'},
            {self.collection_key: 'Women`s Dresses', self.sub_collection_key: 'Straight Fit', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dresses/dresses-465/women/straight/a-t-6356-6269/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Cardigan',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/cardigan/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Blazer',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/blazer/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Zip Up Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/zip-up-jacket/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Biker Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/biker-jacket/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Bomber Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/bomber-jacket/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Zip Up Hoodie',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/zip-up-hoodie/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Shrugs',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/shrugs/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Trench Coat',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/trench-coat/a-t-6356-6309/s/'},
            {self.collection_key: 'Women`s Jumpsuits & Rompers', self.sub_collection_key: 'Jumpsuit',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jumpsuit/jumpsuits,-rompers---and---overalls-563/women/jumpsuit/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Jumpsuits & Rompers', self.sub_collection_key: 'Romper',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jumpsuit/jumpsuits,-rompers---and---overalls-563/women/romper/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Jumpsuits & Rompers', self.sub_collection_key: 'Overalls',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jumpsuit/jumpsuits,-rompers---and---overalls-563/women/overall/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Bras', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/bra/a-t-6307/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Lingerie Dresses',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/lingerie-dresses/a-t-6307/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Lingerie Panties',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/lingerie-panties/a-t-6307/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Babydolls', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/babydolls---and---playsuits/a-t-6307/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Lingerie Sets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/lingerie-set/a-t-6307/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Bustiers & Corsets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/bustiers---and---corsets/a-t-6307/s/'},
            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Camisoles & Chemises',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/camisoles---and---chemises/a-t-6307/s/'},
            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sport Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-tops/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sport Bottoms',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-pants/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sports Bras',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-bras/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sports Suits',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-suits/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sports Jackets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-jackets/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Skirts', self.sub_collection_key: 'Bodycon', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/skirts/skirts-483/women/body-con/a-t-6356-6308/s/'},
            {self.collection_key: 'Women`s Skirts', self.sub_collection_key: 'A-Line', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/skirts/skirts-483/women/a-line/a-t-6356-6308/s/'},
            {self.collection_key: 'Women`s Skirts', self.sub_collection_key: 'Straight Fit', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/skirts/skirts-483/women/straight/a-t-6356-6308/s/'},
            {self.collection_key: 'Women`s Swimwear', self.sub_collection_key: 'Bikini Sets', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/bikini-set/a-t-6356-6435/s/'},
            {self.collection_key: 'Women`s Swimwear', self.sub_collection_key: 'Bikinis', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/bikinis/a-t-6356-6435/s/'},
            {self.collection_key: 'Women`s Swimwear', self.sub_collection_key: 'Sarong & Cover Ups',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/sarong---and---cover-ups/a-t-6356-6435/s/'},
            {self.collection_key: 'Women`s Swimwear', self.sub_collection_key: 'One Piece & Molokini`s',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/one--pieces---and---monokinis/a-t-6356-6435/s/'},
            {self.collection_key: 'Women`s Belts', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/belts/women/a-6356/s/'},
            {self.collection_key: 'Women`s Watches', self.sub_collection_key: None, self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797&tag_id=4012'},
            {self.collection_key: 'Women`s Hats', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/hats/hats---and---caps-566/women/baseball---and---snapback-hat/a-t-6356-6573/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Zip Around Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/zip-around-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Bifold Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/bifold-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Flap Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/flap-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Trifold Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/trifold-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Casual Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/casual-wallets/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Card & Id Cases',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/card---and---id-cases/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Coin Purses & Pouches',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/coin-purses---and---pouches/a-t-6356-5700/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Cat Eye', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/cat-eye/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Square', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/square/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Oval', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/oval/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Round', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/round/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Aviator', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/aviator/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Wayfarer', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/wayfarer/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Rectangle', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/rectangle/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Butterfly', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/butterfly/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Sunglasses', self.sub_collection_key: 'Oversized', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/oversized/a-t-6356-6265-6572/s/'},
            {self.collection_key: 'Women`s Rings', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-rings/rings-284/women/swarovski%7Cmichael-kors%7Cvera-perla%7Cpandora%7Cemporio-armani/a-t-1780-7/s/'},
            {self.collection_key: 'Women`s Necklaces', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women/necklaces-285/swarovski%7Cfossil%7Cemporio-armani%7Cguess%7Cswarovski-elements%7Cmichael-kors%7Cvera-perla%7Csteve-madden%7Cjuicy-couture/a-t-7/s/'},
            {self.collection_key: 'Women`s Bracelets', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-bracelet/bracelets-287/women/kate-spade%7Cfossil%7Cpandora%7Cswarovski%7Cswarovski-elements%7Cmichael-kors%7Cguess/a-t-1780-7/s/'},
            {self.collection_key: 'Women`s Earrings', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-earring/earrings-286/kate-spade%7Cswarovski%7Cvera-perla%7Cpandora%7Cfossil%7Cmichael-kors%7Cemporio-armani%7Cswarovski-elements/a-t-7/s/'},
            {self.collection_key: 'Women`s Trainers', self.sub_collection_key: 'Athletic Trainers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/athletic-shoes/athletic-shoes-534/women/a-t-6356/s/'},
            {self.collection_key: 'Women`s Trainers', self.sub_collection_key: 'Casual Trainers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sneakers/women/casual---and---dress-shoes-481/a-6356-t/s/'},
            {self.collection_key: 'Women`s Trainers', self.sub_collection_key: 'Women`s Heels',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/heels/women/heels/casual---and---dress-shoes-481%7C469/a-6356-6453-t/s/'},
            {self.collection_key: 'Women`s Heels', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/heels/women/heels/casual---and---dress-shoes-481%7C469/a-6356-6453-t/s/'},
            {self.collection_key: 'Women`s Flats', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/flats/casual---and---dress-shoes-481%7Csandals-479/women/flat/a-t-6356-6453/s/'},
            {self.collection_key: 'Women`s Boots', self.sub_collection_key: 'Heels Boots', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/boots/boots-469/women/heels-boots/a-t-6356-6437/s/'},
            {self.collection_key: 'Women`s Boots', self.sub_collection_key: 'Pull on Boots', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/boots/boots-469/women/pull-on-boots/a-t-6356-6437/s/'},
            {self.collection_key: 'Women`s Boots', self.sub_collection_key: 'Lace Up Boots', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/boots/boots-469/women/lace-up-boots/a-t-6356-6437/s/'},
            {self.collection_key: 'Women`s Wedges', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/wedges/sandals-479%7Ccasual---and---dress-shoes-481%7Cboots-469%7Cathletic-shoes-534/women/wedges/a-t-6356-6453/s/'},
            {self.collection_key: 'Women`s Backpacks', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-backpack/backpacks-468/fashion-backpacks/a-t-5700/s/'},
            {self.collection_key: 'Women`s Tote Bags', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/handbags/handbags-472/tommy-hilfiger%7Cguess%7Ccalvin-klein%7Cmichael-kors%7Ckate-spade%7Clauren-by-ralph-lauren%7Cmarc-jacobs%7Claura-ashley%7Ckate-spade-new-york%7Cvalentino%7Cgivenchy/women/tote-bags/a-t-7-6356-6328/s/'},
            {self.collection_key: 'Women`s Crossbody Bags', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/handbags/handbags-472/tommy-hilfiger%7Cguess%7Ccalvin-klein%7Cmichael-kors%7Ckate-spade%7Clauren-by-ralph-lauren%7Cmarc-jacobs%7Claura-ashley%7Ckate-spade-new-york%7Cvalentino%7Cgivenchy/women/crossbody-bags/a-t-7-6356-6328/s/'},
            {self.collection_key: 'Women`s Clutches', self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/handbags/handbags-472/tommy-hilfiger%7Cguess%7Ccalvin-klein%7Cmichael-kors%7Ckate-spade%7Clauren-by-ralph-lauren%7Cmarc-jacobs%7Claura-ashley%7Ckate-spade-new-york%7Cvalentino%7Cgivenchy/women/clutches/a-t-7-6356-6328/s/'},
            {self.collection_key: 'Women`s Luggage & Suitcases', self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/suitcases/trolley-suitcases---and---bags-475/women/luggage-trolley-bags/a-t-6356-5700/s/'},
        ]

    # Open Http connection
    def open_http_connection(self, call_url, page):
        try:
            print 'parsing url ' + call_url
            time.sleep(10)
            scraped_html_page = requests.get(call_url, timeout=self.time_out,
                                             params=dict(page=page))

            print 'parsing url end' + call_url
            # Check response code
            if scraped_html_page.status_code == 200:
                return scraped_html_page.text
        except Exception as e:
            print str(e)
            return None

    # parse page in soup
    def parsePageSoap(self, page):
        soup = BeautifulSoup(page, "html.parser")
        return soup

    # Start Scrap
    def startScrappingProcessing(self, url, isFashion, collection, subCollection):
        print 'Enter startScrappingProcessing'
        url += self.list_all_item_attribute
        scrappedPage = self.open_http_connection(call_url=url, page=1)
        if scrappedPage:
            if not isFashion:
                self.scrapSearchPageResults(page=scrappedPage, url=url, collection=collection,
                                            subCollection=subCollection)
        print 'Exit startScrappingProcessing'

    # Scrap search page result
    def scrapSearchPageResults(self, page, url, collection, subCollection):
        resultData = self.retrieveSearchAsJson(page=page)
        commonTags = self.retrieveURLTags(page=page)
        # Calc total Page result
        totalPage = self.calcTotalPage(resultData['numberOfItems'])
        self.parseProductsList(resultData['itemListElement'], commonTags, collection, subCollection)

        for page in range(2, totalPage, 1):
            # url += self.list_all_item_attribute
            scrappedPage = self.open_http_connection(call_url=url, page=page)
            resultData = self.retrieveSearchAsJson(page=scrappedPage)
            self.parseProductsList(resultData['itemListElement'], commonTags, collection, subCollection)

    def calcTotalPage(self, numberOfItems):
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
            del tags[len(tags)-1]
        return tags

    def retrieveSearchAsJson(self, page):
        soup = self.parsePageSoap(page=page)
        body = soup.find('script', attrs={'type': 'application/ld+json'}).text
        resultData = json.loads(body)

        return resultData

    def parseProductsList(self, items, commonTags, collection, subCollection):
        for item in items:
            product = self.retrieveProductDetails(url=item['url'], commonTags=commonTags, collection=collection,
                                                  subCollection=subCollection)
            self.saveProduct(product=product)

    def retrieveProductImageBySize(self, soup):
        attr = []
        images = soup.find_all(attrs={'class': 'slide'})
        for imageTag in images:
            if imageTag.has_attr('data-thumb'):
                url = str(imageTag['data-thumb'])
                attr.append(url)

        return attr

    def retrieveProductColorsBySize(self, soup):
        attrArry = []
        colors = soup.find(attrs={'class': 'colors-block'}).contents
        for index, color in enumerate(colors):
            if color.name == 'span' and color.has_attr('data-value'):
                attrArry.append(str(color['data-value']))
        return attrArry

    def retrieveProductDescColor(self, soup, product):
        body = soup.find('script', attrs={'type': 'application/ld+json'}).text
        resultData = json.loads(body)
        product['description'] = str(resultData['description'].encode('utf-8').strip())
        product['color'] = str(resultData['color'])
        product['brand'] = str(resultData['brand']['name']).translate(
            string.maketrans("\n\t\r ", "    ")).replace(' ', '')

    def formatPrice(self, value):
        value = value.replace(self.currency, "")
        return value.replace(' ', '')

    def retrieveProductDetails(self, url, commonTags, collection, subCollection):
        product_page_result = self.open_http_connection(call_url=url, page=None)

        if product_page_result:
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
            sizes = soup.find_all(attrs={'class': "item-connection"})
            sizes_arr = []
            for size in sizes:
                sizes_arr.append(str(size.text).translate(string.maketrans("\n\t\r ", "    ")))

            # Get product color and description
            self.retrieveProductDescColor(soup=soup, product=product)

            product['title'] = title
            product['discountAmount'] = discountAmount
            product['compareAtPrice'] = compareAtPrice
            product['price'] = price

            product['collection'] = collection if collection else ''
            product['subCollection'] = subCollection if subCollection else ''
            product['url'] = str(url)
            product['images'] = self.retrieveProductImageBySize(soup)
            product['variants'] = {}
            product['variants']['size'] = sizes_arr
            product['variants']['colors'] = product['color']

            tags = []
            # Get Product tags
            tags.append(getPriceTags(price=compareAtPrice))
            # Get Color Tags
            tags.append(getColorTags(tag=product['color']))
            # Get Brand Tags
            tags.append(product['brand'])
            # Get Collection tags
            tags.append(product['collection'])

            product['tags'] = tags + commonTags
            print product
            return product

    def saveProduct(self, product):
        try:
            record = Product()
            record.title = product['title']
            record.sub_collection = product['subCollection']
            record.collection = product['collection']
            record.description = product['description']
            record.compare_at_Price = product['compareAtPrice']
            record.price = product['price']
            record.discount_amount = product['discountAmount']
            record.url = product['url']
            record.color = product['color']
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
            record.variant_colors = product['color']
            record.variant_size = ','.join(product['variants']['size'])
            record.brand = str(product['brand'])
            record.tags = ','.join(product['tags'])
            record.save()
        except Exception as e:
            print str(e)


    def sendProductToAPI(self, product):
        endPoint = settings.PRODUCT_URL
        endPoint = endPoint.format(settings.API_KEY,settings.API_PASSWORD)

        # data
        data = {
            "product": {
                "title": product['title'],
                "body_html": product['description'],
                "vendor": "Souq",
                "product_type": "Snowboard",
                "images": [
                    {
                        "src": "http:\/\/example.com\/rails_logo.gif"
                    }
                ],
                "metafields": [
                    {
                        "key": "url",
                        "value": product['url'],
                        "value_type": "string",
                        "namespace": "global"
                    }
                ],
                "tags": ','.join(product['tags']),
                "variants": [
                    {
                        "compare_at_price": null,

                        "option1": "Pink",
                        "position": 1,
                        "price": 199.99,


                    }
                ]

            }
        }

        r = requests.post(url = endPoint, data = data)
        return r.text
#
# SouqUAEScrapper().startScrappingProcessing(
#     'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/round-neck/a-t-6356-6274-6503/s/', False,
#     'Men`s T-Shirts', 'Round Neck')
