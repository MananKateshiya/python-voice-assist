

================================

import pytube

link="https://youtu.be/lzkKzZmRZk8"

video = pytube.YouTube(link)
resolution = video.streams.all()

for i in resolution: 
    print(i)

video.streams.get_by_itag(137).download()