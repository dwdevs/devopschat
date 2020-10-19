#import files
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)


# This is the flask APP delivered via 0.0.0.0:5000
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
if __name__ == "__main__":
    app.run(host='0.0.0.0')
