from django.contrib import admin
from .models import *

admin.site.register((MainCategory,
                    SubCategory,
                    Product,
                    Brand,
                    Seller,
                    Buyer,
                    WishList,
                    CheckOut,
                    ContactUs,
                    NewsLetter
                    ))
