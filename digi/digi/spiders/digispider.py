import scrapy
from utility.helpful_scripts import fixing_numbers
import json


class DigispiderSpider(scrapy.Spider):
    name = 'digispider'
    allowed_domains = ['digikala.com']
    start_urls = ['https://www.digikala.com/main/electronic-devices/']

    def __init__(self):
        self.data = {}

    def parse(self, response):
        tags = response.xpath('//*[@class="c-price__value c-price__value--plp"]/del/text()').extract()
        for index in range(len(tags)):
            result = fixing_numbers(tags[index])
            self.data[index] = result
        with open('data.json', 'w') as f:
            f.write(json.dumps(self.data))
