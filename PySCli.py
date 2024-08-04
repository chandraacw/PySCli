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

parser = argparse.ArgumentParser(prog="PyTube Simple CLI",description="Simple and Neat PyTube CLI Tools",epilog=f"{now.strftime('%Y/%m/%d, %H:%M:%S')}")
parser.add_argument("url",help="Video URL")
parser.add_argument("-t","--type",help="Type to be Downloaded (video/audio)",default="video",required=False,dest="typen")
parser.add_argument("-o","--output-path",dest="opath",help="Output path for installed video/audio (Default is CWD)",type=pathlib.Path,default=os.getcwd())
parser.add_argument("-N","--no-thumbnail",help="Download Thumbnail Exception",action="store_true",required=False,dest="is_thumb")
parser.add_argument("-v","--version", action="version",version=f"%(prog)s {__version__}")

def download_vid(url,save=False,no_thumbnail=False):
  yt = YouTube(url)
  if os.path.exists(os.path.join(save,yt.title+".mp4")):
    print("Video file is already exist. Terminating Download...")
    exit()
  print("\n Detected type [Video], Downloading\n")
  if save == False:
    save = os.getcwd()
  streams = yt.streams.filter(progressive=True,file_extension="mp4")
  highest = [streams.get_highest_resolution()]
  for i in tqdm(highest):
    highest[0].download(output_path=save)
  print(f"\n Downloaded Video [{yt.title}] (mp4)")
  sleep(3)
  if no_thumbnail == False:
    print("\nDetected Thumbnail is True... Downloading")
    for i in tqdm(range(1)):
      content = get(yt.thumbnail_url).content
      with open(os.path.join(save,f"{yt.title}_Thumbnail.jpg"),"wb") as f:
        f.write(content)
    print(f"\n Downloaded Thumbnail [{yt.title}] (jpg)")

def download_aud(url,save=False,no_thumbnail=False):
  yt = YouTube(url)
  if os.path.exists(os.path.join(save,yt.title+".mp3")):
    print("Audio file is already exist. Terminating Download...")
    exit()
  print("\n Detected type [Audio], Downloading\n")
  if save == False:
    save = os.getcwd()
  streams = [yt.streams.get_audio_only()]
  for i in tqdm(streams):
    streams[0].download(output_path=save)
    old = os.path.join(save,f"{yt.title}.mp4")
    new = os.path.join(save,f"{yt.title}.mp3")
    os.rename(old,new)
  print(f"\n Downloaded Video [{yt.title}] (mp3)")
  sleep(3)
  if no_thumbnail == False:
    print("\nDetected Thumbnail is True... Downloading")
    for i in tqdm(range(1)):
      content = get(yt.thumbnail_url).content
      with open(os.path.join(save,f"{yt.title}_Thumbnail.jpg"),"wb") as f:
        f.write(content)
    print(f"\n Downloaded Thumbnail [{yt.title}] (jpg)")


def check_options(opt):
  if opt.lower() == "video":
    return "video"
  elif opt.lower() == "audio":
    return "audio"
  else:
    return None

def main():
  args = parser.parse_args()
  path = False
  thumb = False
  if args.is_thumb:
    thumb = True
  if args.opath:
    path = os.path.join(os.getcwd(),args.opath)


  if check_options(args.typen) == "video":
    download_vid(args.url,save=path,no_thumbnail=thumb)
  elif check_options(args.typen):
    download_aud(args.url,save=path,no_thumbnail=thumb)
  else:
    print("""usage: PyTube Simple CLI [-h] [-t TYPEN] [-o OPATH] [-N] url
    PyTube Simple CLI: error: the following arguments are invalid: type""")
    exit()  

if __name__ == '__main__':
  main()
