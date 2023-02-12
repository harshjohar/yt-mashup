from pytube import YouTube
from pydub import AudioSegment
import os
import sys
import urllib.request
import re

def mashup():
  delete_after_use = True
  print(sys.argv)
  if len(sys.argv)!=5:
    print("ERROR: Inputs are not same as the required usage")
    print("Usage/Input should be in the format: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
    print("Example usage: python 102003725.py 'Arijit Singh' 20 30 102003725-output.mp3")
    return

  x = sys.argv[1]
  x = x.replace(' ','') + "songs"
  n = int(sys.argv[2])
  y = int(sys.argv[3])
  output_name = sys.argv[4]

  url = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + str(x))

  video = re.findall(r"watch\?v=(\S{11})", url.read().decode())

  for i in range(n):
    yt = YouTube("https://www.youtube.com/watch?v=" + video[i]) 
    print("Downloading File") 
    audio = yt.streams.filter(only_audio=True).first().download(filename='VidtoAudio-'+str(i)+'.mp3')
    print("Download Complete")
    print("Your mashup will be available soon. Stay tuned...")
    

  if os.path.isfile("VidtoAudio-0.mp3"):
      final = AudioSegment.from_file("VidtoAudio-0.mp3")[0:y*1000]
  for i in range(1,n):
      aud_file = str(os.getcwd()) + "/VidtoAudio-"+str(i)+".mp3"
      final = final.append(AudioSegment.from_file(aud_file)[0:y*1000],crossfade=1000)
  

  final.export(output_name, format="mp3")
  print("Output File " + str(output_name))
    
        
  if delete_after_use:
      for i in range(n):
          os.remove("VidtoAudio-"+str(i)+".mp3")

if __name__ == '__main__':
    mashup()