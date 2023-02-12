from pytube import YouTube
from pydub import AudioSegment
import os
import sys
import urllib.request
import re

def mashup(x, n, y, output_name):
  delete_after_use = True
  print(sys.argv)
  x = x.replace(' ','') + "songs"
  n = int(n)
  y = int(y)

  url = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + str(x))

  video = re.findall(r"watch\?v=(\S{11})", url.read().decode())

  success = 0
  curr = 0
  for i in range(n):
    try:
      yt = YouTube("https://www.youtube.com/watch?v=" + video[i]) 
      print("Downloading File") 
      yt.streams.filter(only_audio=True).first().download(filename='VidtoAudio-'+str(curr)+'.mp3')
      print(f"Download Complete {curr}")
      print("Your mashup will be available soon. Stay tuned...")
      success+=1
      curr+=1
    except:
      print(f"An error occurred while downloading {i} part")
    

  if os.path.isfile("VidtoAudio-0.mp3"):
      final = AudioSegment.from_file("VidtoAudio-0.mp3")[0:y*1000]
  for i in range(1,success):
      aud_file = str(os.getcwd()) + "/VidtoAudio-"+str(i)+".mp3"
      final = final.append(AudioSegment.from_file(aud_file)[0:y*1000],crossfade=1000)
  

  final.export(output_name, format="mp3")
  print("Output File " + str(output_name))
    
        
  if delete_after_use:
      for i in range(success):
          os.remove("VidtoAudio-"+str(i)+".mp3")