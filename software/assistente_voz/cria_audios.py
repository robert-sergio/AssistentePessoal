from gtts import gTTS
from pathlib import Path
from playsound import playsound
import os

# import platform
# from subprocess import call
# platform.system() # 'Linux', 'Windows' or 'Java'

def cria_audio(audio):


    try:
        path_audios = str(Path(__file__).parent.absolute()) + "\\audios\\"
        tts = gTTS(audio, lang='pt-br')

        # If audio ja tiver sido feito não entra nesse trecho do código
        audio = path_audios + audio + '.mp3'
        tts.save(audio)
        
        playsound(audio)
    except:
        print("Deu erro")


def leitura(mensagem, n_item):

    try:
        path_audios = str(Path(__file__).parent.absolute()) + "\\audios\\"
        tts = gTTS(mensagem, lang='pt-br')

        audio = path_audios + 'mensagem{}.mp3'.format(n_item)
        tts.save(audio)
        playsound(audio)

        os.remove(audio)
    
    except:
        print("Deu erro")


# cria_audio('')

