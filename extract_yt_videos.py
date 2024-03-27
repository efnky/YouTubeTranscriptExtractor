from pytube import YouTube

url='https://www.youtube.com/watch?v=C0rGwyJkDTU&t=11s'
my_video=YouTube(url)

my_video = my_video.streams.get_highest_resolution()
my_video.download()