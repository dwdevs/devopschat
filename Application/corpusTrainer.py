#import files
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
