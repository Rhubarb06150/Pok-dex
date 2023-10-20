<<<<<<< HEAD
import tkinter
import tkinter as tk
from tkinter import *
import pokedex2proto
from pokedex2proto import *
from zones import *


def afficher_zone():
    print('zone')

def recherche_zone():
    
    recherche = tk.Toplevel()
    recherche.title('Recherche par zone')
    recherche.iconbitmap('images/icones/lokhlass.ico')
    recherche.geometry('500x343+50+50')
    bg=PhotoImage(file='images/fonds/fondrecherche.png')
    fond=Label(recherche, image=bg)
    fond.place(x=-2,y=-2)
    
    zonechoisie=StringVar(recherche)
    zone=Spinbox(recherche, from_=1, to=251 , values = listenomzone, textvariable=zonechoisie, command=afficher_zone, state = 'readonly')
    zone.place(x=150,y=30)
    
    recherche.mainloop()
    
=======
import tkinter
import tkinter as tk
from tkinter import *
import pokedex2proto
from pokedex2proto import *
from zones import *


def afficher_zone():
    print('zone')

def recherche_zone():
    
    recherche = tk.Toplevel()
    recherche.title('Recherche par zone')
    recherche.iconbitmap('images/icones/lokhlass.ico')
    recherche.geometry('500x343+50+50')
    bg=PhotoImage(file='images/fonds/fondrecherche.png')
    fond=Label(recherche, image=bg)
    fond.place(x=-2,y=-2)
    
    zonechoisie=StringVar(recherche)
    zone=Spinbox(recherche, from_=1, to=251 , values = listenomzone, textvariable=zonechoisie, command=afficher_zone, state = 'readonly')
    zone.place(x=150,y=30)
    
    recherche.mainloop()
    
>>>>>>> c436a3df2194abbdd5032edb016fada9c13a9888
recherche_zone()