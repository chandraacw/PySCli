#!/bin/python3
##########################################################################
##    ____        _____ _________  ##                                   ##
##   / __ \__  __/ ___// ____/ (_) ##           All Thanks To           ##
##  / /_/ / / / /\__ \/ /   / / /  ##              PyTube               ##
## / ____/ /_/ /___/ / /___/ / /   ##           FreeCodeCamp            ##
##/_/    \__, //____/\____/_/_/    ##                                   ##
##      /____/                     ##           -  Chandra  -           ##
##########################################################################
from pytubefix import YouTube
from time import sleep
import os
from requests import get
import pathlib
import argparse
from tqdm import tqdm
from datetime import datetime as dt

now = dt.now()

### Silly Version Variable :3 ###
__get_version__ = [now.strftime("%Y"),now.strftime("%m"),now.strftime("%d")+" 1.0.0"]
__version__ = '/'.join(__get_version__)

#Fix some argument error and bad code
parser = argparse.ArgumentParser(prog="PyTube Simple CLI",description="Simple and Neat PyTube CLI Tools",epilog=f"{now.strftime('%Y/%m/%d, %H:%M:%S')}")
parser.add_argument("url",help="Video URL")
parser.add_argument("-t","--type",help="Type to be Downloaded (video/audio)",choices=["video","audio"],required=False,default="video",dest="typen")
parser.add_argument("-o","--output-path",dest="opath",help="Output path for installed video/audio (Default is CWD)",type=pathlib.Path,default=os.getcwd())
parser.add_argument("-N","--no-thumbnail",help="Download Thumbnail Exception",action="store_true",required=False,dest="is_thumb")
parser.add_argument("-v","--version", action="version",version=f"%(prog)s {__version__}")

def download_vid(url,save,type,no_thumbnail=False):
  yt = YouTube(url)
  if type.lower() == "video":
    base = "Video"
    fex = "mp4"
  elif type.lower() == "audio":
    base = "Audio"
    fex = "mp3"
  if os.path.exists(os.path.join(save,f"{yt.title}.{fex}")):
    print(f"{base} file is already exist. Terminating Download...")
    exit()
  print(f"\n Detected type [{base}], Downloading\n")
  if type.lower() == "video":
    streams = [yt.streams.filter(progressive=True,file_extension=fex).get_highest_resolution()]
  elif type.lower() == "audio":
    streams = [yt.streams.get_audio_only()]
  for i in tqdm(streams):
    streams[0].download(output_path=save,filename=f"{yt.title}.{fex}")
  print(f"\n Downloaded {base} [{yt.title}] ({fex})")
  sleep(3)
  if no_thumbnail == False:
    print("\nDetected Thumbnail is True... Downloading")
    for i in tqdm(range(1)):
      content = get(yt.thumbnail_url).content
      with open(os.path.join(save,f"{yt.title}_Thumbnail.jpg"),"wb") as f:
        f.write(content)
    print(f"\n Downloaded Thumbnail [{yt.title}] (jpg)")

#Multiple fungsi untuk tujuan yang sama

# def download_aud(url,save=False,no_thumbnail=False):
#   yt = YouTube(url)
#   if os.path.exists(os.path.join(save,f"{yt.title}.mp3")):
#     print("Audio file is already exist. Terminating Download...")
#     exit()
#   print("\n Detected type [Audio], Downloading\n")
#   streams = [yt.streams.get_audio_only()]
#   for i in tqdm(streams):
#     streams[0].download(output_path=save,filename=f"{yt.title}.mp3")
#   print(f"\n Downloaded Video [{yt.title}] (mp3)")
#   sleep(3)
#   if no_thumbnail == False:
#     print("\nDetected Thumbnail is True... Downloading")
#     for i in tqdm(range(1)):
#       content = get(yt.thumbnail_url).content
#       with open(os.path.join(save,f"{yt.title}_Thumbnail.jpg"),"wb") as f:
#         f.write(content)
#     print(f"\n Downloaded Thumbnail [{yt.title}] (jpg)")


# Penggunaan buruk fungsi

#def check_options(opt):
#  if opt.lower() == "video":
#    return "video"
#  elif opt.lower() == "audio":
#    return "audio"
#  else:
#    return None

def main():
  args = parser.parse_args()
  thumb = False
  if args.is_thumb:
    thumb = True
  if args.opath != os.getcwd():
    path = os.path.join(os.getcwd(),args.opath)

  #Minor unoptimized code and bug / bad syntax
  if args.typen:
    download_vid(args.url,save=path,type=args.typen,no_thumbnail=thumb)

if __name__ == '__main__':
  main()
