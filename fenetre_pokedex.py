import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from liste_pokemon import listenompokemon
from liste_pokemon import *
from threading import Thread
import winsound
from fenetre_equipes import *

root=Tk()
root.geometry('700x500+50+50')
root.resizable(False,False)
bg=PhotoImage(file='images/fonds/fondsprites3g.png')
bglabel=Label(image=bg)
bglabel.place(x=-2,y=-2)

place=0
posx=-5

nom_du_pokemon=StringVar()

def afficher_icone():
    imgicone=PhotoImage(file='images/sprites3g/icones/'+nom_du_pokemon.get()+'1.png')
    label=Label(root,image=imgicone,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    label.place(x=298,y=138)
    label.photo=imgicone
        
def combobox_nom(event):
    
    etiquetteimg=PhotoImage(file='images/fonds/etiquette3g.png')
    etiquette=Label(root,image=etiquetteimg,borderwidth=0, highlightthickness=0)
    etiquette.place(x=0,y=10)
    etiquette.photo=etiquetteimg
    
    global posx
    posx=5
    place=0
    
    def lettre(label,img,i):
        
        global posx
        posx+=12
        if i == ' ':
            path = ('images/font3g/espace.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(root,image=img,borderwidth=0, highlightthickness=0)
            label.pack()
            label.place(x=posx,y=20)
            label.photo=img
        else:
            path = ('images/font3g/'+i+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(root,image=img,borderwidth=0, highlightthickness=0)
            label.pack()
            label.place(x=posx,y=20)
            label.photo=img 
        
    
    for i in nom_du_pokemon.get():
        
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i)
    
    
    root.title(nom_du_pokemon.get())
    
    combobox_num()
    afficher_pokemon()
    #afficher_icone()
    stats_num()
    
def combobox_num():
    
    etiquettenumimg=PhotoImage(file='images/fonds/etiquettenum3g.png')
    etiquettenum=Label(root,image=etiquettenumimg,borderwidth=0, highlightthickness=0)
    etiquettenum.place(x=0,y=210)
    etiquettenum.photo=etiquettenumimg
    
    global posx
    posx=-5
    place=0
    
    def lettre(label,img,i):
        
        global posx
        posx+=12
        path = ('images/font3g/'+i+'.png')
        img = ImageTk.PhotoImage(Image.open(path))
        label=Label(root,image=img,borderwidth=0, highlightthickness=0)
        label.place(x=posx,y=220)
        label.photo=img
        
    
    numpkmn=int(get_num(nom_du_pokemon.get()))
    if numpkmn < 10:
        numpkmn=str('00'+str((get_num(nom_du_pokemon.get()))))
    elif numpkmn < 100:
        numpkmn=str('0'+str((get_num(nom_du_pokemon.get()))))
    else:
        numpkmn=str(numpkmn)
    for i in ('#'+numpkmn):
        
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i)


def stats_num():
    
    etiquettenumimg=PhotoImage(file='images/fonds/etiquettestats.png')
    etiquettenum=Label(root,image=etiquettenumimg,borderwidth=0, highlightthickness=0)
    etiquettenum.place(x=0,y=258)
    etiquettenum.photo=etiquettenumimg
    
    global posx
    posx=28
    place=0
    
    def lettre(label,img,i,y):
        
        global posx
        posx+=12
        path = ('images/font3g/'+i+'.png')
        img = ImageTk.PhotoImage(Image.open(path))
        label=Label(root,image=img,borderwidth=0, highlightthickness=0)
        label.place(x=posx,y=y)
        label.photo=img
        
    pv = str(get_pv(str(nom_du_pokemon.get())))
        
    for i in pv:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,264)
        
    posx=88
        
    force = str(get_force(str(nom_du_pokemon.get())))
        
    for i in force:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,290)
        
    posx=88
        
    defense = str(get_defense(str(nom_du_pokemon.get())))
        
    for i in defense:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,314)
        
    posx=88
        
    vitesse = str(get_vitesse(str(nom_du_pokemon.get())))
        
    for i in vitesse:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,340)
        
    posx=88
        
    special = str(get_specialgen1(str(nom_du_pokemon.get())))
        
    for i in special:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,366)
        
    posx=128
        
    attspecial = str(get_attspec(str(nom_du_pokemon.get())))
        
    for i in attspecial:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,394)
        
    posx=128
        
    defspecial = str(get_defspec(str(nom_du_pokemon.get())))
        
    for i in defspecial:
        place+=1
        lettre(('label'+str(place)),('img'+str(place)),i,420)

#----------------------------------------------------------------

def afficher_pokemon():
    
    if isshiny.get() == 1:
        
        imgpokemon = Image.open('images/sprites3g/shiny/'+nom_du_pokemon.get()+'.png')
        imgpokemon = ImageTk.PhotoImage(imgpokemon)
        imgpokemonback = Image.open('images/sprites3g/shiny/back/'+nom_du_pokemon.get()+'.png')
        imgpokemonback = ImageTk.PhotoImage(imgpokemonback)

        
    else:
        
        imgpokemon = Image.open('images/sprites3g/'+nom_du_pokemon.get()+'.png')
        imgpokemon = ImageTk.PhotoImage(imgpokemon)
        imgpokemonback = Image.open('images/sprites3g/back/'+nom_du_pokemon.get()+'.png')
        imgpokemonback = ImageTk.PhotoImage(imgpokemonback)
        
    pokemon=Label(root, image=imgpokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    pokemon.config(image=imgpokemon)
    pokemon.im=imgpokemon
    pokemon.place(x=128,y=74)
    
    pokemonback=Label(root, image=imgpokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    pokemonback.config(image=imgpokemonback)
    pokemonback.im=imgpokemonback
    pokemonback.place(x=0,y=74)
    
    pokemonback.bind("<Button-1>", lambda event:cri_pokemon())
    pokemon.bind("<Button-1>", lambda event:cri_pokemon())

def pokemon_suivant():
    
    if get_num(nom_du_pokemon.get()) < 251:
        for i in range(len(listenompokemon)):
            if listenompokemon[i] == nom_du_pokemon.get():
                nom_du_pokemon.set(listenompokemon[i+1])
                combobox_nom('root')
                break
        
def pokemon_precedent():
    
    if get_num(nom_du_pokemon.get()) != 1:
        for i in range(len(listenompokemon)):
            if listenompokemon[i] == nom_du_pokemon.get():
                nom_du_pokemon.set(listenompokemon[i+-1])
                combobox_nom('root')
                break

#SHORTCUT SHINY
    
shinytempo=False
shinynb=0
def tempo_shiny():
    
    global shinytempo
    global shinynb
    shinynb+=1
    shinytempo=True
    if isshiny.get() == 0:
        isshiny.set(1)
    else:
        isshiny.set(0)
    afficher_pokemon()
    
    afficher_pokemon()
    
def desactiver_shiny():
    global shinytempo
    global shinynb
    if shinytempo == True:
        shinynb=0
        
        if isshiny.get() == 1:
            isshiny.set(0)
        else:
            isshiny.set(1)
        shinytempo=False
        afficher_pokemon()
    
def shiny_on_hold():
    global shinynb
    if shinynb == 0:
        tempo_shiny()
    
nom_du_pokemon.set('Bulbizarre')
    
isshiny = tk.IntVar()
shiny=tk.Checkbutton(root, text='Shiny',variable=isshiny, onvalue=1, offvalue=0, command=afficher_pokemon)


animok = tk.IntVar()
anim=tk.Checkbutton(root, text='Animation',variable=animok, onvalue=1, offvalue=0, command=combobox_nom('e'))


root.bind('<Control-Shift-S>',lambda event:shiny_on_hold())
root.bind('<Control-Shift-s>',lambda event:shiny_on_hold())
root.bind('<KeyRelease-S>',lambda event:desactiver_shiny())
root.bind('<KeyRelease-s>',lambda event:desactiver_shiny())

#------------------------
    
combobox_nom('root')
nompokemon=ttk.Combobox(values=listenompokemon,textvariable=nom_du_pokemon,state='readlonly')
root.iconbitmap('images/sprites3g/icones/pokeball.ico')

root.bind('<Right>',lambda event:pokemon_suivant())
root.bind('<Left>',lambda event:pokemon_precedent())

def thread_cri():
    numero_pkmn=get_num(nom_du_pokemon.get())
    if numero_pkmn < 10:
        chemincri=('sons/cris/00'+str(numero_pkmn)+'.wav')
    elif numero_pkmn < 100:
        chemincri=('sons/cris/0'+str(numero_pkmn)+'.wav')
    else:        
        chemincri=('sons/cris/'+str(numero_pkmn)+'.wav')
    winsound.PlaySound(chemincri, winsound.SND_ASYNC)
    
def cri_pokemon():

    thread = Thread(target=thread_cri)
    thread.start()
    

etiquette_equipesimg = Image.open('images/fonds/etiquetteequipes.png')
etiquette_equipesimg = ImageTk.PhotoImage(etiquette_equipesimg)
etiquette_equipes=Label(root, image=etiquette_equipesimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
etiquette_equipes.config(image=etiquette_equipesimg)
etiquette_equipes.im=etiquette_equipesimg
etiquette_equipes.place(x=548,y=354)
etiquette_equipes.bind('<Button-1>',lambda event:choix_equipe('choix_equipe'))

etiquette_creer_equipesimg = Image.open('images/fonds/etiquettecreerequipe.png')
etiquette_creer_equipesimg = ImageTk.PhotoImage(etiquette_creer_equipesimg)
etiquette_creer_equipe=Label(root, image=etiquette_creer_equipesimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
etiquette_creer_equipe.config(image=etiquette_creer_equipesimg)
etiquette_creer_equipe.im=etiquette_creer_equipesimg
etiquette_creer_equipe.place(x=548,y=406)
etiquette_creer_equipe.bind('<Button-1>',lambda event:choix_creation_equipe('master'))
    
    
root.bind('<Control-s>',lambda event:cri_pokemon())
root.bind('<Control-S>',lambda event:cri_pokemon())



nompokemon.bind("<<ComboboxSelected>>", combobox_nom)

root.mainloop()
print(len(listenompokemon))