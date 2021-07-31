import pafy

#URL Video for download
url = "https://www.youtube.com/watch?v=zrxGZ-XpKnw"
video = pafy.new(url)

streams = video.streams

for s in streams:
    print(s)

# Video and Audio Quality
best = video.getbest(preftype="mp4")
print(best.resolution, best.extension)
print(best.url)

#Path to save the video
filename = best.download(quiet=False, filepath="/Users/jacquesjacob/Desktop/")

print("Finish")
