from lxml import html
import requests
page_html = requests.get("http://localhost:8080/planets.html").text

tree = html.fromstring(page_html)

[tr for  tr in tree.xpath("/html/body/div/table/tr")]

from lxml import etree
[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr[@class='planet']")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[1]/table/tr")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[2]/table/tr")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[@id='planets']/table/tr")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[@id='planets']/table/tr[@id!='planetHeader']")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div[@id='planets']/table/tr[position() > 1]")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr/parent::*")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr/parent::table")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr/parent::table[@id='footerTable']")]

[etree.tostring(tr)[:50] for tr in tree.xpath("/html/body/div/table/tr/..")]

mass = tree.xpath("/html/body/div[1]/table/tr[@name='Earth']/td[3]/text()[1]")[0].strip()
mass