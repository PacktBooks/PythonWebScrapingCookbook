import imdb.strategies

if __name__ == "__main__":
    title_html = imdb.strategies.get_title_page_html("tt5886510")
    actors = imdb.strategies.extract_actors_for_title(title_html)
    for actor in actors:
        print(actor)
