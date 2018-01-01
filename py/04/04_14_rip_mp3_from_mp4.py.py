import moviepy.editor as mp
clip = mp.VideoFileClip("Top 10 First Contact Movies.mp4")
clip.audio.write_audiofile("movie_audio.mp3")
