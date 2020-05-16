# Simple Youtube DL

The app opens a small window allowing to copy the link to
a video in order to download it as mp3.

## How to use

Run the executable with python.

### Alternative: Unix System

Run the run.sh in a unix system.
The script install the dependencies and then starts the window.

### Alternative: Windows System

(TODO) Run the .ps1 file.
The script install the dependencies and then starts the window.


## Local Development

In the following text the instruction for local development

Core requirements are:

- python3.8
- pip
- virtualenv

Create virtual environment

```
virtualenv .env
```

Activate the virtual environment:

```
source .env/bin/activate.fish
```

Module requirements are listed in *requirements.txt* file.

Install youtube_dl:

```
pip install youtube-dl
```

Install PyQt5:

```
pip install pyqt5
```


