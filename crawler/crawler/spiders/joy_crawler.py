import scrapy


class JoySpider(scrapy.Spider):
    name = "joy"
    start_urls = ['https://karnaval.com/radyolar/joyfm']

    def parse(self, response):

        yield {
            'song': response.css('div.station_now_playing_container').css('span.title::text').extract(),
            'artist': response.css('div.station_now_playing_container').css('span.sub_title::text').extract(),

        }

