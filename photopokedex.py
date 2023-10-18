import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import keyboard
from pokedex2proto import listepokemon
from pokedex2proto import listenompokemon
from pokedex2proto import *
from photopokedex import *
from pokedexfenetre import *
from PIL import Image,ImageTk

def ouvrirphotopokemon():
    
    photopokemon=Toplevel(master)
    photopokemon.title('Sprites')
    photopokemon.resizable(False,False)
    photopokemon.geometry('700x500+50+50')
    bg2 = PhotoImage(file = 'images/fonds/fondsprites.png')
    label2 = Label( photopokemon, image = bg2) 
    label2.place(x = -2, y = -2)
    photopokemon.iconbitmap('images/icones/icone.ico')
    numpokemon=Spinbox(photopokemon, from_=1, to=120 , values = listenompokemon, textvariable=numspinbox, command=afficher_pokemon)
    version=Spinbox(photopokemon, from_=1, to=4 , values = listeversion, textvariable=versionpokemon, command=afficher_pokemon)
    shiny=tk.Checkbutton(photopokemon, text='Shiny',variable=isshiny, onvalue=1, offvalue=0, command=afficher_pokemon)
    nomdupokemon=Label(photopokemon,text=('Nom: '+numpokemon.get()))
    types=Label(photopokemon,text=(get_types(numpokemon.get())))
    statistiques=Label(photopokemon,text='Statistiques:')
    pv=Label(photopokemon,text='Pv: '+str(get_pv(numpokemon.get())))
    force=Label(photopokemon,text='Force: '+str(get_force(numpokemon.get())))
    defense=Label(photopokemon,text='Défense: '+str(get_defense(numpokemon.get())))
    vitesse=Label(photopokemon,text='Vitesse: '+str(get_vitesse(numpokemon.get())))


    numpokemon.place(x=160,y=20)
    version.place(x=160,y=40)
    shiny.place(x=300,y=30)
    nomdupokemon.place(x=160,y=60)
    types.place(x=160,y=80)
    statistiques.place(x=30,y=160)
    pv.place(x=35,y=180)
    force.place(x=35,y=195)
    defense.place(x=35,y=210)
    vitesse.place(x=35,y=225)
