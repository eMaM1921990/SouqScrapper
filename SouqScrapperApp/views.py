# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


# self.urls_dict = [
#     {'main_collection': 'Men’s T-Shirts', 'sub_collection': 'Round Neck',
#      'url': 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/round-neck/a-t-6356-6274-6503/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s T-Shirts', 'sub_collection': 'V Neck',
#      'url': 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/l/v-neck/a-t-6356-6274-6315-6503/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s T-Shirts', 'sub_collection': 'Shirt Neck',
#      'url': 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/l/shirt-neck/a-t-6356-6274-6315-6503/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Vests', 'sub_collection': None,
#      'url': 'https://uae.souq.com/ae-en/tank-tops/men/tank-tops/a-6356-6274/s/'},
#
#     {'main_collection': 'Men’s Shorts', 'sub_collection': 'Bermuda Shorts',
#      'url': 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/bermuda-short/a-t-6356-6335/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Shorts', 'sub_collection': 'Drawstring Shorts',
#      'url': 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/drawstring-short/a-t-6356-6335/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Shorts', 'sub_collection': 'Cargo Shorts',
#      'url': 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/cargo-short/a-t-6356-6335/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Jeans', 'sub_collection': 'Slim Fit',
#      'url': 'https://uae.souq.com/ae-en/jeans/pants-477/men/slim-fit/a-t-6356  6314/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Jeans', 'sub_collection': 'Straight',
#      'url': 'https://uae.souq.com/ae-en/jeans/pants-477/men/straight/a-t-6356-6314/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Jeans', 'sub_collection': 'Skinny',
#      'url': 'https://uae.souq.com/ae-en/jeans/pants-477/men/skinny/a-t-6356-6314/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Jeans', 'sub_collection': 'Ripped',
#      'url': 'https://uae.souq.com/ae-en/jeans/pants-477/men/ripped/a-t-6356-6314/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Coats, Jackets & Hoodies', 'sub_collection': 'Zip Up Hoodie',
#      'url': 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/zip-up-hoodie/a-t-6356-6309/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Coats, Jackets & Hoodies', 'sub_collection': 'Zip Up Jacket',
#      'url': 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/zip-up-jacket/a-t-6356-6309/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Coats, Jackets & Hoodies', 'sub_collection': 'Puffer Jacket',
#      'url': 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/puffer-jacket/a-t-6356-6309/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Coats, Jackets & Hoodies', 'sub_collection': 'Bomber Jacket',
#      'url': 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/bomber-jacket/a-t-6356-6309/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Shirts', 'sub_collection': 'Full Sleeve',
#      'url': 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/shirts/full-sleeve/a-t-6356-6274-6490/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Shirts', 'sub_collection': 'Short Sleeve',
#      'url': 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/shirts/short-sleeve/a-t-6356-6274-6490/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Suits', 'sub_collection': 'Tuxedo',
#      'url': 'https://uae.souq.com/ae-en/suits/suits-486/men/tuxedo/a-t-6356-6332/s/'},
#
#     {'main_collection': 'Men’s Suits', 'sub_collection': 'Business Suit',
#      'url': 'https://uae.souq.com/ae-en/suits/suits-486/men/business-suit/a-t-6356-6332/s/'},
#
#     {'main_collection': 'Men’s Underwear', 'sub_collection': 'Boxers',
#      'url': 'https://uae.souq.com/ae-en/underwear/underwear-489/men/boxers/a-t-6356-6337/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Underwear', 'sub_collection': 'Briefs',
#      'url': 'https://uae.souq.com/ae-en/underwear/underwear-489/men/briefs/a-t-6356-6337/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Sportswear', 'sub_collection': 'Sports Tops',
#      'url': 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-tops/a-t-6356-5700/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Sportswear', 'sub_collection': 'Sports Shorts',
#      'url': 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-shorts/a-t-6356-5700/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Sportswear', 'sub_collection': 'Sports Pants',
#      'url': 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-pants/a-t-6356-5700/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Sportswear', 'sub_collection': 'Sports Jackets',
#      'url': 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-jackets/a-t-6356-5700/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Sportswear', 'sub_collection': 'Sports Vests',
#      'url': 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-vests/a-t-6356-5700/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Swimwear', 'sub_collection': 'Swim Shorts',
#      'url': 'https://uae.souq.com/ae-en/swimwear/swimwear-487/men/swim-shorts/a-t-6356-6435/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Swimwear', 'sub_collection': 'Swim Trunks',
#      'url': 'https://uae.souq.com/ae-en/swimwear/swimwear-487/men/swim-trunk/a-t-6356-6435/s/?fbs=yes'},
#
#     {'main_collection': 'Men’s Belts', 'sub_collection': None,
#      'url': 'https://uae.souq.com/ae-en/men-belt/belts-557%7Caccessories-466/a-t/s/?ref=nav'},
#
#     {'main_collection': 'Men’s Cufflinks', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/cufflinks/men's-jewelry-292%7Caccessories-466/cufflinks/a-t-6313/s/"},
#
#     {'main_collection': 'Men’s Hats', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/men-cap-or-hat/hats---and---caps-566/men/baseball---and---snapback-hat/a-t-6356-6573/s/?sortby=ir_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Bifold Wallets',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/bifold-wallets/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Card & Id Cases',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/card---and---id-cases/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Trifold Wallets',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/trifold-wallets/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Zip Around Wallets',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/zip-around-wallets/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Flap Wallets',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/flap-wallets/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Clip Wallet',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/clip-wallet/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Wallets', 'sub_collection': 'Travel & Document Holders',
#      'url': "https://uae.souq.com/ae-en/men-wallet/wallets-533/men/travel---and---document-holders/a-t-6356-5700/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Watches', 'sub_collection': 'Casual Watch',
#      'url': "https://fashion.souq.com/ae-en/watches/c/3797?ref=nav&q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImNhc3VhbCB3YXRjaCJdfX0%3D"},
#
#     {'main_collection': 'Men’s Watches', 'sub_collection': 'Dress Watch',
#      'url': "https://fashion.souq.com/ae-en/watches/c/3797?ref=nav&q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImNhc3VhbCB3YXRjaCJdfX0%3D"},
#
#     {'main_collection': 'Men’s Watches', 'sub_collection': 'Sport Watch',
#      'url': "https://fashion.souq.com/ae-en/watches/c/3797?ref=nav&q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbInNwb3J0IHdhdGNoIl19fQ%3D%3D"},
#
#     {'main_collection': 'Men’s Ties', 'sub_collection': 'Neck Tie',
#      'url': "https://uae.souq.com/ae-en/ties/accessories-466/men/neck-ties/a-t-6356-6334/s/"},
#
#     {'main_collection': 'Men’s Ties', 'sub_collection': 'Bow Tie',
#      'url': "https://uae.souq.com/ae-en/ties/accessories-466/men/bow-ties/a-t-6356-6334/s/"},
#
#     {'main_collection': 'Men’s Rings, Necklaces & Bracelets', 'sub_collection': 'Rings',
#      'url': "https://uae.souq.com/ae-en/men/rings-284/men/a-t-1780/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Rings, Necklaces & Bracelets', 'sub_collection': 'Necklaces',
#      'url': "https://uae.souq.com/ae-en/men/men/necklaces-285/a-1780 t/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Rings, Necklaces & Bracelets', 'sub_collection': 'Bracelets',
#      'url': "https://uae.souq.com/ae-en/men/men/bracelets-287/a-1780 t/s/?sortby=date_desc"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Square',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/square/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Aviator',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/aviator/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Rectangle',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/rectangle/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Oval',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/oval/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Wayfarer',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/wayfarer/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Wrap Around',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/wrap-around/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Round',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/round/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Rimless',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/rimless/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Sunglasses', 'sub_collection': 'Half Frame',
#      'url': "https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/half-frame/a-t-6356-6265-6572/s/"},
#
#     {'main_collection': 'Men’s Flip-Flops', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/flip-flops/men/a-6356/s/"},
#
#     {'main_collection': 'Men’s Trainers', 'sub_collection': 'Casual Trainers',
#      'url': "https://uae.souq.com/ae-en/sneakers/casual---and---dress-shoes-481/fashion-sneakers/men/a-t-6453-6356/s/?fbs=yes"},
#
#     {'main_collection': 'Men’s Trainers', 'sub_collection': 'Athletic Trainers',
#      'url': "https://uae.souq.com/ae-en/athletic-shoes/athletic-shoes-534/men/a-t-6356/s/?fbs3_ae=yes&ref=nav"},
#
#     {'main_collection': 'Men’s Sandals', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/sandals/men/sandals-479/a-6356-t/s/"},
#
#     {'main_collection': 'Men’s Formal Shoes', 'sub_collection': 'Loafers & Moccasins',
#      'url': "https://uae.souq.com/ae-en/dress-shoes-men/men/loafers---and---moccasian/a-6356-6453/s/"},
#
#     {'main_collection': 'Men’s Formal Shoes', 'sub_collection': 'Oxfords & Wingtips',
#      'url': "https://uae.souq.com/ae-en/dress-shoes-men/men/oxfords---and---wingtip/a-6356-6453/s/"},
#
#     {'main_collection': 'Men’s Formal Shoes', 'sub_collection': 'Slip-Ons',
#      'url': "https://uae.souq.com/ae-en/dress-shoes-men/men/slip-on/a-6356-6453/s/"},
#
#     {'main_collection': 'Men’s Boots', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/boots/boots-469/men/a-t-6356/s/?fbs3_ae=yes&ref=nav"},
#
#     {'main_collection': 'Men’s Holdalls', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/duffle-bag/duffle-bags-559/men/a-t-6356/s/"},
#
#     {'main_collection': 'Men’s Backpacks', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/backpacks/men/a-6356/l/?fbs3_ae=yes&ref=nav&_=1511343167128"},
#
#     {'main_collection': 'Men’s Travel Cases', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/suitcases/trolley-suitcases---and---bags-475/luggage-trolley-bags/men/a-t-5700-6356/s/"},
#
#     {'main_collection': 'Men’s Briefcases & Work Bags', 'sub_collection': None,
#      'url': "https://uae.souq.com/ae-en/briefcase/men/briefcases/a-6356-6328/s/"},
# ]