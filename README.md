[![Support The Creator](https://img.shields.io/badge/Support_The-Creator-green?style=flat)](https://saweria.co/AryaChandra) [![Made using PyTube](https://img.shields.io/badge/Made_using-PyTube-blue?style=flat)](https://pypi.org/project/pytube)

![PySCli Banner](https://raw.githubusercontent.com/chandraacw/PySCli/main/assets/PySCli.png)


# **PySCli**

PySCli adalah sebuah CLI Tools yang digunakan untuk mendownload video atau audio dari YouTube dengan bantuan [PyTube](https://pypi.org/project/pytube) namun saya menggunakan [PyTubeFix](https://pypi.org/project/pytubefix).

Ini adalah tools yang saya pertama kali buat secara proper.

Jangan sungkan untuk fork repository ini dan mengembangkannya.

## Daftar Isi
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Instalasi

Gunakan [git](https://git-scm.com/download/linux) untuk copy repository.

```bash
apt install git

git clone https://github.com/LezhinPTAD/PySCli

cd PySCli

pip install -r requirements.txt

python PySCli.py -h
```

Untuk Mengsetup Executable, Lakukan.

```bash
> python3 setup_bin.py
WARNING: TERMUX & LINUX ENVIRONTMENT ONLY
Please Choose Number:
1. Copy
2. Symbolic Link
>
```

## Penggunaan

```bash
> python3 PySCli.py -h
usage: PyTube Simple CLI [-h] [-t {video,audio}] [-o OPATH] [-N] [-v] url

Simple and Neat PyTube CLI Tools

positional arguments:
  url                   Video URL

options:
  -h, --help            show this help message and exit
  -t {video,audio}, --type {video,audio}
                        Type to be Downloaded (video/audio)
  -o OPATH, --output-path OPATH
                        Output path for installed video/audio (Default is CWD)
  -N, --no-thumbnail    Download Thumbnail Exception
  -v, --version         show program's version number and exit

2024/11/21, 10:27:37

> python3 PySCli.py -t video -o . https://youtu.be/T3bxbVGWy5k?si=RrZiXJA1ECnM-bKC

 Detected type [Video], Downloading

 ↳ |████████████████████████████████████████████████| 100.0%

 Downloaded Video [Galileo Galilei - Aoi Shiori] (mp4)

 Detected Thumbnail is True... Downloading

Downloading Thumbnail: 100%|██████████████████████| 23.3k/23.3k [00:00<00:00, 6.07MkB/s]

 Downloaded Thumbnail [Galileo Galilei - Aoi Shiori] (jpg)
```

## Kontribusi

Pull request dipersilahkan, jika ingin membantu tools ini dan membantu saya belajar lebih.

## Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
