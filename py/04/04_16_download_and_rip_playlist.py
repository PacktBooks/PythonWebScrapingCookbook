from core.youtube_playlist_crawler import YouTubePlaylistCrawler
from os.path import expanduser

crawler = YouTubePlaylistCrawler()
crawler.crawl_playlist("https://www.youtube.com/watch?v=WbsC_fGArVc&list=RDWbsC_fGArVc",
                       getThumbnails=True,
                       location=expanduser("~") + "/youtuberips",
                       createHTML=True)