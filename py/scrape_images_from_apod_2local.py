from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
import shutil
from os.path import expanduser
import mimetypes
import sys

sys.path.insert(0, "../common")

def get_file_extension(response):
	content_type = response.headers['content-type']
	if content_type == "image/jpeg":
		return ".jpg"
	if content_type == "image/gif":
		return ".gif"
	return None
	
def save_local(base_filename):
	full_filename = expanduser("~") + "/" + base_filename
	print(full_filename)
	with open(full_filename, 'wb') as outfile:
		shutil.copyfileobj(response, outfile)

year=2017
month=9


for day in range(1, 4):
	url = "https://apod.nasa.gov/apod/ap{0}{1:02d}{2:02d}.html".format(year % 2000, month, day)

	print (url)
	sys.stdout.flush()

	try:
		html = urlopen(url)
		bsobj = BeautifulSoup(html, "lxml")

		img_p = bsobj.html.body.center.findAll("p")[1]
		a = img_p.find("a")

		if a != None:
			href = a["href"]
			imgurl = "https://apod.nasa.gov/apod/" + href
			print (imgurl)
			img_data = urllib.request.urlopen(imgurl).read()
		
			#urllib.request.urlretrieve(imgurl, "~/1.jpg")

			with urllib.request.urlopen(imgurl) as response:
				extension = get_file_extension(response)
				if extension != None:
					filename = "{0}{1}".format(day, extension)

					save_local(filename)

			#print(img_data)
	except:
		break
