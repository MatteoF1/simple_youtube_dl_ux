#!/bin/bash

echo 'Installing requirements.'
pip install -r requirements.txt

echo 'Starting!'
python3 simple_youtube_dl_ux.py 
