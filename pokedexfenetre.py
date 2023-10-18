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

#Fonctions bouttons
def fond1():
    bg = PhotoImage(file = 'images/fonds/fond1.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
def fond2():
    bg = PhotoImage(file = 'images/fonds/fond2.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
def fond3():
    bg = PhotoImage(file = 'images/fonds/fond3.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
    
def fond4():
    bg = PhotoImage(file = 'images/fonds/fond4.png')
    label1 = Label( root, image = bg) 
    label1.place(x = -2, y = -2)
    label1.config(image=img)
    label1.im=img
    gen.tkraise()
    
    
def fond5():
    bg = PhotoImage(file = 'images/fonds/fond5.png')
    label1 = Label( root, image = bg) 
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
    root.title('Pokédex (Première Génération)')
    root.iconbitmap('images/icones/dracaufeu.ico')
    messagebox.showinfo(title="Choix de génération", message='Vous avez choisi la première génération, soit les jeux: Pokémon Rouge, Pokémon Bleu et Pokémon Jaune')
    changergen.destroy()
    
def choixgen2():
    gen1.pack_forget()
    gen2.pack_forget()
    root.title('Pokédex (Deuxième Génération)')
    root.iconbitmap('images/icones/hooh.ico')
    messagebox.showinfo(title="Choix de génération",message='Vous avez choisi la deuxième génération, soit les jeux: Pokémon Or, Pokémon Argent et Pokémon Cristal')
    changergen.destroy()
    
    
def avoirlenom():
    messagebox.showinfo(title="Pokémon",message=(get_types(numspinbox.get())))
    

def afficher_pokemon():
    if isshiny.get() == 1:
        
        image = Image.open("images/sprites/"+numpokemon.get()+versionpokemon.get()+"Shiny.png")
        image = ImageTk.PhotoImage(image)

        label_image = Label(photopokemon, image=image)
        label_image.pack()
        
    if isshiny.get() == 0:

        image = Image.open("images/sprites/"+numpokemon.get()+versionpokemon.get()+".png")
        image = ImageTk.PhotoImage(image)

        label_image = Label(photopokemon, image=image)
        label_image.pack()
        
    img=image
    label_image.place(x=30,y=32)
        
    label_image.config(image=img)
    label_image.im=img
    
    photopokemon.title('Fiche de '+numspinbox.get())
    photopokemon.iconbitmap('images/icones/'+numspinbox.get()+'.ico')
    nomdupokemon.config(text='Nom: '+numpokemon.get())
    types.config(text=(get_types(numpokemon.get())))
    pv.config(text=('Pv: '+str(get_pv(numpokemon.get()))))
    force.config(text=('Force: '+str(get_force(numpokemon.get()))))
    defense.config(text=('Défense: '+str(get_defense(numpokemon.get()))))
    vitesse.config(text=('Vitesse: '+str(get_vitesse(numpokemon.get()))))

    


    
fond=random.randint(1,6)
cheminfond="images/fonds/fond"+str(fond)+".png"
root=Tk()
root.title('Pokédex (Première Génération)')
width = 680
height = 576

numspinbox=StringVar(root)
numspinbox.set(1)

versionpokemon=StringVar(root)
isshiny = tk.IntVar()


photopokemon=Toplevel()
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


root.geometry('640x576+50+50')
root.attributes('-alpha', 1)
root.resizable(False,False)
root.iconbitmap('images/icones/Dracaufeu.ico')
bg = PhotoImage(file = cheminfond)
label1 = Label( root, image = bg) 
label1.place(x = -2, y = -2)
fond=Button(root, text = "Changer le fond",bd=2,padx=30,command=changerlefond)
fond.place(x=5,y=545)
gen=Button(root, text = "Changer la génération",bd=2,padx=30,command=changergen)
gen.place(x=5,y=515)
#sprites=Button(root, text = "Pokédex",bd=2,padx=30,command=changergen)
#sprites.place(x=5,y=485)

gen1=Button(root, text='Première génération',command=choixgen1)
gen2=Button(root, text='Deuxième génération',command=choixgen2)
getnom=Button(root, text='Nom',command=avoirlenom)





gen.pack
photopokemon.mainloop()
print(listenompokemon)