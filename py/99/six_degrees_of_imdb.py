import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class Spider(scrapy.spiders.SitemapSpider):
    name = 'spider'
    sitemap_urls = ['https://www.nasa.gov/sitemap.xml']
    allowed_domains=['nasa.gov']

    def parse(self, response):
        print("Parsing: ", response)
        sel = Selector(response)
        items = sel.xpath("//*/a").extract()
        for i in items:
            print(i)

if __name__ == "__main__":
    process = CrawlerProcess({
        'LOG_LEVEL': 'DEBUG',
#        'DEPTH_LIMIT': 10,
#        'DEPTH_STATS': True,
#        'CLOSESPIDER_PAGECOUNT': 30
    })

    process.crawl(Spider)
    spider = next(iter(process.crawlers)).spider
    process.start()
    stats = spider.stats
    print(stats)
    print(spider.crawled_urls)