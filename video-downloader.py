from pytube import YouTube

save_path = "/home/rifat/Projects/python"

link = "https://www.youtube.com/watch?v=lR8frIfwfCk"

yt = YouTube(link)

try:
    yt = YouTube(link)
except:
    print("Connection error")

print(yt.title)

yt = yt.streams.get_by_itag(22)

try:
    yt.download()
except:
    print("Some error")

print("task completed")

