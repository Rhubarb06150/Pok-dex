import tkinter as tk, threading
from tkinter import *
from fenetrecontroles import *
from listepokemon import *
import webbrowser

url = 'https://github.com/Rhubarb06150/Pok-dex'

def site():
    webbrowser.open_new_tab(url)
    

def fenetre_a_propos():
    
    a_propos = tk.Toplevel()
    a_propos.title('À propos')
    a_propos.iconbitmap('images/icones/icone.ico')
    a_propos.geometry('300x200+20+570')
    a_propos.resizable(False,False)
    bg=PhotoImage(file='images/fonds/fondapropos.png')
    
    fond=Label(a_propos, image=bg)
    fond.place(x=-2,y=-2)
    
    controles=Button(a_propos,text='Contrôles',command=fenetre_controles)
    controles.place(x=15,y=120)
    
    code_source=Button(a_propos,text='Code source',command=site)
    code_source.place(x=80,y=120)
    
    code_source=Button(a_propos,text='Liste des Pokémons',command=ouvrir)
    code_source.place(x=160,y=120)
    
    rhubarb=Label(a_propos,text='Fait par Rhubarb')
    rhubarb.place(x=15,y=167)
    
    a_propos.mainloop()