from scrapy import log
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from songhelper.items import SongItem

class SongSpider(CrawlSpider):
    name = 'songhelper'
    home = 'http://www.last.fm'

    def __init__(self, artist='', *args, **kwargs):
        super(SongSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.last.fm/search?q={}'.format(artist)
            ]

    def parse_start_url(self, response):
        sel = Selector(response)

        # choose first link (top result)
        try:
            select_a = sel.xpath('//a[@class="link-block-target"]/@href').extract()[0]
            artist_link = self.home + select_a
        except IndexError:
            self.log('Could not match any items.',
                     level=log.ERROR)
            return

        artist_name = sel.xpath('//a[@class="link-block-target"]/text()').extract()[0]

        if ' - ' in artist_name:
            self.log('Found song: ' + artist_name)
            return
        else:
            self.log('Found artist: ' + artist_name)
            artist_link += '/+similar'
            return Request(url=artist_link, callback=self.get_artists)

    def get_artists(self, response):
        self.log('Finding similar artists...')

        sel = Selector(response)
        artists = sel.xpath('//a[@class="link-block-target"]/@href').extract()[:5]

        # Top 5 similar artists
        names = sel.xpath('//a[@class="link-block-target"]/text()').extract()[:5]

        for artist in artists:
            artist_link = self.home + artist
            yield Request(artist_link, callback=self.get_songs)

    def get_songs(self, response):
        sel = Selector(response)

        items = []
        artist = sel.xpath('//h1[@class="header-title"]/text()').extract()[0].strip()
        links = sel.xpath('//a[@class="chartlist-play-button js-playlink"]/@href').extract()
        names = sel.xpath('//span[@class="chartlist-ellipsis-wrap"]/a/@title').extract()

        for name,link in zip(names, links):
            item = SongItem()
            item['artist'] = artist
            item['name'] = name
            item['link'] = link

            items.append(item)
        return items
