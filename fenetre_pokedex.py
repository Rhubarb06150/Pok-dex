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
import webbrowser

root=Tk()
root.geometry('700x500+50+50')
root.resizable(False,False)
bg=PhotoImage(file='images/fonds/fondsprites3g.png')
bglabel=Label(image=bg)
bglabel.place(x=-2,y=-2)

#IMAGES MISES DE BASE

imgpokemon = PhotoImage(file='images/sprites3g/Bulbizarre.png')
pokemon=Label(root, image=imgpokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
pokemon.config(image=imgpokemon)
pokemon.im=imgpokemon
pokemon.place(x=128,y=74)
    
imgpokemonback = PhotoImage(file='images/sprites3g/back/Bulbizarre.png')
pokemonback=Label(root, image=imgpokemonback,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
pokemonback.config(image=imgpokemonback)
pokemonback.im=imgpokemonback
pokemonback.place(x=0,y=74)

etiquette_type1img = Image.open('images/types/empty.png')
etiquette_type1img = ImageTk.PhotoImage(etiquette_type1img)
etiquette_type1=Label(root, image=etiquette_type1img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
etiquette_type1.im=etiquette_type1img
etiquette_type1.place(x=76,y=216)
        
etiquette_type2img = Image.open('images/types/empty.png')
etiquette_type2img = ImageTk.PhotoImage(etiquette_type2img)
etiquette_type2=Label(root, image=etiquette_type2img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
etiquette_type2.im=etiquette_type2img
etiquette_type2.place(x=142,y=216)

#_________________________________________

#LETTRES DU NOM

listelabel=[]
        
path=PhotoImage(file='images/font3g/espace.png')
        
label1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label1)
label1.place(x=20,y=20)
        
label2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label2)
label2.place(x=32,y=20)        

label3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label3)
label3.place(x=44,y=20)

label4=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label4)
label4.place(x=56,y=20)

label5=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label5)
label5.place(x=68,y=20)

label6=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label6)
label6.place(x=80,y=20)

label7=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label7)
label7.place(x=92,y=20)

label8=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label8)
label8.place(x=104,y=20)

label9=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label9)
label9.place(x=116,y=20)

label10=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label10)
label10.place(x=128,y=20)

label11=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabel.append(label11)
label11.place(x=140,y=20)

#________________________________________________________________
#LETTRE DU NUMERO

listelabelnum=[]

labelnum1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelnum.append(labelnum1)
labelnum1.place(x=16,y=220)

labelnum2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelnum.append(labelnum2)
labelnum2.place(x=28,y=220)

labelnum3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelnum.append(labelnum3)
labelnum3.place(x=40,y=220)

#________________________________________________________________
#LETTRES STATS

    #PV

listelabelpv=[]

path=PhotoImage(file='images/font3g/underscore.png')
        
labelpv1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelpv.append(labelpv1)
labelpv1.place(x=38,y=264)

labelpv2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelpv.append(labelpv2)
labelpv2.place(x=50,y=264)

labelpv3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelpv.append(labelpv3)
labelpv3.place(x=62,y=264)

    #ATTAQUE

listelabelatt=[]

labelatt1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelatt.append(labelatt1)
labelatt1.place(x=98,y=290)

labelatt2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelatt.append(labelatt2)
labelatt2.place(x=110,y=290)

labelatt3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelatt.append(labelatt3)
labelatt3.place(x=122,y=290)

    #DEFENSE

listelabeldef=[]

labeldef1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabeldef.append(labeldef1)
labeldef1.place(x=98,y=316)

labeldef2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabeldef.append(labeldef2)
labeldef2.place(x=110,y=316)

labeldef3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabeldef.append(labeldef3)
labeldef3.place(x=122,y=316)

    #VITESSE

listelabelvit=[]

labelvit1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelvit.append(labelvit1)
labelvit1.place(x=98,y=342)

labelvit2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelvit.append(labelvit2)
labelvit2.place(x=110,y=342)

labelvit3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelvit.append(labelvit3)
labelvit3.place(x=122,y=342)

    #SPECIAL

listelabelspec=[]

labelspec1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelspec.append(labelspec1)
labelspec1.place(x=98,y=368)

labelspec2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelspec.append(labelspec2)
labelspec2.place(x=110,y=368)

labelspec3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelspec.append(labelspec3)
labelspec3.place(x=122,y=368)

    #ATTAQUE SPECIALE

listelabelattspec=[]

labelattspec1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelattspec.append(labelattspec1)
labelattspec1.place(x=138,y=394)

labelattspec2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelattspec.append(labelattspec2)
labelattspec2.place(x=150,y=394)

labelattspec3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelattspec.append(labelattspec3)
labelattspec3.place(x=162,y=394)

    #DEFENSE SPECIALE

listelabeldefspec=[]

labeldefspec1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabeldefspec.append(labeldefspec1)
labeldefspec1.place(x=138,y=420)

labeldefspec2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabeldefspec.append(labeldefspec2)
labeldefspec2.place(x=150,y=420)

labeldefspec3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabeldefspec.append(labeldefspec3)
labeldefspec3.place(x=162,y=420)


#__________________________________

nom_du_pokemon=StringVar()

def lettre(mot,liste):
    
    for i in range(len(mot)):
            
                
        if mot[i] == ' ':
                    
            path = ('images/font3g/espace.png')
            img = ImageTk.PhotoImage(Image.open(path))
                    
            liste[i].configure(image=img)
            liste[i].im=img

                
        else:
                    
            path = ('images/font3g/'+mot[i]+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
                    
            liste[i].configure(image=img)
            liste[i].im=img
            
def lettre_num():
    
    numpkmn=int(get_num(nom_du_pokemon.get()))
    if numpkmn < 10:
        numpkmn=str('00'+str((get_num(nom_du_pokemon.get()))))
    elif numpkmn < 100:
        numpkmn=str('0'+str((get_num(nom_du_pokemon.get()))))
    else:
       numpkmn=str(numpkmn)
    
    for i in range(len(numpkmn)):
            
                
        if numpkmn[i] == ' ':
                    
            path = ('images/font3g/espace.png')
            img = ImageTk.PhotoImage(Image.open(path))
                    
            listelabelnum[i].configure(image=img)
            listelabelnum[i].im=img

                
        else:
                    
            path = ('images/font3g/'+numpkmn[i]+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
                    
            listelabelnum[i].configure(image=img)
            listelabelnum[i].im=img


def combobox_nom(event):
    
#_________________________________ACTION_____________________________________________
    
                 
    lettre('           ',listelabel)
    lettre('   ',listelabelpv)
    lettre('   ',listelabelatt)
    lettre('   ',listelabeldef)
    lettre('   ',listelabelvit)
    lettre('   ',listelabelspec)
    lettre('   ',listelabelattspec)
    lettre('   ',listelabeldefspec)
    
    pv=str(get_pv(nom_du_pokemon.get()))
    att=str(get_force(nom_du_pokemon.get()))
    defense=str(get_defense(nom_du_pokemon.get()))
    vit=str(get_vitesse(nom_du_pokemon.get()))
    spec=str(get_specialgen1(nom_du_pokemon.get()))
    attspec=str(get_attspec(nom_du_pokemon.get()))
    defspec=str(get_defspec(nom_du_pokemon.get()))
    
    lettre(nom_du_pokemon.get(),listelabel)
    lettre(pv,listelabelpv)
    lettre(att,listelabelatt)
    lettre(defense,listelabeldef)
    lettre(vit,listelabelvit)
    lettre(spec,listelabelspec)
    lettre(attspec,listelabelattspec)
    lettre(defspec,listelabeldefspec)
    
    lettre_num()
    root.title(nom_du_pokemon.get())
    afficher_pokemon()
    afficher_types()

#_________________________________ACTION_____________________________________________


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
        
    pokemon.config(image=imgpokemon)
    pokemon.im=imgpokemon
    pokemon.place(x=128,y=74)
    
    pokemonback.config(image=imgpokemonback)
    pokemonback.im=imgpokemonback
    pokemonback.place(x=0,y=74)
    
    pokemonback.bind("<Button-1>", lambda event:cri_pokemon())
    pokemon.bind("<Button-1>", lambda event:cri_pokemon())

def pokemon_suivant():
    
    if get_num(nom_du_pokemon.get()) < 384:
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
#____________________________________________


def afficher_types():
    
    etiquette_type1img = Image.open('images/types/empty.png')
    etiquette_type1img = ImageTk.PhotoImage(etiquette_type1img)
    etiquette_type1.config(image=etiquette_type1img)
    etiquette_type1.im=etiquette_type1img
    
    etiquette_type2img = Image.open('images/types/empty.png')
    etiquette_type2img = ImageTk.PhotoImage(etiquette_type2img)
    etiquette_type2.config(image=etiquette_type2img)
    etiquette_type2.im=etiquette_type2img
    
    
    if get_type1(nom_du_pokemon.get()) != False:
        
        etiquette_type1img = Image.open('images/types/'+str(get_type1(nom_du_pokemon.get()))+'.png')
        etiquette_type1img = ImageTk.PhotoImage(etiquette_type1img)
        etiquette_type1.config(image=etiquette_type1img)
        etiquette_type1.im=etiquette_type1img
        
    if get_type2(nom_du_pokemon.get()) != False:
        
        etiquette_type2img = Image.open('images/types/'+str(get_type2(nom_du_pokemon.get()))+'.png')
        etiquette_type2img = ImageTk.PhotoImage(etiquette_type2img)
        etiquette_type2.config(image=etiquette_type2img)
        etiquette_type2.im=etiquette_type2img
    
    
nom_du_pokemon.set('Germignon')
    
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
    
def ouvrir_pokepedia():
    
    ouvrir = tkinter.messagebox.askquestion(title='Aller sur Poképédia',message=('Voulez vous ouvrir la page Poképédia de '+str(nom_du_pokemon.get())+'?'))
    
    if ouvrir == 'yes':
        
        webbrowser.open('https://www.pokepedia.fr/'+(nom_du_pokemon.get()))

#BOUTTONS EQUIPES _____________________________________________

etiquette_equipesimg = Image.open('images/fonds/etiquetteequipes.png')
etiquette_equipesimg = ImageTk.PhotoImage(etiquette_equipesimg)
etiquette_equipes=Label(root, image=etiquette_equipesimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
etiquette_equipes.config(image=etiquette_equipesimg)
etiquette_equipes.im=etiquette_equipesimg
etiquette_equipes.place(x=548,y=354)
etiquette_equipes.bind('<Button-1>',lambda event:choix_equipe('choix_equipe_fenetre'))

etiquette_creer_equipesimg = Image.open('images/fonds/etiquettecreerequipe.png')
etiquette_creer_equipesimg = ImageTk.PhotoImage(etiquette_creer_equipesimg)
etiquette_creer_equipe=Label(root, image=etiquette_creer_equipesimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
etiquette_creer_equipe.config(image=etiquette_creer_equipesimg)
etiquette_creer_equipe.im=etiquette_creer_equipesimg
etiquette_creer_equipe.place(x=536,y=406)
etiquette_creer_equipe.bind('<Button-1>',lambda event:choix_creation_equipe('master'))

plusdinfosimg = Image.open('images/fonds/plusdinfos.png')
plusdinfosimg = ImageTk.PhotoImage(plusdinfosimg)
plusdinfos=Label(root, image=plusdinfosimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
plusdinfos.config(image=plusdinfosimg)
plusdinfos.im=plusdinfosimg
plusdinfos.place(x=4,y=474)
plusdinfos.bind('<Button-1>',lambda event:ouvrir_pokepedia())

#________________________________________________________________________
    


root.bind('<Control-s>',lambda event:cri_pokemon())
root.bind('<Control-S>',lambda event:cri_pokemon())



nompokemon.bind("<<ComboboxSelected>>", combobox_nom)

print(str((int(len(listenompokemon))/251)*100)+'% des Pokémons implémantés')

root.mainloop()

