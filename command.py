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
from PIL import Image
import pytesseract as pyt
import cv2

speak = pyttsx3.init()
estado=0


def conversor(arquivo):
    imagem = cv2.imread(arquivo)
    filenameImagem = "{}.png".format(os.getpid())
    cv2.imwrite(filenameImagem, imagem) 
    texto = pyt.image_to_string(Image.open(filenameImagem))
    os.remove(filenameImagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    fala("Iniciando a leitura.")  
    fala(texto)
    fala("Fim da leitura!")


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
        elif cmd=="text":
            fala("Você escolheu a opção de leitura de texto em imagens!")
            fala("Insira aqui o caminho da imagem juntamente com o seu nome e extensão!")
            caminho = input('Digite:')
            caminho = str(caminho)
            conversor(caminho)
        else:
            fala("Não existe esse comando na minha lista!")
    else: 
        return 1

bot = "Olá, meu nome é Helena, fui desenvolvida para te auxiliar em atividades do seu cotidiano. Atualmente possuo recursos limitados, mas continuo em constante aperfeiçoamento. Bom uso!"

#msg = "Olá Eduardo, tudo bem?O que deseja acessar?"

fala(bot)
#fala(msg)
voz = sr.Recognizer()

with sr.Microphone() as s:
    while True:
        if estado==1:        
            fala("Tchau. Até a próxima!")
            sys.exit(1)
        try:
            print("Comando: ")
            audio = voz.listen(s) 
            speech = voz.recognize_google(audio)
            print(speech)
            estado = comandos(speech.lower())
        except:
            print("Comando não encontrado!")
