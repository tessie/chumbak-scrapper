import scrapy
import json
from urllib import urlencode


class ClothingDescriptionSpdider(scrapy.Spider):
    name = "clothing"
    start_urls = [
        'https://api-cdn.chumbak.com/v1/category/474/products/',
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        has_next = jsonresponse['product_pages']['has_next']
        url = 'https://api-cdn.chumbak.com/v1/category/474/products?'
        products = jsonresponse['products']
        print(json.dumps(products, indent=2))
        if has_next != 0:
            next_page = jsonresponse['product_pages']['next_page']
            params = urlencode({"page": next_page, "count_per_page": 20})
            url = url + params
            yield scrapy.Request(
                    url,
                    callback=self.parse
                )
