from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class JobListing(Resource):
    def get(self, jobListingId):
        print("Request for job listing with id: " + jobListingId)
        return {'YouRequestedJobWithId': jobListingId}

api.add_resource(JobListing, '/', '/joblisting/<string:jobListingId>')

if __name__ == '__main__':
    print("Starting the job listing API")
    app.run(debug=True)