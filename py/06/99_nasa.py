import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class Spider(scrapy.spiders.CrawlSpider):
    name = 'spider'
    start_urls = ['https://stackoverflow.com/jobs']
    #allowed_domains=['nasa.gov']
    rules = (
        Rule(LinkExtractor(allow=()), callback='parse', follow=True),
             )

    def parse(self, response):
        print(response)

if __name__ == "__main__":
    process = CrawlerProcess({
        'LOG_LEVEL': 'DEBUG'
    })
    process.crawl(Spider)
    process.start()
