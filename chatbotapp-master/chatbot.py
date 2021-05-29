import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

cred = credentials.Certificate('serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatbotapp-330bf.firebaseio.com/'
})

english_bot = ChatBot("Chatterbot", storage_adapter= 'chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(english_bot.storage)
trainer.train("chatterbot.corpus.english")

ref = db.reference('sentchat')
data = ref.get() 

temp = list(data.values())
temp2=dict(temp[-1])
temp2m = temp2['message']

name = temp2['user']

request = temp2m
response = english_bot.get_response(request)
responseN = str(response)

userName = 'CHATBOT'
data = ref.push({
              "user": userName,
              "message": responseN
          })
