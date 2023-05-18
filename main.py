import pytube
url= input("youtube url giriniz")
videoKlasor=""
pytube.YouTube(url).streams.get_highest_resolution().download(videoKlasor)
