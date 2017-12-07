__author__ = 'eMaM'


class SouqHelper():
    def __init__(self):
        self.collection_key = 'collections'
        self.sub_collection_key = 'sub_collection'
        self.isFashion_key = 'isFashion'
        self.url_key = 'url'
        self.tags_key = 'tags'
        self.urls_dict = [
            {self.collection_key: "Men's T-Shirts",
             self.sub_collection_key: 'Round Neck',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/round-neck/a-t-6356-6274-6503/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's T-Shirts",
             self.sub_collection_key: 'V Neck',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/l/v-neck/a-t-6356-6274-6315-6503/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's T-Shirts",
             self.sub_collection_key: 'Shirt Neck',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/t--shirts/l/shirt-neck/a-t-6356-6274-6315-6503/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Vests",
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tank-tops/men/tank-tops/a-6356-6274/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Shorts",
             self.sub_collection_key: 'Bermuda Shorts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/bermuda-short/a-t-6356-6335/s/',
             self.tags_key: "Men's, Men's Clothing "},


            {self.collection_key: "Men's Shorts",
             self.sub_collection_key: 'Drawstring Shorts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/drawstring-short/a-t-6356-6335/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Shorts",
             self.sub_collection_key: 'Cargo Shorts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482%7Csportswear-467/men/cargo-short/a-t-6356-6335/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Jeans",
             self.sub_collection_key: 'Slim Fit',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/slim-fit/a-t-6356  6314/s/',
             self.tags_key: "Men's, Men's Clothing "},


            {self.collection_key: "Men's Jeans",
             self.sub_collection_key: 'Straight',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/straight/a-t-6356-6314/s/',
             self.tags_key: "Men's, Men's Clothing "},


            {self.collection_key: "Men's Jeans",
             self.sub_collection_key: 'Skinny',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/skinny/a-t-6356-6314/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Jeans",
             self.sub_collection_key: 'Ripped',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/men/ripped/a-t-6356-6314/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Coats, Jackets & Hoodies",
             self.sub_collection_key: 'Zip Up Hoodie',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/zip-up-hoodie/a-t-6356-6309/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Coats, Jackets & Hoodies",
             self.sub_collection_key: 'Puffer Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/puffer-jacket/a-t-6356-6309/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Coats, Jackets & Hoodies",
             self.sub_collection_key: 'Bomber Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473/men/bomber-jacket/a-t-6356-6309/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Shirts",
             self.sub_collection_key: 'Full Sleeve',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/shirts/full-sleeve/a-t-6356-6274-6490/s/',
             self.tags_key: "Men's, Men's Clothing "},


            {self.collection_key: "Men's Shirts",
             self.sub_collection_key: 'Short Sleeve',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shirts/tops-488%7C467/men/shirts/short-sleeve/a-t-6356-6274-6490/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Suits",
             self.sub_collection_key: 'Tuxedo',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/suits/suits-486/men/tuxedo/a-t-6356-6332/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Suits",
             self.sub_collection_key: 'Business Suit',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/suits/suits-486/men/business-suit/a-t-6356-6332/s/',
             self.tags_key: "Men's, Men's Clothing "},

            {self.collection_key: "Men's Underwear", self.sub_collection_key: 'Boxers', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/underwear/underwear-489/men/boxers/a-t-6356-6337/s/'},
            {self.collection_key: "Men's Underwear", self.sub_collection_key: 'Briefs', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/underwear/underwear-489/men/briefs/a-t-6356-6337/s/'},
            {self.collection_key: "Men's Sportswear", self.sub_collection_key: 'Sports Tops', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-tops/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Sportswear", self.sub_collection_key: 'Sports Shorts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-shorts/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Sportswear", self.sub_collection_key: 'Sports Pants',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-pants/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Sportswear", self.sub_collection_key: 'Sports Jackets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-jackets/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Sportswear", self.sub_collection_key: 'Sports Vests',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/men/sport-vests/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Swimwear", self.sub_collection_key: 'Swim Shorts', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/men/swim-shorts/a-t-6356-6435/s/'},
            {self.collection_key: "Men's Swimwear", self.sub_collection_key: 'Swim Trunks', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/men/swim-trunk/a-t-6356-6435/s/'},
            {self.collection_key: "Men's Belts", self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-belt/belts-557%7Caccessories-466/a-t/s/'},
            {self.collection_key: "Men's Cufflinks", self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: "https://uae.souq.com/ae-en/cufflinks/men%60s-jewelry-292%7Caccessories-466/cufflinks/a-t-6313/s/"},
            {self.collection_key: "Men's Hats", self.sub_collection_key: None, self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-cap-or-hat/hats---and---caps-566/men/baseball---and---snapback-hat/a-t-6356-6573/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Bifold Wallets', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/bifold-wallets/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Card & Id Cases',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/card---and---id-cases/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Trifold Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/trifold-wallets/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Zip Around Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/zip-around-wallets/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Flap Wallets', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/flap-wallets/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Clip Wallet', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/clip-wallet/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Wallets", self.sub_collection_key: 'Travel & Document Holders',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/men-wallet/wallets-533/men/travel---and---document-holders/a-t-6356-5700/s/'},
            {self.collection_key: "Men's Watches", self.sub_collection_key: 'Casual Watch', self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImNhc3VhbCB3YXRjaCJdfX0%3D'},
            {self.collection_key: "Men's Watches", self.sub_collection_key: 'Dress Watch', self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbImRyZXNzIHdhdGNoIl19fQ%3D%3D'},
            {self.collection_key: "Men's Watches", self.sub_collection_key: 'Sport Watch', self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797?q=eyJzIjoiYmVzdCIsImYiOnsiaWRfdHlwZV9pdGVtIjpbIjQ5MCJdLCJzZ2VuX2dlbmRlcl9lbiI6WyJtZW4iXSwic2dlbl93YXRjaF90eXBlX2VuIjpbInNwb3J0IHdhdGNoIl19fQ%3D%3D'},
            {self.collection_key: "Men's Ties", self.sub_collection_key: 'Neck Tie', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/ties/accessories-466/men/neck-ties/a-t-6356-6334/s/'},
            {self.collection_key: "Men's Ties", self.sub_collection_key: 'Bow Tie', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/ties/accessories-466/men/bow-ties/a-t-6356-6334/s/'},
            {self.collection_key: "Men's Rings, Necklaces & Bracelets", self.sub_collection_key: 'Rings',
             self.isFashion_key: False, self.url_key: 'https://uae.souq.com/ae-en/men/rings-284/men/a-t-1780/s/'},
            {self.collection_key: "Men's Rings, Necklaces & Bracelets", self.sub_collection_key: 'Necklaces',
             self.isFashion_key: False, self.url_key: 'https://uae.souq.com/ae-en/men/men/necklaces-285/a-1780 t/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Square', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/square/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Aviator', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/aviator/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Rectangle', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/rectangle/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Oval', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/oval/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Wayfarer', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/wayfarer/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Wrap Around', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/wrap-around/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Round', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/round/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Rimless', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/men/sunglasses/rimless/a-t-6356-6265-6572/s/'},
            {self.collection_key: "Men's Sunglasses", self.sub_collection_key: 'Half Frame', self.isFashion_key: False,
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

            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Blouses',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/blouses/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Blouses"
             },

            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'T-Shirts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/t--shirts/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, T-Shirts"

             },

            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Shirts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/shirts/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Shirts"
             },

            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Crop Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/crop-tops/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Crop Tops"

             },
            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Pull Over Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/pullover-tops/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Pull Over Tops"
             },
            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Long Line Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/long-line-tops/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Long Line Tops"

             },
            {self.collection_key: 'Women`s Tops', self.sub_collection_key: 'Hoodies & Sweatshirts',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/hoodies---and---sweatshirts/a-t-6356-6274/s/'},

            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Cami & Strappy Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/cami---and---strappy-tops/a-t-6356-6274/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Cami & Strappy Tops"
             },

            {self.collection_key: 'Women`s Tops',
             self.sub_collection_key: 'Tank Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/tops/tops-488/women%7Cwomens/tank-tops/a-t-6356-6274/s/',
             self.tags_key: "Middle East, Souq.com, Women's, Women's Clothing, Women's Tops, Tank Tops"
             },

            {self.collection_key: 'Women`s Trousers & Leggings',
             self.sub_collection_key: 'Trousers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/pants/pants-477/women/trousers/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Trousers & Leggings, Trousers"
             },

            {self.collection_key: 'Women`s Trousers & Leggings',
             self.sub_collection_key: 'Leggings',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/pants/pants-477/women/leggings/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Trousers & Leggings, Leggings"

             },
            {self.collection_key: 'Women`s Shorts',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/shorts/shorts-482/women/a-t-6356/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Shorts"},

            {self.collection_key: 'Women`s Jeans',
             self.sub_collection_key: 'Skinny',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/skinny/a-t-6356-5700-6314/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Jeans, Skinny"},

            {self.collection_key: 'Women`s Jeans', self.sub_collection_key: 'Slim Fit', self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/slim-fit/a-t-6356-5700-6314/s/'},

            {self.collection_key: 'Women`s Jeans',
             self.sub_collection_key: 'Straight',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/straight/a-t-6356-5700-6314/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Jeans, Straight"},

            {self.collection_key: 'Women`s Jeans',
             self.sub_collection_key: 'Ripped',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jeans/pants-477/women/jeans/ripped/a-t-6356-5700-6314/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Jeans, Ripped"},

            {self.collection_key: 'Women`s Dresses',
             self.sub_collection_key: 'Bodycon',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dresses/dresses-465/women/bodycon/a-t-6356-6269/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Dresses, Bodycon"},

            {self.collection_key: 'Women`s Dresses',
             self.sub_collection_key: 'A-Line',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dresses/dresses-465/women/a-line/a-t-6356-6269/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Dresses, A-Line"},


            {self.collection_key: 'Women`s Dresses',
             self.sub_collection_key: 'Straight Fit',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/dresses/dresses-465/women/straight/a-t-6356-6269/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Dresses, Straight Fit"},

            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Cardigan',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/cardigan/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Cardigan"},


            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Blazer',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/blazer/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Blazer"},

            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Zip Up Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/zip-up-jacket/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Zip Up Jacket"},

            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Biker Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/biker-jacket/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Biker Jacket"},

            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Bomber Jacket',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/bomber-jacket/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Bomber Jacket"},


            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Zip Up Hoodie',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/zip-up-hoodie/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Zip Up Hoodie"},

            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Shrugs',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/shrugs/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Shrugs"},

            {self.collection_key: 'Women`s Coats & Jackets', self.sub_collection_key: 'Trench Coat',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jackets/jackets---and---coats-473%7Csportswear-467/women/trench-coat/a-t-6356-6309/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Coats & Jackets, Trench Coat"},


            {self.collection_key: 'Women`s Jumpsuits & Rompers', self.sub_collection_key: 'Jumpsuit',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jumpsuit/jumpsuits,-rompers---and---overalls-563/women/jumpsuit/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Jumpsuits & Rompers, Jumpsuit"},

            {self.collection_key: 'Women`s Jumpsuits & Rompers', self.sub_collection_key: 'Romper',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jumpsuit/jumpsuits,-rompers---and---overalls-563/women/romper/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Jumpsuits & Rompers, Romper"},


            {self.collection_key: 'Women`s Jumpsuits & Rompers', self.sub_collection_key: 'Overalls',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/jumpsuit/jumpsuits,-rompers---and---overalls-563/women/overall/a-t-6356-5700/s/'},

            {self.collection_key: 'Women`s Lingerie',
             self.sub_collection_key: 'Bras',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/bra/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Bras"},


            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Lingerie Dresses',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/lingerie-dresses/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Lingerie Dresses"},

            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Lingerie Panties',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/lingerie-panties/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Lingerie Panties"},


            {self.collection_key: 'Women`s Lingerie',
             self.sub_collection_key: 'Babydolls',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/babydolls---and---playsuits/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Babydolls"},


            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Lingerie Sets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/lingerie-set/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Lingerie sets"},



            {self.collection_key: 'Women`s Lingerie', self.sub_collection_key: 'Bustiers & Corsets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/bustiers---and---corsets/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Bustiers & Corsets "},


            {self.collection_key: 'Women`s Lingerie',
             self.sub_collection_key: 'Camisoles & Chemises',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/lingerie/womens-lingerie-348/camisoles---and---chemises/a-t-6307/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Lingerie, Camisoles & Chemises "},

            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sport Tops',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-tops/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Sportswear, Sports Tops"},

            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sport Bottoms',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-pants/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Sportswear, Sports Bottoms"},


            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sports Bras',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-bras/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Sportswear, Sports Bras"},


            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sports Suits',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-suits/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Sportswear, Sports Suits"},


            {self.collection_key: 'Women`s Sportswear', self.sub_collection_key: 'Sports Jackets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sportswear/sportswear-467/women/sport-jackets/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Sportswear, Sports Jackets"},


            {self.collection_key: 'Women`s Skirts',
             self.sub_collection_key: 'Bodycon',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/skirts/skirts-483/women/body-con/a-t-6356-6308/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Skirts, Bodycon"},


            {self.collection_key: 'Women`s Skirts',
             self.sub_collection_key: 'A-Line',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/skirts/skirts-483/women/a-line/a-t-6356-6308/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Skirts, A-Line"},

            {self.collection_key: 'Women`s Skirts',
             self.sub_collection_key: 'Straight Fit',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/skirts/skirts-483/women/straight/a-t-6356-6308/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Skirts, Straight Fit"},

            {self.collection_key: 'Women`s Swimwear',
             self.sub_collection_key: 'Bikini Sets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/bikini-set/a-t-6356-6435/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Swimwear, Bikini Sets"},


            {self.collection_key: 'Women`s Swimwear',
             self.sub_collection_key: 'Bikinis',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/bikinis/a-t-6356-6435/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Swimwear, Bikinis "},


            {self.collection_key: 'Women`s Swimwear', self.sub_collection_key: 'Sarong & Cover Ups',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/sarong---and---cover-ups/a-t-6356-6435/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Swimwear, Sarong & Cover Ups"},


            {self.collection_key: 'Women`s Swimwear', self.sub_collection_key: 'One Piece & Molokini`s',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/swimwear/swimwear-487/women/one--pieces---and---monokinis/a-t-6356-6435/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Clothing, Women's Swimwear, One Piece & Monokini's"},


            {self.collection_key: 'Women`s Belts',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/belts/women/a-6356/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Belts"},


            {self.collection_key: 'Women`s Watches', self.sub_collection_key: None, self.isFashion_key: True,
             self.url_key: 'https://fashion.souq.com/ae-en/search?campaign_id=3797&tag_id=4012'},
            {self.collection_key: 'Women`s Hats',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/hats/hats---and---caps-566/women/baseball---and---snapback-hat/a-t-6356-6573/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Hats"},


            {self.collection_key: 'Women`s Purses & Wallets',
             self.sub_collection_key: 'Zip Around Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/zip-around-wallets/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Zip Around Wallets "},

            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Bifold Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/bifold-wallets/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Bifold Wallets "},

            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Flap Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/flap-wallets/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Flap Wallets "},

            {self.collection_key: 'Women`s Purses & Wallets', self.sub_collection_key: 'Trifold Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/trifold-wallets/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Trifold Wallets "},


            {self.collection_key: 'Women`s Purses & Wallets',
             self.sub_collection_key: 'Casual Wallets',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/casual-wallets/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Casual Wallets "},

            {self.collection_key: 'Women`s Purses & Wallets',
             self.sub_collection_key: 'Card & Id Cases',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/card---and---id-cases/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Card & Id Cases "},


            {self.collection_key: 'Women`s Purses & Wallets',
             self.sub_collection_key: 'Coin Purses & Pouches',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-wallet/wallets-533%7Caccessories-466%7Chandbags-472/women/coin-purses---and---pouches/a-t-6356-5700/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Purses & Wallets, Coin Purses & Pouches "},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Cat Eye',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/cat-eye/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Cat Eye"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Square',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/square/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Square"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Oval',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/oval/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Oval"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Round',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/round/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Round"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Aviator',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/aviator/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Aviator"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Wayfarer',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/wayfarer/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Wayfarer"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Rectangle',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/rectangle/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Rectangle"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Butterfly',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/butterfly/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Butterfly"},


            {self.collection_key: 'Women`s Sunglasses',
             self.sub_collection_key: 'Oversized',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/eyewear/eyewear-433/women/sunglasses/oversized/a-t-6356-6265-6572/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Accessories, Women's Sunglasses, Oversized "},


            {self.collection_key: 'Women`s Rings',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-rings/rings-284/women/swarovski%7Cmichael-kors%7Cvera-perla%7Cpandora%7Cemporio-armani/a-t-1780-7/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Jewellery, Women's Rings"},


            {self.collection_key: 'Women`s Necklaces',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women/necklaces-285/swarovski%7Cfossil%7Cemporio-armani%7Cguess%7Cswarovski-elements%7Cmichael-kors%7Cvera-perla%7Csteve-madden%7Cjuicy-couture/a-t-7/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Jewellery, Women's Necklaces"},

            {self.collection_key: 'Women`s Bracelets',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-bracelet/bracelets-287/women/kate-spade%7Cfossil%7Cpandora%7Cswarovski%7Cswarovski-elements%7Cmichael-kors%7Cguess/a-t-1780-7/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Jewellery, Women's Bracelets"},


            {self.collection_key: 'Women`s Earrings',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/women-earring/earrings-286/kate-spade%7Cswarovski%7Cvera-perla%7Cpandora%7Cfossil%7Cmichael-kors%7Cemporio-armani%7Cswarovski-elements/a-t-7/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Jewellery, Womens Earrings"},


            {self.collection_key: 'Women`s Trainers', self.sub_collection_key: 'Athletic Trainers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/athletic-shoes/athletic-shoes-534/women/a-t-6356/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Shoes, Women's Trainers, Athletic Trainers"},


            {self.collection_key: 'Women`s Trainers',
             self.sub_collection_key: 'Casual Trainers',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/sneakers/women/casual---and---dress-shoes-481/a-6356-t/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Shoes, Women's Trainers, Casual Trainers"},

            {self.collection_key: 'Women`s Trainers',
             self.sub_collection_key: 'Women`s Heels',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/heels/women/heels/casual---and---dress-shoes-481%7C469/a-6356-6453-t/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Shoes, Women's Heels"},

            {self.collection_key: 'Women`s Flats',
             self.sub_collection_key: None,
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/flats/casual---and---dress-shoes-481%7Csandals-479/women/flat/a-t-6356-6453/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Shoes, Women's Flats"},


            {self.collection_key: 'Women`s Boots',
             self.sub_collection_key: 'Heels Boots',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/boots/boots-469/women/heels-boots/a-t-6356-6437/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Shoes, Women's Boots, Heels Boots"},


            {self.collection_key: 'Women`s Boots',
             self.sub_collection_key: 'Pull on Boots',
             self.isFashion_key: False,
             self.url_key: 'https://uae.souq.com/ae-en/boots/boots-469/women/pull-on-boots/a-t-6356-6437/s/',
             self.tags_key:"Middle East, Souq.com, Women's, Women's Shoes, Women's Boots, Pull On Boots"},

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