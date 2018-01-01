from elasticsearch import Elasticsearch
import copy

class StackOverflowJobListingElasticSearchFacade(object):
    def __init__(self, es=None):
        self._es = es
        if self._es is None:
            self._es = Elasticsearch()
        pass

    def put(self, job_listing):
        datum = {
            'id': job_listing.id,
            'Listing': job_listing.json,
            'URL': job_listing.url,
            'Clean': job_listing.clean
        }
        print(datum)
        self._es.index(index='so_jobs', doc_type='so_job_listing', id=datum['id'], body=datum)

    def delete_all(self):
        res = self._es.delete_by_query(index="so_jobs", body={"query": {"match_all": {}}})
        print(res)