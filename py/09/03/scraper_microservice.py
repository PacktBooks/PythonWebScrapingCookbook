from nameko.rpc import rpc
from sojobs.scraping import get_cleaned_job_listing
class ScapeStackOverflowJobListings:
    name = "stack_overflow_job_listings_scraping_microservice"

    @rpc
    def get_cleaned_listing(self, job_listing_id):
        listing = get_cleaned_job_listing(job_listing_id)
        print(listing)
        return listing

if __name__ == "__main__":
    print("HI!")
    print(get_cleaned_job_listing("122517"))