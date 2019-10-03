

from scrapy.selector import Selector
from scrapy import Spider
import scrapy
from isoSpider.items import IsospiderItem

class isoSpider(Spider):
    name = "get_iso"
    start_urls= ['https://www.iso.org/ics/21.020/x/']



    def parse(self, response):
        item = IsospiderItem()
        item['iso_num']= response.css('.entry-name a::attr(title)').extract()
        yield item