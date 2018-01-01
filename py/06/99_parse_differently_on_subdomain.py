import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class Spider(scrapy.spiders.CrawlSpider):
    name = 'spider'
    #start_urls = ['http://localhost:5001/CrawlDepth0-1.html']
    #start_urls = ["https://antonio-maiolo.com/"]
    allowed_domains=['nasa.gov']

 #        Rule(LinkExtractor(allow=('CrawlDepth*')), callback='parse_mission_pages', follow=True),
    rules = [Rule(LinkExtractor(allow=()), callback='parse_mission_pages', follow=True)]

    def parse(self, response):
        print("Parsing non-mission page: ", response)

    def parse_mission_pages(self, response):
        print("Parsing mission page: ", response)

if __name__ == "__main__":
    process = CrawlerProcess({
        'LOG_LEVEL': 'DEBUG'
    })
    process.crawl(Spider)
    process.start()
