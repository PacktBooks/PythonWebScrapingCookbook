from scrapy.selector import Selector
import requests

response = requests.get("http://stackoverflow.com/questions")

selector = Selector(response)
selector

summaries = selector.xpath('//div[@class="summary"]/h3')
summaries[0:5]


[x.extract() for x in summaries.xpath('a[@class="question-hyperlink"]/text()')][:10]
