from flask import Flask
from flask_restful import Resource, Api
from elasticsearch import Elasticsearch
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
api = Api(app)

CONFIG = {'AMQP_URI': "amqp://guest:guest@rabbitmq"}

class JobListing(Resource):
    def get(self, job_listing_id):
        return "HI!"

api.add_resource(JobListing, '/', '/joblisting/<string:job_listing_id>')

if __name__ == '__main__':
    print("Starting the job listing API ...")
    app.run(host='0.0.0.0', port=8080, debug=True)