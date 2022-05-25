from pytube import YouTube


link = input("Enter the link of YouTube video you want to download:")
yt = YouTube(link)


print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)

ys = yt.streams.get_highest_resolution()


# IF PROGRAM DONT WORK YOU NEED TO INSTALL PYTUBE
# pip install pytube
