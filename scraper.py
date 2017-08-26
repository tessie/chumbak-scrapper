import scrapy
import json


class ClothingDescriptionSpdider(scrapy.Spider):
    name = "clothing"
    start_urls = [
        'https://api-cdn.chumbak.com/v1/category/474/products/',
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        # current_page = json['product_pages']['current_page']
        products = jsonresponse['products']
        for product in products:
            print product
