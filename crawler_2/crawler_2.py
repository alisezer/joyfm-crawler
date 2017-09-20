import scrapy
from scrapy.crawler import CrawlerProcess


class JoySpider(scrapy.Spider):
    name = "joyfm"
    start_urls = ['https://karnaval.com/radyolar/joyfm']

    def parse(self, response):

        yield [
            response.css('div.station_now_playing_container').css('span.title::text').extract(),
            response.css('div.station_now_playing_container').css('span.sub_title::text').extract()]


process = CrawlerProcess()
process.crawl(JoySpider)
process.start()
process.stop()
