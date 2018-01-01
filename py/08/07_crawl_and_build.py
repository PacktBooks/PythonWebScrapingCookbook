import imdb.strategies
import imdb.relationship_crawler

if __name__ == "__main__":
    crawler = imdb.relationship_crawler. \
        ImdbRelationshipCrawler("Kevin Bacon",
                                1,  # max depth
                                5,  # max titles per actor
                                5,  # max actors per title
                                50, # max total actors
                                50, # max total titles
                                50, # max actors per depth
                                50) # max titles per depth
    crawler.crawl()

    for relationship in crawler.relationships.values():
        print(relationship)