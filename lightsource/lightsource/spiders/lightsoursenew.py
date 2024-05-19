import scrapy


class LightsoursenewSpider(scrapy.Spider):
    name = "lightsoursenew"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/kemerovo/category/svet"]

    def parse(self, response):
        pass
