import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import random
import keyboard

root=Tk()
root.title('Pokédex - Accueil')
width = 680
height = 480
root.geometry('600x400+50+50')
root.attributes('-alpha', 1)
root.resizable(False,False)
root.iconbitmap('icones/hooh.ico')
file=open("icones/theme.txt")
theme=file.read()
file.close()

def themecheck():
    global theme
    if theme == 'hooh':
        themehooh()
    if theme == 'lugia':
        themelugia()
    if theme == 'dracaufeu':
        themedracaufeu()
    if theme == 'lokhlass':
        themelokhlass()
    print(theme)
        
def themehooh():
    root.iconbitmap('icones/hooh.ico')
    root.configure(bg='white')
    root.attributes('-alpha', 1)
    gen1.iconbitmap('icones/hooh.ico')
    gen1.configure(bg='white')
    gen1.attributes('-alpha', 1)
    gen2.iconbitmap('icones/hooh.ico')
    gen2.configure(bg='white')
    gen2.attributes('-alpha', 1)
    gen.iconbitmap('icones/hooh.ico')
    gen.configure(bg='white')
    gen.attributes('-alpha', 1)
        
def themelugia():
    root.iconbitmap('icones/lugia.ico')
    root.configure(bg='#48423D')
    root.attributes('-alpha', 1)
    gen1.iconbitmap('icones/lugia.ico')
    gen1.configure(bg='#48423D')
    gen1.attributes('-alpha', 1)
    gen2.iconbitmap('icones/lugia.ico')
    gen2.configure(bg='#48423D')
    gen2.attributes('-alpha', 1)
    gen.iconbitmap('icones/lugia.ico')
    gen.configure(bg='#48423D')
    gen.attributes('-alpha', 1)
        
def themepikachu():
    root.iconbitmap('icones/pikachu.ico')
    root.configure(bg='white')
    root.attributes('-alpha', 1)
        
def themesuicune():
    root.iconbitmap('icones/suicune.ico')
    root.configure(bg='white')
    root.attributes('-alpha', 1)
        
def themetortank():
    root.iconbitmap('icones/tortank.ico')
    root.configure(bg='white')
    root.attributes('-alpha', 1)
        
def themedracaufeu():
    root.iconbitmap('icones/dracaufeu.ico')
    root.configure(bg='#FFC879')
    root.attributes('-alpha', 1)
        
def themeflorizzare():
    root.iconbitmap('icones/florizzare.ico')
    root.configure(bg='white')
    root.attributes('-alpha', 1)
    
def themelokhlass():
    root.iconbitmap('icones/lokhlass.ico')
    root.configure(bg='#6782f0')
    root.attributes('-alpha', 0.9)

def gen1():
    
    gen1 = tk.Toplevel()
    gen1.title("Première Génération")
    gen1.iconbitmap('icones/lokhlass.ico')
    gen1.config(width=240, height=240)
    button_close = ttk.Button(
        gen1,
        text="Cool",
        command=gen1.destroy
    )
    button_close.place(x=85, y=200)
    
def gen2():
    
    gen2 = tk.Toplevel()
    gen2.title("Deuxième Génération")
    gen2.iconbitmap('icones/lokhlass.ico')
    gen2.config(width=240, height=240)
    button_close = ttk.Button(
        gen2,
        text="Cool",
        command=gen2.destroy
    )
    button_close.place(x=85, y=200)

def choixgen():
    gen=Tk()
    gen.title('Choix de la génération')
    width = 480
    height = 240
    gen.geometry('480x240+50+50')
    gen.attributes('-alpha', 1)
    gen.resizable(False,False)
    gen.iconbitmap('icones/hooh.ico')
    choixgen1 = ttk.Button(gen, text='Première génération', command=gen1)
    choixgen1.pack()

    choixgen2 = ttk.Button(gen, text='Deuxième génération', command=gen2)
    choixgen2.pack()
    
hooh = ttk.Button(root, text='Thème Ho-Oh', command=themehooh)
hooh.pack()

lugia = ttk.Button(root, text='Thème Lugia', command=themelugia)
lugia.pack()

dracaufeu = ttk.Button(root, text='Thème Dracaufeu', command=themedracaufeu)
dracaufeu.pack()

lokhlass = ttk.Button(root, text='Thème Lokhlass', command=themelokhlass)
lokhlass.pack()

choixgen = ttk.Button(root, text='Choix de la génération', command=choixgen)
choixgen.pack()

root.mainloop()
themecheck()
