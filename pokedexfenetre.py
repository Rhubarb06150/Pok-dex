import tkinter
import tkinter as tk
from tkinter import *
import random
import keyboard
import winsound

#Fonctions bouttons

def choixgeneration():
    fenetrechoixgeneration=Tk()
    root.title('Choix de la génération')
    width = 240
    height = 300
    fenetrechoixgeneration.geometry('300x240+50+50')
    fenetrechoixgeneration.attributes('-alpha', 1)
    fenetrechoixgeneration.resizable(False,False)
    fenetrechoixgeneration.iconbitmap('images/icones/hooh.ico')
    filename = 'sons/clicmenu.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

fond=random.randint(1,5)
cheminfond="images/fonds/fond"+str(fond)+".png"
root=Tk()
root.title('Pokédex')
width = 680
height = 576
root.geometry('640x576+50+50')
root.attributes('-alpha', 1)
root.resizable(False,False)
root.iconbitmap('images/icones/hooh.ico')
bg = PhotoImage(file = cheminfond)
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0)
gen=Button(root, text = "Génération",relief=RIDGE,bd=5,padx=50,command=choixgeneration)
gen.pack()

root.mainloop()