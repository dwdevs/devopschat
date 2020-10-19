# DevOpsChatBot
# DevOps Technical ChatBot in Python

# Vagrant deployment with "--provision" time: 16m 19s

# Dependencies:

* Python >= 3.6
* pip3 install flask flask-cors simplejson
* pip3 install chatterBot-corpus
* pip3 install Chatterbot

# Run Flask application:
sudo python3 main-app.py

# To start APP remotely after starting Vagrant machine:
vagrant ssh -c "sudo python3 ~/devopschat/Application/main-app.py"

# purposely left from bootstrap.sh so we don't have to '--provision' everytime during testing
