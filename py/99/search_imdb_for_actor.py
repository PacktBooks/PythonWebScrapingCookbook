import requests
from urllib import parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
import os
from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt
import networkx as nx

class ImdbActorInfo:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class ImdbTitleInfo:
    def __init__(self, name, id, year):
        self.name = name
        self.id = id
        self.year = year

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def search_imdb_for_actor(actor_name):
    url_encoded_name = parse.urlencode({"q": actor_name})
    print(url_encoded_name)
    search_url = "http://www.imdb.com/find?ref_=nv_sr_fn&s=nm&%s" % url_encoded_name

    html = requests.get(search_url)

    soup = BeautifulSoup(html.text, "lxml")
    row = soup.find("td", {"class": "result_text"})
    anchor = row.find("a")

    if str(anchor.text).lower() == actor_name.lower():
        path = urlparse(anchor["href"]).path
        return ImdbActorInfo(actor_name, os.path.split(os.path.split(path)[0])[1])

    return None

def get_imdb_actor_page_html(actor_info):
    actor_url = "http://www.imdb.com/name/%s" % actor_info.id
    return requests.get(actor_url).text

def get_title_html(title):
    title_url = "http://www.imdb.com/title/%s" % title.id
    return requests.get(title_url).text

def get_acted_in_info(actor_page_html):
    soup = BeautifulSoup(actor_page_html, "lxml")
    filmo = soup.find("div", {"class": "filmo-category-section"})

    titles = []

    for row in filmo.find_all("div", {"class": "filmo-row"}):
        anchor = row.find("a")

        path = urlparse(anchor["href"]).path
        id = os.path.split(os.path.split(path)[0])[1]
        title = anchor.text
        year = row.find("span", {"class": "year_column"}).text.strip()
        titles.append(ImdbTitleInfo(title, id, year))

    return titles;

def get_cast_from_title_html(title_page_html):
    soup = BeautifulSoup(title_page_html, "lxml")
    cast_list_table = soup.find("table", {"class": "cast_list"})

    cast = []

    items = cast_list_table.find_all("td", {""})
    for item in cast_list_table.find_all("td", {"class": "itemprop", "itemprop": "actor"}):
        anchor = item.find("a", {"itemprop": "url"})

        path = urlparse(anchor["href"]).path
        id = os.path.split(os.path.split(path)[0])[1]
        name = item.find("span", {"class": "itemprop", "itemprop": "name"}).text
        actor = ImdbActorInfo(name, id)
        cast.append(actor)

        print(actor)

    return cast

if __name__ == "__main__":
    actor_info = search_imdb_for_actor("Kevin Bacon")

    actor_page_html = get_imdb_actor_page_html(actor_info)
    acted_in = get_acted_in_info(actor_page_html)
    title_page_html = get_title_html(acted_in[0])
    cast = get_cast_from_title_html(title_page_html)

    es = Elasticsearch(['localhost'], http_auth=('scraping', 'scraping'))

    for cast_member in cast:
        #print(cast_member)
        #es.index(index='imdb_actors', doc_type='imdb_actor', id=cast_member.id, body=str(cast_member))
        pass

    for title in acted_in:
        #es.index(index='imdb_titles', doc_type='imdb_title', id=title.id, body=str(title))
        pass

    g = nx.Graph()
    g.add_node(actor_info)
    cast_nodes = [cm for cm in cast if cm.id != actor_info.id]
    g.add_nodes_from(cast_nodes)
    g.add_edges_from([(actor_info, cm) for cm in cast])

    print("drawing network")
    print(g.nodes())
    pos = nx.spring_layout(g)
    d = {n : n.name for n in g.nodes()}
    print(d)
    nx.draw_networkx_nodes(g,  pos, d, node_color='green', node_size=700)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g,  pos, d)
    plt.show()