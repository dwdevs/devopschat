#import files
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Training with Personal Ques & Ans 
#training_data_simple = open('training_data/normal.txt').read().splitlines()
#training_data_personal = open('training_data/all.txt').read().splitlines()

#training_data = training_data_simple + training_data_personal

#trainer = ListTrainer(chatbot)
#trainer.train(training_data)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
