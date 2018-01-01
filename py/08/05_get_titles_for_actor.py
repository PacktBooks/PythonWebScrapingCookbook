import imdb.strategies

if __name__ == "__main__":
    search_results = imdb.strategies.search_for_actor_result_html("Kevin Bacon")
    actor_info = imdb.strategies.extract_actor_info_from_search_result(search_results)

    actor_page_html = imdb.strategies.get_actor_page_html(actor_info)
    actor_acted_in = imdb.strategies.extract_acted_in_titles(actor_page_html)

    actor_info.set_titles(actor_acted_in)
    for title_id in actor_info.titles:
        print(actor_info.titles[title_id])
