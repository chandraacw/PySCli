#!/bin/python3
##########################################################################
##    ____        _____ _________  ##                                   ##
##   / __ \__  __/ ___// ____/ (_) ##           All Thanks To           ##
##  / /_/ / / / /\__ \/ /   / / /  ##              PyTube               ##
## / ____/ /_/ /___/ / /___/ / /   ##           FreeCodeCamp            ##
##/_/    \__, //____/\____/_/_/    ##                                   ##
##      /____/                     ##           -  Chandra  -           ##
##########################################################################

# FIXES BY ANGGI ANANDA
from pytubefix import YouTube
from pytubefix.cli import on_progress
from time import sleep
import os
from requests import get
import pathlib
import argparse
import sys
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
  yt = YouTube(url, on_progress_callback=on_progress)
  base = "Video" if type.lower() == "video" else "Audio"
  fex = "mp4" if type.lower() == "video" else "mp3"
  if os.path.exists(os.path.join(save,f"{yt.title}.{fex}")):
    print(f"{base} file is already exist. Terminating Download...")
    exit()
  print(f"\n Detected type [{base}], Downloading\n")
  if type.lower() == "video":
    stream = yt.streams.filter(progressive=True,file_extension=fex).get_highest_resolution()
  elif type.lower() == "audio":
    stream = yt.streams.filter(only_audio=True).first()
  stream.download(output_path=save,filename=f"{yt.title}")
  print(f"\n\n Downloaded {base} [{yt.title}] ({fex})")
  sleep(3)
  if no_thumbnail == False:
    print("\n Detected Thumbnail is True... Downloading\n")
    responses = get(yt.thumbnail_url, stream=True)
    total = int(responses.headers.get('content-length',0))

    with open(os.path.join(save,f"{yt.title}_Thumbnail.jpg"),"wb") as f, tqdm(
        desc="Downloading Thumbnail",
        total=total,
        unit="kB",
        unit_scale=True,
        unit_divisor=1024
    ) as bar:
      for data in responses.iter_content(chunk_size=1024):
        size = f.write(data)
        bar.update(size)
    print(f"\n Downloaded Thumbnail [{yt.title}] (jpg)")

# Multiple fungsi untuk tujuan yang sama

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

# def check_options(opt):
#   if opt.lower() == "video":
#     return "video"
#   elif opt.lower() == "audio":
#     return "audio"
#   else:
#     return None

def main():
  args = parser.parse_args()
  thumb = False
  if args.is_thumb:
    thumb = True
  if args.opath != os.getcwd():
    path = os.path.join(os.getcwd(),args.opath)

  # Minor unoptimized code and causing bug / bad syntax
  # Sedikit kode tidak teroptimisasi dan memicu bug / sintaks buruk
  if args.typen:
    download_vid(args.url,save=path,type=args.typen,no_thumbnail=thumb)

if __name__ == '__main__':
  main()
