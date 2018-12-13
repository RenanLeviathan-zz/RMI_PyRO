import Pyro4
from tkinter import *
import pygame

class Cliente:
    def __init__(self, master=None):
        # conectando ao servidor
        msg = ""
        # iniciando interface gráfica
        frame = Frame(master, width=300,height=300)
        frame.pack()
        label = Label(frame, text="Oráculo (não de Delfos)"+msg)
        label.pack()
        self.text = Entry(frame)
        self.text.pack()
        btn = Button(frame, text="Envie sua pergunta", command=self.send_text)
        btn.pack()

    def send_text(self):
        tts_server = Pyro4.Proxy("PYRO:ttsserver@localhost:3000")
        audio = tts_server.speak(self.text.get())
        pygame.init()
        som = pygame.mixer.Sound(audio)
        som.play()


root = Tk()
Cliente(root)
root.mainloop()