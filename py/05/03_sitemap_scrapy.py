import scrapy
from scrapy.crawler import CrawlerProcess

class Spider(scrapy.spiders.SitemapSpider):
    name = 'spider'
    sitemap_urls = ['https://www.nasa.gov/sitemap.xml']

    def parse(self, response):
        print("Parsing: ", response)

if __name__ == "__main__":
    process = CrawlerProcess({
        'DOWNLOAD_DELAY': 0,
        'LOG_LEVEL': 'DEBUG'
    })
    process.crawl(Spider)
    process.start()