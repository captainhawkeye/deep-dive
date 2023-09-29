import yt_dlp

url = input("Enter Video URL: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video Downloaded Successfully")