import requests
from bs4 import BeautifulSoup
html = requests.get("http://localhost:8080/planets.html").text
soup = BeautifulSoup(html, "lxml")

table = soup.find("table")
str(table)[:100]

[str(tr)[:50] for tr in table.findAll("tr")]

table.find("tr", {"id", "planet3"})

items = dict()
planet_rows = table.findAll("tr", {"class": "planet"})
for i in planet_rows:
    tds = i.findAll("td")
    items[tds[1].text.strip()] = tds[2].text.strip()