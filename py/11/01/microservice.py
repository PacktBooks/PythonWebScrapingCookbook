from nameko.rpc import rpc
from nameko.runners import ServiceRunner
import signal
import eventlet
import time
import os

class ScrapeStackOverflowJobListingsMicroService:
    name = "stack_overflow_job_listings_scraping_microservice"

    @rpc
    def get_job_listing_info(self, job_listing_id):
        print("Got request for listing: " + job_listing_id)
        return "HI! " + job_listing_id

if __name__ == "__main__":
    eventlet.monkey_patch()

    amqp_uri = "pyamqp://guest:guest@rabbitmq"
    if os.environ.get("BROKER") is not None:
        amqp_uri = os.environ["BROKER"]

    print("Using: " + amqp_uri)

    while True:
        try:
            runner = ServiceRunner(config={"AMQP_URI": amqp_uri})
            runner.add_service(ScrapeStackOverflowJobListingsMicroService)

            runnlet = eventlet.spawn(runner.wait)

            signal.signal(signal.SIGTERM, lambda signum, frame: eventlet.spawn_n(runner.stop))

            print("Starting")
            runner.start()
            print("Started")
            runnlet.wait()
            runner.stop()

            # proper shutdown
            break

        except:
            time.sleep(5)
            pass