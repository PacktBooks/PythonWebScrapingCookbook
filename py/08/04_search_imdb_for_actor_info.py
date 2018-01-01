import imdb.strategies

if __name__ == "__main__":
    search_results = imdb.strategies.search_for_actor_result_html("Kevin Bacon")
    actor_info = imdb.strategies.extract_actor_info_from_search_result(search_results)
    print(actor_info)


