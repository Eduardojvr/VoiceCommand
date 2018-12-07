#imports do bot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# imports do reconhecimento de voz
import speech_recognition as sr
import pyttsx3
#import objc
import time
import os
import sys
import webbrowser

speak = pyttsx3.init()
estado=0


def fala(text):
    speak.say(str(text))
    speak.runAndWait() 

def comandos(cmd):
    if cmd != "bye":
        fala("Abrindo "+cmd)
        if cmd=="desktop":
            os.popen('cd && cd Desktop && open .')
        elif cmd=="firefox":
            os.popen('cd / && cd Applications && open Firefox.app')
        elif cmd=="facebook":
            webbrowser.open_new("https://www.facebook.com")
        elif cmd=="instagram":
            webbrowser.open_new("https://www.instagram.com")
        elif cmd=="youtube":
            webbrowser.open_new("https://www.youtube.com")
        elif cmd=="studio":
            os.popen('cd / && cd Applications && open Visual\ Studio\ Code.app/') 
        else:
            fala("Não existe esse comando na minha lista de permissões!")
    else: 
        return 1


msg = "Olá Eduardo, tudo bem?O que deseja acessar?"

fala(msg)
voz = sr.Recognizer()

with sr.Microphone() as s:
    while True:
        if estado==1:        
            fala("Tchau, até a próxima Eduardo!")
            sys.exit(1)
        try:
            print("Comando: ")
            audio = voz.listen(s) 
            speech = voz.recognize_google(audio)
            print(speech)
            estado = comandos(speech.lower())
        except:
            print("Comando não encontrado!")
