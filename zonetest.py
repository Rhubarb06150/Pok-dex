import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import keyboard
from pokedex2proto import listepokemon
from pokedex2proto import listenompokemon
from pokedex2proto import *
from PIL import Image,ImageTk
from functools import partial

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
        
def pk_precedent():
    
    if get_num(numpokemon.get()) > 1:
        
        numspinbox.set(get_nom(get_num(numpokemon.get())-1))
        afficher_pokemon()
        
    else:
        
        messagebox.showinfo(title="Aucun Pokémon Précédent",message="Vous ne pouvez pas aller plus loin!")

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
        messagebox.showinfo(title="Aucun Pokémon Trouvé!",message="Aucun pokémon correspondant à ce nom n'a été trouvé")
    
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
    numero.config(text=('Numéro: '+str(get_num(numpokemon.get()))))
    evo.config(text=(get_evo(numpokemon.get())))



root=Tk()

numspinbox=StringVar(root)
numspinbox.set(1)

versionpokemon=StringVar(root)
isshiny = tk.IntVar()

root.title('Sprites')
root.resizable(False,False)
root.geometry('700x500+50+50')
bg2 = PhotoImage(file = 'images/fonds/fondsprites.png')
label2 = Label( root, image = bg2) 
label2.place(x = -2, y = -2)
root.iconbitmap('images/icones/icone.ico')
numpokemon=Spinbox(root, from_=1, to=120 , values = listenompokemon, textvariable=numspinbox, command=afficher_pokemon, state = 'readonly')
version=Spinbox(root, from_=1, to=4 , values = listeversion, textvariable=versionpokemon, command=afficher_pokemon, state = 'readonly')
shiny=tk.Checkbutton(root, text='Shiny',variable=isshiny, onvalue=1, offvalue=0, command=afficher_pokemon)
nomdupokemon=Label(root,text=('Nom: '+numpokemon.get()))
types=Label(root,text=(get_types(numpokemon.get())))

statistiques=Label(root,text='Statistiques:')
pv=Label(root,text='Pv: '+str(get_pv(numpokemon.get())))
force=Label(root,text='Force: '+str(get_force(numpokemon.get())))
defense=Label(root,text='Défense: '+str(get_defense(numpokemon.get())))
vitesse=Label(root,text='Vitesse: '+str(get_vitesse(numpokemon.get())))
numero=Label(root,text='Numéro: '+str(get_num(numpokemon.get())))

evo=Label(root,text=(get_evo(numpokemon.get())))
rechercher=Button(root,text='Rechercher le Pokémon',command=recherchedupokemon)
root.bind('<Return>',lambda event:recherchedupokemon())
root.bind('<Left>',lambda event:pk_precedent())
root.bind('<Right>',lambda event:pk_suivant())
recherchepokemon = tk.Entry(root)

suivant=Button(root,text='Pokémon Suivant',command=pk_suivant)
precedent=Button(root,text='Pokémon Précédent',command=pk_precedent)


numpokemon.place(x=160,y=20)
version.place(x=160,y=40)
shiny.place(x=300,y=30)
nomdupokemon.place(x=160,y=60)
types.place(x=160,y=80)
statistiques.place(x=30,y=208)
pv.place(x=35,y=231)
force.place(x=35,y=246)
defense.place(x=35,y=261)
vitesse.place(x=35,y=276)
numero.place(x=30,y=168)
precedent.place(x=12,y=460)
suivant.place(x=585,y=460)
evo.place(x=30,y=329)
rechercher.place(x=552,y=34)
recherchepokemon.place(x=558,y=14)


#sprites=Button(menupokemon, text = "Pokédex",bd=2,padx=30,command=changergen)
#sprites.place(x=5,y=485)

root.mainloop()
print(listenompokemon)

#À la création d'un Pokémon:
#les 4 sprites
#le nom dans listenompokemon
#lajout dans listepokemon et dans la classe Pokémon
#le sprite du pas
#son cri
#son icône
