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

## Penggunaan

```bash
> python PySCli.py -h
usage: PyTube Simple CLI [-h] [-t TYPEN] [-o OPATH] [-N] [-v] url

Simple and Neat PyTube CLI Tools

positional arguments:
  url                   Video URL

options:
  -h, --help            show this help message and exit
  -t TYPEN, --type TYPEN
                        Type to be Downloaded (video/audio)
  -o OPATH, --output-path OPATH
                        Output path for installed video/audio (Default is
                        CWD)
  -N, --no-thumbnail    Download Thumbnail Exception
  -v, --version         show program's version number and exit

2024/08/04, 16:39:4

> python PySCli.py https://youtu.be/xX7xWEh6ujk\?si\=r9sjcuOeQR0d7inY -o Output_Folder

Detected type [Video], Downloading

100%|███████████████████████████████████████████| 1/1 [00:31<00:00, 31.86s/it]

 Downloaded Video [Sparkle - Your Name【 Kimi no Na wa. 】AMV] (mp4)

Detected Thumbnail is True... Downloading
100%|███████████████████████████████████████████| 1/1 [00:00<00:00,  2.65it/s]

 Downloaded Thumbnail [Sparkle - Your Name【 Kimi no Na wa. 】AMV] (jpg)
>
```

## Kontribusi

Pull request dipersilahkan, jika ingin membantu tools ini dan membantu saya belajar lebih.

## Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
