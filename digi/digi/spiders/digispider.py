import scrapy
from utility.helpful_scripts import fixing_numbers
import requests
from requests.structures import CaseInsensitiveDict
import json


class DigispiderSpider(scrapy.Spider):
    name = 'digispider'
    allowed_domains = ['digikala.com']
    start_urls = ['https://www.digikala.com/main/electronic-devices/']

    def parse(self, response):
        tags = response.xpath('//*[@class="c-price__value c-price__value--plp"]/del/text()').extract()
        names = response.xpath('//*[@class="c-super-deal__main-title"]/text()').extract()
        for index in range(len(tags)):
            result = fixing_numbers(tags[index])
            data = {"name": names[index], "price": result}
            headers = CaseInsensitiveDict()
            token = '7459202cbf5bf0cb10c6826bd1a92f7f698c2b6d'
            headers["Accept"] = "application/json"
            headers["Authorization"] = f"Token {token}"
            x = requests.post("http://localhost:8000/api/", data=data, headers=headers)
            print(x)
