#imports do bot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# imports do reconhecimento de voz
import speech_recognition as sr
import pyttsx3
#import objc
import time
import os


speak = pyttsx3.init()

def fala(text):
    speak.say(str(text))
    speak.runAndWait() 

def comandos(cmd):
    fala("Abrindo "+cmd)
    if cmd=="desktop":
        os.popen('cd && cd Desktop && open .')
    elif cmd=="firefox":
        os.popen('cd / && cd Applications && open Firefox.app')
    elif cmd=="facebook":
        os.popen("cd / && cd Applications && open Firefox.app/ https://www.facebook.com")
    elif cmd=="instagram":
        os.popen("cd / && cd Applications && open Firefox.app/ https://www.instagram.com")

msg = "Eduardo seu lindo! Qual aplicativo devo iniciar?"
fala(msg)
voz = sr.Recognizer()

with sr.Microphone() as s:
    while True:
        try:
            print("Comando: ")
            audio = voz.listen(s) 
            speech = voz.recognize_google(audio)
            print(speech)
            comandos(speech.lower())
        except:
            print("Comando não encontrado!")
