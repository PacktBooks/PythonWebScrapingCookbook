from bs4 import BeautifulSoup
import json
from nltk.corpus import stopwords

with open("spacex-job-listing.html", "r") as file:
    content = file.read()

bs = BeautifulSoup(content, "lxml")
script_tag = bs.find("script", {"type": "application/ld+json"})

job_listing_contents = json.loads(script_tag.contents[0])
print(job_listing_contents)

# print the skills
for skill in job_listing_contents["skills"]:
    print(skill)