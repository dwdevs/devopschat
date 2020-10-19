#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot

# Creating ChatBot Instance
chatbot = ChatBot(
    'CoronaBot',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.jaccard_similarity",
            "response_selection_method": "chatterbot.response_selection.get_first_response",
            'threshold': 0.65,
            'default_response': "I am sorry, but I do not understand you."
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


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
