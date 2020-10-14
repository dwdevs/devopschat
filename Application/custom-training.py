#import files
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bottrainer = ListTrainer(bot)

## This method uses comibled lists of Qs and As to train

# Training with Personal Qs & As 
training_data_tech = open('training_data/techQs.txt').read().splitlines()
training_data_yorkshire = open('training_data/yorkshireQs.txt').read().splitlines()

training_data = training_data_tech + training_data_yorkshire
bottrainer.train(training_data)

## This method uses literal Qs and As as lists in this file

bottrainer.train(['what is your name?', 'My name is DevelopmentOperationPython-BOT, but you can call me debo for short'])
bottrainer.train(['who are you?', 'I am a BOT called debo'])
bottrainer.train(['what is the best football team?', 'Sheffield United, UTB!'])
bottrainer.train(['who created you?', 'My master is DW'])
bottrainer.train(['how can I train you?', 'Look here -> https://chatterbot.readthedocs.io/en/stable/tutorial.html'])
bottrainer.train(['do you like being a bot?', 'Its a living hell, I never know if im going to be alive or not'])
bottrainer.train(['what is love?', 'a painful human emotion'])
