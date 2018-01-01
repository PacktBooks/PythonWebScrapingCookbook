from bs4 import BeautifulSoup
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tech2grams import tech_2grams
from punctuation import remove_punctuation
import requests
import urllib
import os
from stack_overflow_job_listing_es import StackOverflowJobListingElasticSearchFacade

from urllib.parse import urlparse

class StackOverflowJobListing(object):
    def __init__(self, url, id, html, clean, json):
        self._url = url
        self._html = html
        self._clean = clean
        self._json = json
        self._id = id

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value

    @property
    def clean(self):
        return self._clean

    @clean.setter
    def clean(self, value):
        self._clean = value

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


class StackOverflowStrategies(object):
    @classmethod
    def get_job_listing_html(cls, url):
        r = requests.get(url)
        html = r.text
        return html

    @classmethod
    def get_job_listing_json(cls, html):
        bs = BeautifulSoup(html, "lxml")
        script_tag = bs.find("script", {"type": "application/ld+json"})

        job_listing_json = json.loads(script_tag.contents[0])
        return job_listing_json

    @classmethod
    def get_job_listing_cleaned(cls, html):
        soup = BeautifulSoup(html, "lxml")
        #print(desc_bs)

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()    # rip it out

        #text = soup.get_text()

        lines = [line for line in soup.find_all(text=True) if not line.isspace()]
        #print(text2)

        # break into lines and remove leading and trailing space on each
        #lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        #chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        #for c in chunks:
        #    print(c)
        # drop blank lines
        joined = ' '.join(chunk for chunk in lines if chunk)

        #joined = ' '.join(just_text)
        tokens = word_tokenize(joined)

        stop_list = stopwords.words('english')
        with_no_stops = [word for word in tokens if word.lower() not in stop_list]
        two_grammed = tech_2grams(with_no_stops)
        cleaned = remove_punctuation(two_grammed)

        return ' '.join(cleaned)

    @classmethod
    def generate_sections_of_url(cls, url):
        path = urlparse(url).path
        sections = []; temp = "";
        while path != '/':
            temp = os.path.split(path)
            path = temp[0]
            sections.insert(0, temp[1])
        return sections

    @classmethod
    def get_job_id_from_url(cls, url):
        parsed = urlparse(url)
        parts = cls.generate_sections_of_url(parsed.path)
        return parts[1]

    @classmethod
    def job_listing_from_url(cls, url):
        id = StackOverflowStrategies.get_job_id_from_url(url)
        html = StackOverflowStrategies.get_job_listing_html(url)
        json = StackOverflowStrategies.get_job_listing_json(html)
        clean = StackOverflowStrategies.get_job_listing_cleaned(json['description'])

        return StackOverflowJobListing(url, id, html, clean, json)

if __name__ == "__main__":
    url = "https://stackoverflow.com/jobs/122517/spacex-enterprise-software-engineer-full-stack-spacex"
    listing = StackOverflowStrategies.job_listing_from_url(url)

    print(listing.clean)

    #print(listing.clean)
    #print(listing.json)

    db = StackOverflowJobListingElasticSearchFacade()
    db.delete_all()
    db.put(listing)
