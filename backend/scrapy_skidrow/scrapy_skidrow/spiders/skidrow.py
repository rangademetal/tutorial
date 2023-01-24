import scrapy
from ..items import ScrapySkidrowItem
from scrapy.utils.log import configure_logging
import logging


class SkidrowSpider(scrapy.Spider):
    name = 'skidrow'
    allowed_domains = ['https://www.skidrowreloaded.com/pc/']
    start_urls = ['https://www.skidrowreloaded.com/pc/']

    configure_logging(install_root_handler=False)
    logging.basicConfig(filename="/home/sad/PycharmProject/rest/logs/skidrow_data.log",
                        format='%(asctime)s %(message)s', level=logging.INFO,
                        filemode='a')

    async def parse(self, response):
        item = ScrapySkidrowItem()
        for game in range(1, 251):
            item['id'] = str(game)
            item['name'] = response.xpath(f'/html/body/div/div[3]/div[1]/div[1]/ul[1]/li[{game}]/a//text()').get()
            item['link'] = response.xpath(f'/html/body/div/div[3]/div[1]/div[1]/ul[1]/li[{game}]/a/@href').get()

            yield item
        next_page = response.css('.lcp_nextlink').attrib['href']
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
