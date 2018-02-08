from lxml import html
import requests
page_html = requests.get("http://localhost:8080/planets.html").text
tree = html.fromstring(page_html)

[(v, v.xpath("@name")) for v in tree.cssselect('tr.planet')]

tr = tree.cssselect("tr#planet3")
tr[0], tr[0].xpath("./td[2]/text()")[0].strip()

tr = tree.cssselect("tr[name='Pluto']")
tr[0], tr[0].xpath("td[2]/text()")[0].strip()