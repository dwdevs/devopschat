#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)
bot = ChatBot("Python-BOT")
trainer = ListTrainer(bot)
trainer.train(['what is your name?', 'My name is DevelopmentOperationPython-BOT, but you can call me debo'])
trainer.train(['who are you?', 'I am a BOT called debo'])
trainer.train(['what is the best football team?', 'Sheffield United, UTB!'])
trainer.train(['who created you?', 'My master is DW'])
trainer.train(['how can I train you?', 'Look here -> https://chatterbot.readthedocs.io/en/stable/tutorial.html'])


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
@app.route("/")
def index():    
    return render_template("index.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()
