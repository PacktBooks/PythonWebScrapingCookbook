from util.urls import URLUtility
from core.file_blob_writer import FileBlobWriter

video_id = "MWFm4j39YCE"
thumbnail_url_base = "https://img.youtube.com/vi/"

for i in range(0,4):
    thumbnail_url = thumbnail_url_base + video_id + "/" + str(i) + ".jpg"
    print("Getting thumbnail: " + thumbnail_url)
    data = URLUtility(thumbnail_url).data
    FileBlobWriter().write("thumbnail_" + video_id + "_" + str(i) + ".jpg", data)
    print("Got video thumbnail # " + str(i))

names = ['default', 'hqdefault', 'mqdefault', 'sddefault', 'maxresdefault']
for n in names:
    thumbnail_url = thumbnail_url_base + video_id + "/" + n + ".jpg"
    print("Getting thumbnail: " + thumbnail_url)
    data = URLUtility(thumbnail_url).data
    FileBlobWriter().write("thumbnail_" + video_id + "_" + n + ".jpg", data)
    print("Got video thumbnail # " + n)