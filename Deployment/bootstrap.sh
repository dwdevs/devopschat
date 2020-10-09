#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
sudo apt-get install -y software-properties-common

# Install ChatterBot & Flask
pip3 install flask flask-cors simplejson
pip3 install chatterbot_corpus
pip3 install ChatterBot
#pip3 install -U spacy && python3 -m spacy download en

# Start the program
#mkdir devopsAPP && cd devopsAPP
git clone https://github.com/dwdevs/devopschat.git
cd devopschat
python3 ./Application/app.py
