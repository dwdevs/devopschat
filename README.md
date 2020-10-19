# DevOps Technical ChatBot in Python

> **Vagrant deployment with "--provision" time: 16m 19s**(mainly spacy install and build)

## Dependencies:
```bash
* Python >= 3.6
* pip3 install flask flask-cors simplejson
* pip3 install chatterBot-corpus
* pip3 install Chatterbot
```
## Running the Chatbot Application:

### Run Flask APP manually:
```bash
sudo python3 main-app.py
```

### Run APP with Vagrant:
```bash
cd Deployment
vagrant up
```
#### To start APP remotely after starting Vagrant machine and exiting python app:
```bash
vagrant ssh -c "sudo python3 ~/devopschat/Application/main-app.py"
```

** Checking log files on vagrant machine **
```bash
vagrant ssh -c "sudo tail -F ~/devopschat/Application/chat-X.log"
```
