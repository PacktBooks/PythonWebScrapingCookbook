import imdb.strategies
import imdb.relationship_crawler
import networkx as nx
import matplotlib.pyplot as plt
import imdb.models

if __name__ == "__main__":
    crawler1 = imdb.relationship_crawler.ImdbRelationshipCrawler("Kevin Bacon",
                                                                 1,  # max depth
                                                                 5,  # max titles per actor
                                                                 5,  # max actors per title
                                                                 50,  # max total actors
                                                                 50,  # max total titles
                                                                 50,  # max actors per depth
                                                                 50) # max titles per depth

    crawler2 = imdb.relationship_crawler.ImdbRelationshipCrawler("Kevin Bacon",
                                                                 2, # max depth
                                                                 5, # max titles per actor
                                                                 3, # max actors per title
                                                                 50, # max total actors
                                                                 50, # max total titles
                                                                 50, # max actors per depth
                                                                 50) # max titles per depth
    crawler = crawler2
    crawler.crawl()

    for relationship in crawler.relationships.values():
        print(relationship)

    g = nx.Graph()

    for actor in crawler.actors.values(): g.add_node(actor)
    for title in crawler.titles.values(): g.add_node(title)

    for relationship in crawler.relationships.values():
        g.add_edge(relationship.from_actor, relationship.via_title)
        g.add_edge(relationship.via_title, relationship.to_actor)

    plt.figure(figsize=(10,8))

    node_positions = nx.spring_layout(g)

    nx.draw_networkx_nodes(g, node_positions, crawler.actors.values(), node_color='green', node_size=200)
    nx.draw_networkx_nodes(g, node_positions, crawler.titles.values(), node_color='red', node_size=100)

    nx.draw_networkx_edges(g, node_positions)

    labels = { node: node.name for node in g.nodes() }
    nx.draw_networkx_labels(g, node_positions, labels, font_size=10)

    plt.show()
