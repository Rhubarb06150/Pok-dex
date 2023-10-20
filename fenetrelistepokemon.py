import tkinter as tk, threading
from tkinter import *
from fenetrecontroles import *
import webbrowser

def page2():
    listepokemon.destroy()
    fenetre_listepokemon()
    
def fenetre_listepokemon():
    
    listepokemon = tk.Toplevel()
    listepokemon.title('Liste des Pokémon (Page 1)')
    listepokemon.iconbitmap('images/icones/icone.ico')
    listepokemon.geometry('700x400+50+50')
    listepokemon.resizable(False,False)
    
    bg=PhotoImage(file='images/fonds/fondlistepokemon.png')
    fond=Label(listepokemon, image=bg)
    fond.place(x=-2,y=-2)
    
    
    bulbizarre=Label(listepokemon,text='Bulbizarre')
    bulbizarre.place(x=70,y=25)
    herbiizarre=Label(listepokemon,text='Herbizarre')
    herbiizarre.place(x=70,y=75)
    florizarre=Label(listepokemon,text='Florizarre')
    florizarre.place(x=70,y=125)
    
    salameche=Label(listepokemon,text='Salamèche')
    salameche.place(x=70,y=165)
    reptincel=Label(listepokemon,text='Reptincel')
    reptincel.place(x=70,y=205)
    dracaufeu=Label(listepokemon,text='Dracaufeu')
    dracaufeu.place(x=70,y=255)
    
    florizarre=Label(listepokemon,text='Florizarre')
    florizarre.place(x=70,y=125)
    florizarre=Label(listepokemon,text='Florizarre')
    florizarre.place(x=70,y=125)
    florizarre=Label(listepokemon,text='Florizarre')
    florizarre.place(x=70,y=125)
    
    
    
    page2=Button(listepokemon,text='Page 2')
    page2.place(x=642,y=360)
    listepokemon.mainloop()

fenetre_listepokemon()