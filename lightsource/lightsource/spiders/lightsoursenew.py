import scrapy

class LightsoursenewSpider(scrapy.Spider):
    name = "lightsoursenew"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/kemerovo/category/svet"]

    def parse(self, response):
        lihts = response.css('_Ud0k')
        for light in lihts:
            yield {'name':light.css('div.lsooF span::text').get(),
                   'price': light.css('div.pY3d2 span::text').get(),
                   'url': light.css('a').attrib['href']
                   }
