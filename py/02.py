#%% 
import requests
response = requests.get("http://127.0.0.1:8080/pages/planets.html")
response.text

#%%
from scrapy.selector import Selector
import requests
from urllib.request import urlopen
payload = { 'pagesize': 1, 'sort': 'newest'}
response = requests.get("http://stackoverflow.com/questions", params=payload)
response.url
selector = Selector(response)
selector
summaries = selector.xpath('//div[@class="summary"]/h3')
summaries[0:5]