import scrapy
import json

class ClothingDescriptionSpdider(scrapy.Spider):
    name = "clothing"
    start_urls = [
        'https://api-cdn.chumbak.com/v1/category/474/products/',
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        next_page = jsonresponse['product_pages']['next_page']
        count_per_page = 20
        products = jsonresponse['products']
        print(json.dumps(products, indent=2))
