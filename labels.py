import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from liste_pokemon import listenompokemon
from liste_pokemon import *

#LABELS

#LISTES

listelabel=[]
listelabelnum=[]
listelabelpv=[]
listelabelatt=[]
listelabeldef=[]
listelabelvit=[]
listelabelspec=[]
listelabelattspec=[]
listelabeldefspec=[]


#IMAGES MISES DE BASE

def labels(master):
    
    global listelabel
    global listelabelnum
    global listelabelpv
    global listelabelatt
    global listelabeldef
    global listelabelvit
    global listelabelspec
    global listelabelattspec
    global listelabeldefspec
    
    imgpokemon = PhotoImage(file='images/sprites3g/Bulbizarre.png')
    pokemon=Label(master, image=imgpokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    pokemon.config(image=imgpokemon)
    pokemon.im=imgpokemon
    pokemon.place(x=128,y=74)
        
    imgpokemonback = PhotoImage(file='images/sprites3g/back/Bulbizarre.png')
    pokemonback=Label(master, image=imgpokemonback,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    pokemonback.config(image=imgpokemonback)
    pokemonback.im=imgpokemonback
    pokemonback.place(x=0,y=74)

    etiquetteimg=PhotoImage(file='images/fonds/etiquette3g.png')
    etiquette=Label(master,image=etiquetteimg,borderwidth=0, highlightthickness=0)
    etiquette.place(x=0,y=10)
    etiquette.photo=etiquetteimg

    etiquette_type1img = Image.open('images/types/empty.png')
    etiquette_type1img = ImageTk.PhotoImage(etiquette_type1img)
    etiquette_type1=Label(master, image=etiquette_type1img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    etiquette_type1.im=etiquette_type1img
    etiquette_type1.place(x=76,y=216)
            
    etiquette_type2img = Image.open('images/types/empty.png')
    etiquette_type2img = ImageTk.PhotoImage(etiquette_type2img)
    etiquette_type2=Label(master, image=etiquette_type2img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    etiquette_type2.im=etiquette_type2img
    etiquette_type2.place(x=142,y=216)

    #_________________________________________

    #LETTRES DU NOM

    listelabel=[]
            
    path=PhotoImage(file='images/font3g/espace.png')
            
    label1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label1)
    label1.place(x=20,y=20)
            
    label2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label2)
    label2.place(x=32,y=20)        

    label3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label3)
    label3.place(x=44,y=20)

    label4=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label4)
    label4.place(x=56,y=20)

    label5=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label5)
    label5.place(x=68,y=20)

    label6=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label6)
    label6.place(x=80,y=20)

    label7=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label7)
    label7.place(x=92,y=20)

    label8=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label8)
    label8.place(x=104,y=20)

    label9=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label9)
    label9.place(x=116,y=20)

    label10=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label10)
    label10.place(x=128,y=20)

    label11=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label11)
    label11.place(x=140,y=20)

    #________________________________________________________________
    #LETTRE DU NUMERO

    listelabelnum=[]

    labelnum1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelnum.append(labelnum1)
    labelnum1.place(x=16,y=220)

    labelnum2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelnum.append(labelnum2)
    labelnum2.place(x=28,y=220)

    labelnum3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelnum.append(labelnum3)
    labelnum3.place(x=40,y=220)

    #________________________________________________________________
    #LETTRES STATS

        #PV

    listelabelpv=[]

    path=PhotoImage(file='images/font3g/underscore.png')
            
    labelpv1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelpv.append(labelpv1)
    labelpv1.place(x=38,y=264)

    labelpv2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelpv.append(labelpv2)
    labelpv2.place(x=50,y=264)

    labelpv3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelpv.append(labelpv3)
    labelpv3.place(x=62,y=264)

        #ATTAQUE

    listelabelatt=[]

    labelatt1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelatt.append(labelatt1)
    labelatt1.place(x=98,y=290)

    labelatt2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelatt.append(labelatt2)
    labelatt2.place(x=110,y=290)

    labelatt3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelatt.append(labelatt3)
    labelatt3.place(x=122,y=290)

        #DEFENSE

    listelabeldef=[]

    labeldef1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldef.append(labeldef1)
    labeldef1.place(x=98,y=316)

    labeldef2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldef.append(labeldef2)
    labeldef2.place(x=110,y=316)

    labeldef3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldef.append(labeldef3)
    labeldef3.place(x=122,y=316)

        #VITESSE

    listelabelvit=[]

    labelvit1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelvit.append(labelvit1)
    labelvit1.place(x=98,y=342)

    labelvit2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelvit.append(labelvit2)
    labelvit2.place(x=110,y=342)

    labelvit3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelvit.append(labelvit3)
    labelvit3.place(x=122,y=342)

        #SPECIAL

    listelabelspec=[]

    labelspec1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelspec.append(labelspec1)
    labelspec1.place(x=98,y=368)

    labelspec2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelspec.append(labelspec2)
    labelspec2.place(x=110,y=368)

    labelspec3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelspec.append(labelspec3)
    labelspec3.place(x=122,y=368)

        #ATTAQUE SPECIALE

    listelabelattspec=[]

    labelattspec1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelattspec.append(labelattspec1)
    labelattspec1.place(x=138,y=394)

    labelattspec2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelattspec.append(labelattspec2)
    labelattspec2.place(x=150,y=394)

    labelattspec3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelattspec.append(labelattspec3)
    labelattspec3.place(x=162,y=394)

        #DEFENSE SPECIALE

    listelabeldefspec=[]

    labeldefspec1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldefspec.append(labeldefspec1)
    labeldefspec1.place(x=138,y=420)

    labeldefspec2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldefspec.append(labeldefspec2)
    labeldefspec2.place(x=150,y=420)

    labeldefspec3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldefspec.append(labeldefspec3)
    labeldefspec3.place(x=162,y=420)
