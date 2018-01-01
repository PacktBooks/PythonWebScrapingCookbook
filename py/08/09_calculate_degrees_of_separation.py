import imdb.strategies
import imdb.relationship_crawler
import networkx as nx
import matplotlib.pyplot as plt
import imdb.models

if __name__ == "__main__":
    crawler = imdb.relationship_crawler.ImdbRelationshipCrawler("Kevin Bacon",
                                                                2,  # max depth
                                                                5,  # max titles per actor
                                                                3,  # max actors per title
                                                                50,  # max total actors
                                                                50,  # max total titles
                                                                50,  # max actors per depth
                                                                50)  # max titles per depth
    crawler.crawl()

    for relationship in crawler.relationships.values():
        print(relationship)

    g = nx.Graph()

    for actor in crawler.actors.values(): g.add_node(actor)
    for title in crawler.titles.values(): g.add_node(title)

    for relationship in crawler.relationships.values():
        g.add_edge(relationship.from_actor, relationship.via_title)
        g.add_edge(relationship.via_title, relationship.to_actor)

    # find the Michael Douglas actor object
    to = [n for n in crawler.actors.values() if n.name == "Michael Douglas"][0]

    # calculate degrees of separation
    path = nx.astar_path(g, crawler.start_actor, to)

    # report
    degrees_of_separation = int((len(path) - 1) / 2) - 1
    print("Degrees of separation: {}".format(degrees_of_separation))
    for i in range(0, len(path)):
        print(" " * i, path[i].name)
