from urllib.request import urlopen
page = urlopen("http://localhost:8080/unicode.html")
content = page.read()
content[840:1280]

str(content, "utf-8")[837:1270]

import requests
response = requests.get("http://localhost:8080/unicode.html")
response.encoding
response.text[837:1270]