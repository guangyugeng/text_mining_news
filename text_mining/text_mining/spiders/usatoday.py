import scrapy
#coding=utf-8
import re
from text_mining.items import TextMiningItem

class DmozSpider(scrapy.Spider):

    name = "usatoday"
    allowed_domains = ["usatoday.com"]
    start_urls = [ "http://www.usatoday.com/news/nation/"
    ]

    def parse(self, response):

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

       # print 1
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print link

            for w in link:
                m = re.search(u"^/story/news/nation.*", w)
                if m != None:

                    torrent = TextMiningItem()
                    torrent['link'] = "http://www.usatoday.com"+m.group()
                    yield torrent

