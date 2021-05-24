import speech_recognition as sr
from pathlib import Path
from playsound import playsound
import json

import requests
from bs4 import BeautifulSoup

from cria_audios import cria_audio
from cria_audios import leitura

def monitora_microfone():

    microfone = sr.Recognizer()
    path_audios = str(Path(__file__).parent.absolute()) + "\\audios\\"

    hotword = 'magnólia'
    n = 1

    while True:

        with sr.Microphone() as source:
            playsound(path_audios + "diga alguma coisa.mp3")
            audio = microfone.listen(source)

        try:
            trigger =  microfone.recognize_google(audio, language='pt-BR')
            trigger = trigger.lower()

            # print("Falado: ", trigger)

            if hotword in trigger:
                # Alguma mensagem de aguardar
                # cria_audio(trigger.replace(hotword,''))
                n = executa_comandos(trigger, n)

            else:
                print('trigger nao ativado')

        except sr.UnknownValueError:
            playsound(path_audios + "Nao entendi.mp3")
            pass

        except: #  sr.RequestError as e
            playsound(path_audios + "erro fatal.mp3")
            pass

def executa_comandos(trigger, n):
    ''' Funcao de comandos '''
    if 'notícias' in trigger:
        # Busca ultimas noticias
        n = ultimas_noticias_google(n)

    elif 'clima' in trigger:
        clima()
        pass

    return n

def ultimas_noticias_google(n):
    site = requests.get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')

    for item in noticias.findAll('item')[:5]:
        mensagem = item.title.text
        leitura(mensagem, n)
        n += 1

    return n

def clima():
    '''  '''

    site = requests.get("http://api.openweathermap.org/data/2.5/weather?q={},br&appid=e9b602c780a1995d5f32c271f8639c0d&units=metric&lang=pt".format('barreirinhas'))
    agora =  site.json()
    # print(json.dumps(agora, indent=4))
    temperatura = agora['main']['temp']
    minima = agora['main']['temp_min']
    maxima = agora['main']['temp_max']
    desc = agora['weather'][0]['main']
    print(desc,temperatura,minima,maxima)


if __name__ == "__main__":
    monitora_microfone()
