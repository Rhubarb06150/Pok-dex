import tkinter as tk, threading
from tkinter import *

def fenetre_controles():
    
    aide = tk.Toplevel()
    aide.title('Aide et contrôles')
    aide.iconbitmap('images/icones/icone.ico')
    aide.geometry('350x550+1460+20')
    bg=PhotoImage(file='images/fonds/fondaide.png')
    fond=Label(aide, image=bg)
    fond.place(x=-2,y=-2)
    pksuivant=Label(aide,text='-Pokémon suivant: droit')
    pksuivant.place(x=70,y=100)
    pkprecedent=Label(aide,text='-Pokémon précédent: gacuhe')
    pkprecedent.place(x=70,y=115)
    spriteor=Label(aide,text='-Voir le sprite de la version Or: haut')
    spriteor.place(x=70,y=135)
    spriteargent=Label(aide,text='-Voir le sprite de la version Argent: bas')
    spriteargent.place(x=70,y=150)
    
    voirshiny=Label(aide,text='-Voir la version chromatique du Pokémon: Ctrl + Maj + S')
    voirshiny.place(x=20,y=175)
    ecoutercri=Label(aide,text='-Écouter le cri du Pokémon: Ctrl + S')
    ecoutercri.place(x=20,y=190)
    
    aide.mainloop()