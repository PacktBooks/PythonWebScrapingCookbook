import requests
import omdb
import json
#req = requests.get("http://www.omdbapi.com/?apikey=b60fac23&i=nm0000102")
#print(req.text)

client = omdb.Client(apikey='b60fac23')
info = client.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)

