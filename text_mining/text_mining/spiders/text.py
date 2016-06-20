from text_mining.items import TextMiningItem
from scrapy.contrib.spiders import CrawlSpider, Rule
import json
#coding=utf-8
urls = []
f = open('usa.json')
links = json.load(f)
for url in links:
    urls.append(url[u'link'])
#print urls

class TextSpider(CrawlSpider):
    name = "text"
    allowed_domains = ["usatoday.com"]
    start_urls = urls

    def parse(self, response):

        for sel in response.xpath('//p//text()').extract():
            print sel
            torrent = TextMiningItem()
            torrent['desc'] = sel
            yield torrent

