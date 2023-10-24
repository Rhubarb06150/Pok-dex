import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from pokedex2proto import listenompokemon
from pokedex2proto import *



icone1=True

def icone_switch(root):
    
    global icone1
    
    if icone1 == True:
        
        root.after(500,icone_2(root))
        
    else:
        
        root.after(500,icone_1(root))

def icone_1(root):
    
    global icone1

    imgiconepokemon = Image.open('images/sprites3g/icones/'+nom_du_pokemon.get()+'2.png')
    imgiconepokemon = ImageTk.PhotoImage(imgiconepokemon)
    icone1 = True
    
    iconepokemon=Label(root, image=imgiconepokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    iconepokemon.config(image=imgiconepokemon)
    iconepokemon.im=imgiconepokemon
    iconepokemon.place(x=298,y=138)
   
    icone_switch(root)
    
def icone_2(root):
    
    global icone1

    imgiconepokemon = Image.open('images/sprites3g/icones/'+nom_du_pokemon.get()+'1.png')
    imgiconepokemon = ImageTk.PhotoImage(imgiconepokemon)
    icone1 = False
    
    iconepokemon=Label(root, image=imgiconepokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    iconepokemon.config(image=imgiconepokemon)
    iconepokemon.im=imgiconepokemon
    iconepokemon.place(x=298,y=138)
    
    icone_switch(root)
    

            
