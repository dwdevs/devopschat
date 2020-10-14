#!/bin/bash
clear
echo "#### Updating OS and Installing Python3 ####"
sudo apt-get update -y
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
sudo apt-get install -y software-properties-common

# Install ChatterBot & Flask
clear
echo "#### Installing ChatterBot & Flask ####"
pip3 install flask flask-cors simplejson
pip3 install chatterbot_corpus
pip3 install ChatterBot

# Start the program
clear
echo "#### Starting Chatbot ####"
git clone https://github.com/dwdevs/devopschat.git
cd devopschat
python3 ./Application/app.py
