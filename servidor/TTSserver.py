import Pyro4
from gtts import gTTS
import pygame
import Pyro4.utils.flame

@Pyro4.expose
class TTSserver(object):
    def speak(self, text):
        tts = gTTS(text,'pt-br')
        tts.save("teste.mp3")
        print("Rodando...")
        #pygame.mixer.music.load("teste.mp3")
        #pygame.mixer.music.play()
        data = open('teste.mp3', 'rb')
        return data

daemon = Pyro4.Daemon("localhost", 3000)
uri = daemon.register(TTSserver,"ttsserver")
print("Ready. Object uri=",uri)
daemon.requestLoop()