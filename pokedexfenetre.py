import tkinter
import tkinter as tk
from tkinter import *
import random
import keyboard

#Fonctions bouttons

def choixgeneration():
    gen.pack_forget()
    root.title('Choix de la génération')
    gen1.pack()
    gen2.pack()

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
    
fond=random.randint(1,5)
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
label1.place(x = 0, y = 0)
gen=Button(root, text = "Génération",relief=RIDGE,bd=5,padx=50,command=choixgeneration)
gen1=Button(root, text='Première génération',command=choixgen1)
gen2=Button(root, text='Deuxième génération',command=choixgen2)
gen.place(x=5,y=540)
root.mainloop()