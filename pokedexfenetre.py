import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import keyboard
from pokedex2proto import listepokemon
from pokedex2proto import listenompokemon
from pokedex2proto import *
from fenetrecontroles import *
from fenetreparametres import *
from fenetreapropos import *
from PIL import Image,ImageTk
from functools import partial
import time
import winsound
from threading import Thread
import webbrowser

#vérifications version
ajour=False
version=0.02




urlnv='https://github.com/Rhubarb06150/Pok-dex'
url = 'https://raw.githubusercontent.com/Rhubarb06150/Pok-dex/main/version.txt'
for line in urllib.request.urlopen(url):
    version_check=(line.decode('utf-8'))

if version == float(version_check):
    ajour=True

#Fonctions bouttons
def fond1():
    bg = PhotoImage(file = 'images/fonds/fond1.png')
    label1 = Label( menupokemon, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
def fond2():
    bg = PhotoImage(file = 'images/fonds/fond2.png')
    label1 = Label( menupokemon, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
def fond3():
    bg = PhotoImage(file = 'images/fonds/fond3.png')
    label1 = Label( menupokemon, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
    
def fond4():
    bg = PhotoImage(file = 'images/fonds/fond4.png')
    label1 = Label( menupokemon, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
    
def fond5():
    bg = PhotoImage(file = 'images/fonds/fond5.png')
    label1 = Label( menupokemon, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    

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
    
def changergen():
    changergen=Tk()
    changergen.title('Choix de la génération')
    changergen.geometry('200x60+50+50')
    changergen.resizable(False,False)
    changergen.iconbitmap('images/icones/Mewtwo.ico')
    gen1=Button(changergen, text='Première génération',command=choixgen1)
    gen1.place(x=2,y=2)
    gen2=Button(changergen, text='Deuxième génération',command=choixgen2)
    gen2.place(x=2,y=30)
    
    

def choixgen1():
    gen1.pack_forget()
    gen2.pack_forget()
    menupokemon.title('Pokédex (Première Génération)')
    menupokemon.iconbitmap('images/icones/dracaufeu.ico')
    messagebox.showinfo(title="Choix de génération", message='Vous avez choisi la première génération, soit les jeux: Pokémon Rouge, Pokémon Bleu et Pokémon Jaune')
    changergen.destroy()
    
def choixgen2():
    gen1.pack_forget()
    gen2.pack_forget()
    menupokemon.title('Pokédex (Deuxième Génération)')
    menupokemon.iconbitmap('images/icones/hooh.ico')
    messagebox.showinfo(title="Choix de génération",message='Vous avez choisi la deuxième génération, soit les jeux: Pokémon Or, Pokémon Argent et Pokémon Cristal')
    changergen.destroy()
    
    
def avoirlenom():
    messagebox.showinfo(title="Pokémon",message=(get_types(numspinbox.get())))
    
def pk_suivant():
    
    if get_num(numpokemon.get()) > 0 and get_num(numpokemon.get()) < 251:
        
        numspinbox.set(get_nom(get_num(numpokemon.get())+1))
        afficher_pokemon()
    
    else:
        
        messagebox.showinfo(title="Aucun Pokémon Suivant",message="Vous ne pouvez pas aller plus loin!")
    recherchepokemon.delete(0,100)
        
def pk_precedent():
    
    if get_num(numpokemon.get()) > 1:
        
        numspinbox.set(get_nom(get_num(numpokemon.get())-1))
        afficher_pokemon()
        
    else:
        
        messagebox.showinfo(title="Aucun Pokémon Précédent",message="Vous ne pouvez pas aller plus loin!")
    recherchepokemon.delete(0,100)

def recherchedupokemon():
    pokemontrouve=False
    
    for i in range (len(listepokemon)):
        
        if len(listepokemon[i].rawnom)== 1 :
            
            if listepokemon[i].rawnom == recherchepokemon.get() :
                
                pokemontrouve=True
                numspinbox.set(listepokemon[i].nom)
                afficher_pokemon()
                
        for i2 in range (len(listepokemon[i].rawnom)):
            
            if listepokemon[i].rawnom[i2] == recherchepokemon.get():
                
                pokemontrouve=True
                numspinbox.set(listepokemon[i].nom)
                afficher_pokemon()
                
        if recherchepokemon.get() == listepokemon[i].nom:
            
            pokemontrouve=True
            numspinbox.set(listepokemon[i].nom)
            afficher_pokemon()
            
    if pokemontrouve == False:
        messagebox.showinfo(title="Aucun Pokémon Trouvé!",message="Aucun Pokémon correspondant à ce nom n'a été trouvé")
    recherchepokemon.delete(0,100)
    
def afficher_pokemon():
    if isshiny.get() == 1:
        
        image = Image.open("images/sprites/"+numpokemon.get()+versionpokemon.get()+"Shiny.png")
        image = ImageTk.PhotoImage(image)

        label_image = Label(root, image=image)
        label_image.pack()
        
    if isshiny.get() == 0:

        image = Image.open("images/sprites/"+numpokemon.get()+versionpokemon.get()+".png")
        image = ImageTk.PhotoImage(image)

        label_image = Label(root, image=image)
        label_image.pack()
        
        
    imagepas = Image.open("images/pas/"+numpokemon.get()+".png")
    imagepas = ImageTk.PhotoImage(imagepas)

    label_imagepas = Label(root, image=imagepas)
    label_imagepas.pack()
        
    img=image
    img2=imagepas
    label_image.place(x=30,y=32)
    label_imagepas.place(x=167,y=114)
        
    label_image.config(image=img)
    label_image.im=img
    label_imagepas.config(image=img2)
    label_imagepas.im=img2
    
    root.title('Fiche de '+numspinbox.get())
    root.iconbitmap('images/icones/'+numspinbox.get()+'.ico')
    nomdupokemon.config(text='Nom: '+numpokemon.get())
    types.config(text=(get_types(numpokemon.get())))
    
    pv.config(text=('Pv: '+str(get_pv(numpokemon.get()))))
    force.config(text=('Force: '+str(get_force(numpokemon.get()))))
    defense.config(text=('Défense: '+str(get_defense(numpokemon.get()))))
    vitesse.config(text=('Vitesse: '+str(get_vitesse(numpokemon.get()))))
    special.config(text=('Spécial: '+str(get_specialgen1(numpokemon.get()))))
    attaque_speciale.config(text=('Attaque spéciale: '+str(get_attspec(numpokemon.get()))))
    defense_speciale.config(text=('Défense spéciale: '+str(get_defspec(numpokemon.get()))))
    numero.config(text=('Numéro: '+str(get_num(numpokemon.get()))))
    
    if get_evo(numpokemon.get()) == 'Aucune évolution':
        evo.config(text=(get_evo(numpokemon.get())))
    else:
        evo.config(text=('Évolution: '+get_evo(numpokemon.get())))
    
    
    if get_pre_evo(numpokemon.get()) == 'Aucune pré-évolution':
        pre_evo.config(text=(get_pre_evo(numpokemon.get())))
    else:
        pre_evo.config(text=('Pré évolution: '+get_pre_evo(numpokemon.get())))
    
    
    
    if get_evo(numpokemon.get()) == 'Aucune évolution':
        afficher_evolution["state"] = "disabled"
    else:
        afficher_evolution["state"] = "normal"
        
    if get_pre_evo(numpokemon.get()) == 'Aucune pré-évolution':
        afficher_pre_evolution["state"] = "disabled"
    else:
        afficher_pre_evolution["state"] = "normal"

def thread_cri():
    numero_pkmn=get_num(numspinbox.get())
    if numero_pkmn < 10:
        chemincri=('sons/cris/00'+str(numero_pkmn)+'.wav')
    elif numero_pkmn < 100:
        chemincri=('sons/cris/0'+str(numero_pkmn)+'.wav')
    else:        
        chemincri=('sons/cris/'+str(numero_pkmn)+'.wav')
    winsound.PlaySound(chemincri, winsound.SND_FILENAME)
    
    
def afficher_evolution():
    numspinbox.set(get_evo(numpokemon.get()))
    afficher_pokemon()
    
def afficher_pre_evolution():
    numspinbox.set(get_pre_evo(numpokemon.get()))
    afficher_pokemon()
    
    
def cri_pokemon():

    thread = Thread(target=thread_cri)
    thread.start()

def version_argent():
    versionpokemon.set('Argent')
    afficher_pokemon()
    
def version_or():
    versionpokemon.set('Or')
    afficher_pokemon()
    
shinynb=0
def tempo_shiny():
    
    global shinynb
    shinynb+=1
    if isshiny.get() == 0:
        isshiny.set(1)
    else:
        isshiny.set(0)
    afficher_pokemon()

    afficher_pokemon()
    
def desactiver_shiny():
    global shinynb
    shinynb=0
    
    if isshiny.get() == 1:
        isshiny.set(0)
    else:
        isshiny.set(1)
        
    afficher_pokemon()
    
def shiny_on_hold():
    global shinynb
    if shinynb == 0:
        tempo_shiny()
    
    

root=Tk()

numspinbox=StringVar(root)
numspinbox.set(1)

versionpokemon=StringVar(root)
isshiny = tk.IntVar()

root.title('Sprites')
root.resizable(False,False)
root.geometry('700x500+20+20')
bg2 = PhotoImage(file = 'images/fonds/fondspritestest.png')
label2 = Label( root, image = bg2) 
label2.place(x = -2, y = -2)
root.iconbitmap('images/icones/icone.ico')
numpokemon=Spinbox(root, from_=1, to=251 , values = listenompokemon, textvariable=numspinbox, command=afficher_pokemon, state = 'readonly')
version=Spinbox(root, from_=1, to=4 , values = listeversion, textvariable=versionpokemon, command=afficher_pokemon, state = 'readonly')
shiny=tk.Checkbutton(root, text='Shiny',variable=isshiny, onvalue=1, offvalue=0, command=afficher_pokemon)
nomdupokemon=Label(root,text=('Nom: '+numpokemon.get()))
types=Label(root,text=(get_types(numpokemon.get())))

statistiques=Label(root,text='Statistiques:')


pv=Label(root,text='Pv: '+str(get_pv(numpokemon.get())))
force=Label(root,text='Force: '+str(get_force(numpokemon.get())))
defense=Label(root,text='Défense: '+str(get_defense(numpokemon.get())))
vitesse=Label(root,text='Vitesse: '+str(get_vitesse(numpokemon.get())))
special=Label(root,text=('Spécial: '+str(get_specialgen1(numpokemon.get()))))
attaque_speciale=Label(root,text=('Attaque spéciale: '+str(get_attspec(numpokemon.get()))))
defense_speciale=Label(root,text=('Défense spéciale: '+str(get_defspec(numpokemon.get()))))


numero=Label(root,text='Numéro: '+str(get_num(numpokemon.get())))

evo=Label(root,text=(get_evo(numpokemon.get())))
pre_evo=Label(root,text=(get_pre_evo(numpokemon.get())))
rechercher=Button(root,text='Rechercher le Pokémon',command=recherchedupokemon)
root.bind('<Return>',lambda event:recherchedupokemon())
root.bind('<Left>',lambda event:pk_precedent())
root.bind('<Right>',lambda event:pk_suivant())

root.bind('<Down>',lambda event:version_argent())
root.bind('<Up>',lambda event:version_or())

root.bind('<Control-Shift-S>',lambda event:shiny_on_hold())
root.bind('<KeyRelease-S>',lambda event:desactiver_shiny())

root.bind('<Control-s>',lambda event:cri_pokemon())
root.bind('<Control-S>',lambda event:cri_pokemon())

root.bind('<Control-L>',lambda event:ouvrir())
root.bind('<Control-l>',lambda event:ouvrir())

recherchepokemon = tk.Entry(root)

a_propos=Button(root,text='À propos',command=fenetre_a_propos)
parametres=Button(root,text='Paramètres',command=fenetre_parametres)
cri=Button(root,text='Écouter le cri',command=cri_pokemon)
afficher_evolution=Button(root,text="Afficher l'évolution",command=afficher_evolution)
afficher_pre_evolution=Button(root,text="Afficher la pré-évolution",command=afficher_pre_evolution)


numpokemon.place(x=160,y=20)
version.place(x=160,y=40)
shiny.place(x=300,y=28)
nomdupokemon.place(x=160,y=60)
types.place(x=160,y=80)
statistiques.place(x=30,y=208)


pv.place(x=35,y=230)
force.place(x=35,y=245)
defense.place(x=35,y=260)
vitesse.place(x=35,y=275)
special.place(x=35,y=290)
attaque_speciale.place(x=219,y=207)
defense_speciale.place(x=219,y=225)


numero.place(x=30,y=168)
evo.place(x=30,y=329)
pre_evo.place(x=30,y=372)
rechercher.place(x=552,y=34)
recherchepokemon.place(x=558,y=14)
cri.place(x=215,y=105)

a_propos.place(x=628,y=460)
parametres.place(x=618,y=430)

afficher_evolution.place(x=30,y=348)
afficher_pre_evolution.place(x=30,y=392)

afficher_pokemon()

#sprites=Button(menupokemon, text = "Pokédex",bd=2,padx=30,command=changergen)
#sprites.place(x=5,y=485)

print("Merci d'utiliser mon Pokédex :)")

if ajour == True:
    print()
    print('À jour!')
else:
    print()
    print('Nouvelle version disponible!')
    MsgBox = tk.messagebox.askquestion("Nouvelle version disponible!", "Une nouvelle version est disponible, voulez vous la télécharger?", icon="question")
    
    if MsgBox == "yes":
        root.destroy()
        webbrowser.open_new_tab(urlnv)
print()


root.mainloop()

#À la création d'un Pokémon:

#les 4 sprites
#le nom dans listenompokemon
#lajout dans listepokemon et dans la classe Pokémon
#le sprite du pas
#son cri
#son icône