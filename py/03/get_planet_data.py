import requests
from bs4 import BeautifulSoup

def get_planet_data():
	html = requests.get("http://localhost:8080/planets.html").text
	soup = BeautifulSoup(html, "lxml")

	planet_trs = soup.html.body.div.table.findAll("tr", {"class": "planet"})

	def to_dict(tr):
		tds = tr.findAll("td")
		planet_data = dict()
		planet_data['Name'] = tds[1].text.strip()
		planet_data['Mass'] = tds[2].text.strip()
		planet_data['Radius'] = tds[3].text.strip()
		planet_data['Description'] = tds[4].text.strip()
		planet_data['MoreInfo'] = tds[5].findAll("a")[0]["href"].strip()
		return planet_data

	planets = [to_dict(tr) for tr in planet_trs]

	return planets

if __name__ == "__main__":
	print(get_planet_data())
