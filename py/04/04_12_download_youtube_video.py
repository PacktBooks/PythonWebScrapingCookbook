#pytube

import pytube as pt

#yt = pt.YouTube("http://youtube.com/watch?v=MWFm4j39YCE")
yt = pt.YouTube("https://www.youtube.com/watch?v=WbsC_fGArVc&list=RDWbsC_fGArVc")
print (yt.get_videos())

mp4 = yt.filter("mp4")[-1]
print(mp4)

print (mp4.filename)
print (mp4.video_codec)

mp4.download(".", force_overwrite=True,
             on_progress=lambda br, fs, start: print(str(int(br/fs*1000)/10)+"%", br, fs, start))
