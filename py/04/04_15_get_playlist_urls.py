from bs4 import BeautifulSoup
from selenium import webdriver

pl_url = "https://www.youtube.com/watch?v=WbsC_fGArVc&list=RDWbsC_fGArVc"

driver = webdriver.PhantomJS()
driver.set_script_timeout(30)
driver.get(pl_url)

html = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")
print(html)

bsobj = BeautifulSoup(html, "lxml")
playlist_anchors = bsobj.findAll("a", {"class": " spf-link playlist-video clearfix yt-uix-sessionlink spf-link "})
for a in playlist_anchors:
    print ("https://www.youtube.com/" + a['href'])
