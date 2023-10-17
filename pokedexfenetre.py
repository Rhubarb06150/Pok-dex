import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import keyboard
from pokedex2proto import listepokemon
from pokedex2proto import *

#Fonctions bouttons
def fond1():
    bg = PhotoImage(file = 'images/fonds/fond1.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
def fond2():
    bg = PhotoImage(file = 'images/fonds/fond2.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
def fond3():
    bg = PhotoImage(file = 'images/fonds/fond3.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
def fond4():
    bg = PhotoImage(file = 'images/fonds/fond4.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
def fond5():
    bg = PhotoImage(file = 'images/fonds/fond5.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
    

def changerlefond():
    fondselect=Tk()
    fondselect.title('Choix du fond')
    fondselect.geometry('200x250+50+50')
    fondselect.resizable(False,False)
    fondselect.iconbitmap('images/icones/lokhlass.ico')
    bfond1=Button(fondselect, text='Pokémon Rouge et Bleu',command=fond1)
    bfond2=Button(fondselect, text='Pokémon Or',command=fond2)
    bfond3=Button(fondselect, text='Pokémon Argent',command=fond3)
    bfond4=Button(fondselect, text='Pokémon Cristal',command=fond4)
    bfond5=Button(fondselect, text='Pokémon Collection',command=fond5)
    bfond1.pack()
    bfond2.pack()
    bfond3.pack()
    bfond4.pack()
    bfond5.pack()
    fondselect.mainloop()

def choixgen1():
    gen1.pack_forget()
    gen2.pack_forget()
    root.title('Pokédex (Première Génération)')
    root.iconbitmap('images/icones/dracaufeu.ico')
    messagebox.showinfo(title="Choix de génération", message='Vous avez choisi la première génération, soit les jeux: Pokémon Rouge, Pokémon Bleu et Pokémon Jaune')
    
def choixgen2():
    gen1.pack_forget()
    gen2.pack_forget()
    root.title('Pokédex (Deuxième Génération)')
    root.iconbitmap('images/icones/hooh.ico')
    messagebox.showinfo(title="Choix de génération",message='Vous avez choisi la deuxième génération, soit les jeux: Pokémon Or, Pokémon Argent et Pokémon Cristal')
    
def fermer():
    root.destroy()
fond=random.randint(1,9)
cheminfond="images/fonds/fond"+str(fond)+".png"
root=Tk()
root.title('Pokédex (Première Génération)')
width = 680
height = 576
root.geometry('640x576+50+50')
root.attributes('-alpha', 1)
root.resizable(False,False)
root.iconbitmap('images/icones/dracaufeu.ico')
bg = PhotoImage(file = cheminfond)
label1 = Label( root, image = bg) 
label1.place(x = -2, y = -2)
gen=Button(root, text = "Changer le fond",bd=2,padx=30,command=changerlefond)
gen.place(x=5,y=545)
gen1=Button(root, text='Première génération',command=choixgen1)
gen2=Button(root, text='Deuxième génération',command=choixgen2)
gen2.place(x=360,y=245)
gen1.place(x=160,y=245)
gen.pack
root.mainloop()