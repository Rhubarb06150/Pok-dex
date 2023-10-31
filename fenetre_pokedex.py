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
import urllib
import sys
print(sys.executable)
#import requests

listemaj=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
listemin=['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

root=Tk()

fenetrex=int((root.winfo_screenwidth()/2)-350)
fenetrey=int((root.winfo_screenheight()/2)-250)

root.geometry('700x500+'+str(fenetrex)+'+'+str(fenetrey))
root.resizable(False,False)

bg=PhotoImage(file='images/fonds/fondsprites3g.png')
bglabel=Label(image=bg)
bglabel.place(x=-2,y=-2)
bglabel.im=bg

file=open('version.txt')
version=str(file.read())
file.close

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

path = ('images/fonds/chromatiqueoff.png')
chromatiqueimg = ImageTk.PhotoImage(Image.open(path))
chromatiquelb=Label(root,image=chromatiqueimg,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
chromatiquelb.photo=chromatiqueimg
chromatiquelb.place(x=216,y=210)
chromatiquelb.bind("<Button-1>", lambda event:chroma_switch())


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


    #POK2MON PREFERE

listelabelpref=[]

path=PhotoImage(file='images/font3g/violet/0.png')

listelabelpref1=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelpref.append(listelabelpref1)
listelabelpref1.place(x=202,y=48)
listelabelpref1.place_forget()

listelabelpref2=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelpref.append(listelabelpref2)
listelabelpref2.place(x=214,y=48)
listelabelpref2.place_forget()

listelabelpref3=Label(root,image=path,borderwidth=0, highlightthickness=0)
listelabelpref.append(listelabelpref3)
listelabelpref3.place(x=226,y=48)
listelabelpref3.place_forget()

#__________________________________

#IMAGES PARAMETRES

img = Image.open('images/fonds/non.png')
img = ImageTk.PhotoImage(img)

verifier_maj_etat=Label(root,image=img,borderwidth=0, highlightthickness=0)
verifier_maj_etat.im=img
verifier_maj_etat.place(x=304,y=104)
verifier_maj_etat.place_forget()

activer_son_etat=Label(root,image=img,borderwidth=0, highlightthickness=0)
activer_son_etat.im=img
activer_son_etat.place(x=76,y=20)
activer_son_etat.place_forget()

def afficher_verifier_maj():
    
    if verifier_les_maj.get() == 1:
        img = Image.open('images/fonds/oui.png')
        img = ImageTk.PhotoImage(img)
        verifier_maj_etat.config(image=img)
        verifier_maj_etat.im=img
        
        
    else:
        img = Image.open('images/fonds/non.png')
        img = ImageTk.PhotoImage(img)
        verifier_maj_etat.config(image=img)
        verifier_maj_etat.im=img
        
    file1=open('txts/maj.txt','w')
    file1.write(str(verifier_les_maj.get()))
    file1.close
    
def maj_switch():
    
    if verifier_les_maj.get() == 1:
        verifier_les_maj.set(0)
    else:
        verifier_les_maj.set(1)
    afficher_verifier_maj()
        
verifier_les_maj = tk.IntVar()
verifier_maj=tk.Checkbutton(root,variable=verifier_les_maj, onvalue=1, offvalue=0,)

activer_son_var = tk.IntVar()
activer_son=tk.Checkbutton(root,variable=activer_son_var, onvalue=1, offvalue=0,)

nom_du_pokemon = StringVar()
file=open('txts/pkmn_pref.txt')
pokemon_prefere_num=str(file.read())
file.close
pokemon_nom=get_nom(int(pokemon_prefere_num))
nom_du_pokemon.set(pokemon_nom)

path = ('images/sprites3g/icones/'+nom_du_pokemon.get()+'1.png')
imageiconeimg = ImageTk.PhotoImage(Image.open(path))
imageicone=Label(image=imageiconeimg,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
imageicone.photo=imageiconeimg
imageicone.place(x=298,y=138)

def lettre(mot,liste):
    
    for i in range(len(mot)):
        
        if isshiny.get() == 0 and liste == listelabel:
                
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
                
        elif isshiny.get() == 1 and liste == listelabel:
            
            if mot[i] == ' ':
                        
                path = ('images/font3g/espace.png')
                img = ImageTk.PhotoImage(Image.open(path))
                        
                liste[i].configure(image=img)
                liste[i].im=img

                    
            else:
                        
                path = ('images/font3g/shiny/'+mot[i]+'.png')
                img = ImageTk.PhotoImage(Image.open(path))
                        
                liste[i].configure(image=img)
                liste[i].im=img
        else:
            
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
    
    for i in range(3):
            
                
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

def icone_switch():
    
    path = ('images/sprites3g/icones/'+nom_du_pokemon.get()+'1.png')
    imageiconeimg = ImageTk.PhotoImage(Image.open(path))
    imageicone.config(image=imageiconeimg,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    imageicone.photo=imageiconeimg

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
    root.title('Pokédex ('+str(version)+') '+nom_du_pokemon.get()+' : '+str(get_num(nom_du_pokemon.get())))
    afficher_pokemon()
    afficher_types()
    icone_switch()

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

def num_pokemon_prefere():
    
    file=open('txts/pkmn_pref.txt')
    num_pref=str(file.read())
    file.close
    
    for i in range(len(num_pref)):
        
        path = ('images/font3g/violet/'+str(num_pref[i])+'.png')
        img = ImageTk.PhotoImage(Image.open(path))
        
        listelabelpref[i].config(image=img)
        listelabelpref[i].photo=img
        

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
    chromatique()
    
    lettre('           ',listelabel)
    lettre(nom_du_pokemon.get(),listelabel)
    
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
        chromatique()
        lettre('           ',listelabel)
        lettre(nom_du_pokemon.get(),listelabel)
    
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
        
def chroma_switch():
        
    if isshiny.get()==0:
        isshiny.set(1)
    else:
        isshiny.set(0)
        
    combobox_nom('r')
    chromatique()
        
def chromatique():
        
    if isshiny.get() == 0:
            
        path = ('images/fonds/chromatiqueoff.png')
        chromatiqueimg = ImageTk.PhotoImage(Image.open(path))
        chromatiquelb.config(image=chromatiqueimg)
        chromatiquelb.photo=chromatiqueimg
            
    else:
            
        path = ('images/fonds/chromatiqueon.png')
        chromatiqueimg = ImageTk.PhotoImage(Image.open(path))
        chromatiquelb.config(image=chromatiqueimg)
        chromatiquelb.photo=chromatiqueimg
            

#BOUTTONS _________________________________________________________________________________________________

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

retouraupokedeximg = Image.open('images/fonds/retouraupokedex.png')
retouraupokedeximg = ImageTk.PhotoImage(retouraupokedeximg)
retouraupokedex=Label(root, image=retouraupokedeximg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
retouraupokedex.config(image=retouraupokedeximg)
retouraupokedex.im=retouraupokedeximg
retouraupokedex.place(x=484,y=0)
retouraupokedex.bind('<Button-1>',lambda event:pokedex())
retouraupokedex.place_forget()

parametresimg = Image.open('images/fonds/parametres.png')
parametresimg = ImageTk.PhotoImage(parametresimg)
parametres=Label(root, image=parametresimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
parametres.config(image=parametresimg)
parametres.im=parametresimg
parametres.place(x=576,y=0)
parametres.bind('<Button-1>',lambda event:parametres_f())

pokemonaleatoireimg = Image.open('images/fonds/aleatoire.png')
pokemonaleatoireimg = ImageTk.PhotoImage(pokemonaleatoireimg)
pokemonaleatoire=Label(root, image=pokemonaleatoireimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
pokemonaleatoire.config(image=pokemonaleatoireimg)
pokemonaleatoire.im=pokemonaleatoireimg
pokemonaleatoire.place(x=190,y=406)
pokemonaleatoire.bind('<Button-1>',lambda event:pokemon_aleatoire())

pokemonprefimg = Image.open('images/fonds/definirpref.png')
pokemonprefimg = ImageTk.PhotoImage(pokemonprefimg)
pokemonpref=Label(root, image=pokemonprefimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
pokemonpref.config(image=pokemonprefimg)
pokemonpref.im=pokemonprefimg
pokemonpref.place(x=18,y=76)
pokemonpref.bind('<Button-1>',lambda event:pokemon_prefere())
pokemonpref.place_forget()

verifiermajimg = Image.open('images/fonds/verifiermaj.png')
verifiermajimg = ImageTk.PhotoImage(verifiermajimg)
verifiermaj=Label(root, image=verifiermajimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
verifiermaj.config(image=verifiermajimg)
verifiermaj.im=verifiermajimg
verifiermaj.place(x=18,y=104)
verifiermaj.bind('<Button-1>',lambda event:maj_switch())
verifiermaj.place_forget()

avancéimg = Image.open('images/fonds/avancé.png')
avancéimg = ImageTk.PhotoImage(avancéimg)
avancé=Label(root, image=avancéimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
avancé.config(image=avancéimg)
avancé.im=avancéimg
avancé.place(x=404,y=0)
avancé.bind('<Button-1>',lambda event:avance_f())

chercherimg = Image.open('images/fonds/chercher.png')
chercherimg = ImageTk.PhotoImage(chercherimg)
chercher=Label(root, image=chercherimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
chercher.config(image=chercherimg)
chercher.im=chercherimg
chercher.place(x=238,y=406)
chercher.bind('<Button-1>',lambda event:chercher_pokemon())

img = Image.open('images/sprites3g/icones/empty.png')
img = ImageTk.PhotoImage(img)
label_pre_evolution=Label(root, image=img, bg='#f8b0a0',borderwidth=0, highlightthickness=0)
label_pre_evolution.im=img
label_pre_evolution.place(x=6,y=270)
label_pre_evolution.place_forget()

#________________________________________________________________________

def pokemon_prefere():
    
    pokemon_pref = tkinter.messagebox.askquestion(title='Définir le Pokémon préféré',message=('Voulez vous définir '+str(nom_du_pokemon.get())+' en tant que Pokémon préféré?'))
    
    if pokemon_pref == 'yes':
        
        numpkmn=int(get_num(nom_du_pokemon.get()))
        
        res=''
        if numpkmn < 10:
            res=('00'+str((get_num(nom_du_pokemon.get()))))
        elif numpkmn < 100:
            res=('0'+str((get_num(nom_du_pokemon.get()))))
        else:
           res=str(numpkmn)
        
        file=open('txts/pkmn_pref.txt', 'w')
        file.write(str(res))
        file.close
        num_pokemon_prefere()
        pokemon_pref = tkinter.messagebox.showinfo(title='Pokémon préféré défini!',message=(str(nom_du_pokemon.get())+' à été défini en tant que Pokémon préféré'))

def pokemon_aleatoire():

    pokemon_aleatoire_var=random.randint(1,len(listenompokemon))
    nom_du_pokemon.set(listenompokemon[pokemon_aleatoire_var])
    combobox_nom('e')
    root.title('Pokédex ('+str(version)+') '+nom_du_pokemon.get()+' : '+str(get_num(nom_du_pokemon.get())))
    
def cacher_pokedex():

    parametres.place_forget()
    
    pokemon.place_forget()
    pokemonback.place_forget()
    etiquette_equipes.place_forget()
    plusdinfos.place_forget()
    etiquette_type1.place_forget()
    etiquette_type2.place_forget()
    etiquette_creer_equipe.place_forget()
    chromatiquelb.place_forget()
    imageicone.place_forget()
    pokemonaleatoire.place_forget()
    
    for i in listelabel:
        i.place_forget()
    for i in listelabelpv:
        i.place_forget()
    for i in listelabelatt:
        i.place_forget()
    for i in listelabeldef:
        i.place_forget()
    for i in listelabelspec:
        i.place_forget()
    for i in listelabelattspec:
        i.place_forget()
    for i in listelabeldefspec:
        i.place_forget()
    for i in listelabelvit:
        i.place_forget()
    for i in listelabelnum:
        i.place_forget()

def cacher_parametres():

    listelabelpref1.place_forget()
    listelabelpref2.place_forget()
    listelabelpref3.place_forget()
    pokemonpref.place_forget()
    verifiermaj.place_forget()
    verifier_maj_etat.place_forget()
    retouraupokedex.place_forget()

    for i in listelabelversionlb:
        i.place_forget()

def afficher_parametres():

    retouraupokedex.place(x=484,y=0)
    listelabelpref1.place(x=202,y=48)
    listelabelpref2.place(x=214,y=48)
    listelabelpref3.place(x=226,y=48)
    pokemonpref.place(x=18,y=76)
    verifiermaj.place(x=18,y=104)
    verifier_maj_etat.place(x=304,y=104)
    xpos=636
    for i in listelabelversionlb:
        i.place(x=xpos,y=440)
        xpos+=12


def parametres_f():
    
    num_pokemon_prefere()
    
    root.title('Paramètres')
    
    img = Image.open('images/fonds/fondparametres.png')
    img = ImageTk.PhotoImage(img)
    
    bglabel.config(image=img)
    bglabel.im=img
    
    cacher_avance()
    cacher_pokedex()
    label_pre_evolution.place_forget()

    afficher_verifier_maj()
        
    afficher_parametres()

    cacher_les_types()

    avancé.place(x=404,y=0)
    retouraupokedex.place(x=484,y=0)
    parametres.place_forget()
    afficher_version()
    
    for i in listelabeliconeavancelb:
        i.place_forget()

    root.bind('<Control-s>',lambda event:None)
    root.bind('<Control-S>',lambda event:None)
    root.bind('<Right>',lambda event:None)
    root.bind('<Left>',lambda event:None)
    root.bind('<Control-Shift-S>',lambda event:None)
    root.bind('<Control-Shift-s>',lambda event:None)
    root.bind('<KeyRelease-S>',lambda event:None)
    root.bind('<KeyRelease-s>',lambda event:None)
    root.bind('<Control-f>',lambda event:None)
    root.bind('<Control-F>',lambda event:None)

def afficher_pokedex():

    avancé.place(x=404,y=0)
    retouraupokedex.place_forget()
    parametres.place(x=576,y=0)

    pokemon.place(x=128,y=74)
    pokemonback.place(x=0,y=74)
    etiquette_type1.place(x=76,y=216)
    etiquette_type2.place(x=142,y=216)
    chromatiquelb.place(x=216,y=210)
    
    xpos=20
    for label in listelabel:
        label.place(x=xpos,y=20)
        xpos+=12

    labelnum1.place(x=16,y=220)
    labelnum2.place(x=28,y=220)
    labelnum3.place(x=40,y=220)

    labelpv1.place(x=38,y=264)
    labelpv2.place(x=50,y=264)
    labelpv3.place(x=62,y=264)

    labelatt1.place(x=98,y=290)
    labelatt2.place(x=110,y=290)
    labelatt3.place(x=122,y=290)

    labeldef1.place(x=98,y=316)
    labeldef2.place(x=110,y=316)
    labeldef3.place(x=122,y=316)

    labelvit1.place(x=98,y=342)
    labelvit2.place(x=110,y=342)
    labelvit3.place(x=122,y=342)

    labelspec1.place(x=98,y=368)
    labelspec2.place(x=110,y=368)
    labelspec3.place(x=122,y=368)

    labelattspec1.place(x=138,y=394)
    labelattspec2.place(x=150,y=394)
    labelattspec3.place(x=162,y=394)

    labeldefspec1.place(x=138,y=420)
    labeldefspec2.place(x=150,y=420)
    labeldefspec3.place(x=162,y=420)

    etiquette_equipes.place(x=548,y=354)
    etiquette_creer_equipe.place(x=536,y=406)
    plusdinfos.place(x=4,y=474)
    
    imageicone.place(x=298,y=138)
    parametres.place(x=576,y=0)
    pokemonaleatoire.place(x=190,y=406)

    chercher.place(x=238,y=406)

def afficher_nom_pokemon():

    xpos=20
    for label in listelabel:
        label.place(x=xpos,y=20)
        xpos+=12

def pokedex():
    
    root.title('Pokédex ('+str(version)+') '+nom_du_pokemon.get()+' : '+str(get_num(nom_du_pokemon.get())))
    
    img = Image.open('images/fonds/fondsprites3g.png')
    img = ImageTk.PhotoImage(img)
    
    bglabel.config(image=img)
    bglabel.im=img

    afficher_pokedex()
    cacher_parametres()
    cacher_avance()
    cacher_les_types()
    label_pre_evolution.place_forget()
    
    retouraupokedex.place_forget()
    
    for i in listelabeliconeavancelb:
        i.place_forget()
    
    root.bind('<Control-s>',lambda event:cri_pokemon())
    root.bind('<Control-S>',lambda event:cri_pokemon())
    root.bind('<Right>',lambda event:pokemon_suivant())
    root.bind('<Left>',lambda event:pokemon_precedent())
    root.bind('<Control-Shift-S>',lambda event:shiny_on_hold())
    root.bind('<Control-Shift-s>',lambda event:shiny_on_hold())
    root.bind('<KeyRelease-S>',lambda event:desactiver_shiny())
    root.bind('<KeyRelease-s>',lambda event:desactiver_shiny())
    root.bind('<Control-f>',lambda event:chercher_pokemon())
    root.bind('<Control-F>',lambda event:chercher_pokemon())

def cacher_avance():

    for label in listelabelconditionlb:
        label.place_forget()
    for i in listelabeliconeavancelb:
        i.place_forget()
    for i in listelabelflechelb:
        i.place_forget()

def afficher_condition_evolution():
    
    for i in listepokemon:
        if i.nom == nom_du_pokemon.get():
            if i.condition_evolution != False:
                if type(i.condition_evolution[numero_icone_choisi]) is int:
                    cond_ev=('Évolue en '+i.evolution[numero_icone_choisi]+' au niveau '+str(i.condition_evolution[numero_icone_choisi]))
                else:
                    cond_ev=i.condition_evolution[numero_icone_choisi]

                place=0
                posx1=2
                xpos=0

                for label2 in listelabelconditionlb:

                    img = Image.open('images/font3g/minuscule/espace.png')
                    img = ImageTk.PhotoImage(img)
                    label2.config(image=img)
                    label2.im=img
    
                for label in listelabelconditionlb:

                    label.place(x=xpos,y=208)
                    xpos+=12

                for i3 in range(len(cond_ev)):

                    lettrecondition(listelabelconditionlb[i3],cond_ev,i3)
                    
def afficher_icones_avance():
    
    for i in listepokemon:
        if i.nom== nom_du_pokemon.get():
            if i.evolution != False:
                evolutions=get_evo(nom_du_pokemon.get())
                
                place=0
                posx1=0
                xpos=0
                
                for label in listelabeliconeavancelb:

                    label.place(x=xpos,y=88)
                    xpos+=64

                for i3 in range(len(evolutions)):

                    afficher_levolution(listelabeliconeavancelb[i3],evolutions[i3])
                

def avance_f():

    avancé.place_forget()
    
    root.title('Infos avancées de '+nom_du_pokemon.get())
    
    img = Image.open('images/fonds/fondavancé.png')
    img = ImageTk.PhotoImage(img)
    
    bglabel.config(image=img)
    bglabel.im=img

    cacher_parametres()
    cacher_pokedex()

    label_pre_evolution.place(x=332,y=102)
    for i in listepokemon:
        if i.nom == nom_du_pokemon.get():
            pre_ev=i.pre_evolution
            if pre_ev != False:
                img = Image.open('images/sprites3g/icones/'+pre_ev+'1.png')
                img = ImageTk.PhotoImage(img)
                label_pre_evolution.config(image=img)
                label_pre_evolution.im=img
            else:
                img = Image.open('images/sprites3g/icones/empty.png')
                img = ImageTk.PhotoImage(img)
                label_pre_evolution.config(image=img)
                label_pre_evolution.im=img

    
    for i in listepokemon:
        if i.nom == nom_du_pokemon.get():
            if i.condition_evolution != False:
                cond_ev=i.condition_evolution
    
    for i in range(5):
        afficher_levolution(listelabeliconeavancelb[i],'empty')
    afficher_icones_avance()
 
    afficher_nom_pokemon()
    lettre('           ',listelabel)
    lettre(nom_du_pokemon.get(),listelabel)

    retouraupokedex.place(x=484,y=0)
    parametres.place(x=576,y=0)

    chercher.place_forget()

    afficher_les_types()

    root.bind('<Control-s>',lambda event:None)
    root.bind('<Control-S>',lambda event:None)
    root.bind('<Right>',lambda event:None)
    root.bind('<Left>',lambda event:None)
    root.bind('<Control-Shift-S>',lambda event:None)
    root.bind('<Control-Shift-s>',lambda event:None)
    root.bind('<KeyRelease-S>',lambda event:None)
    root.bind('<KeyRelease-s>',lambda event:None)
    root.bind('<Control-f>',lambda event:None)
    root.bind('<Control-F>',lambda event:None)

listelabelconditionlb=[]
def listelabelcondition(label,xpos,bg):
    img = Image.open('images/font3g/minuscule/espace.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg=bg,borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=208)
    listelabelconditionlb.append(label)

listelabelflechelb=[]
def listelabelfleche(label,xpos,bg):
    img = Image.open('images/fonds/selectVIDE.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg=bg,borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=152)
    listelabelflechelb.append(label)

listelabelversionlb=[]
def listelabelversion(label,xpos):
    img = Image.open('images/font3g/nombres/espace.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=440)
    listelabelversionlb.append(label)
    
listelabelresistanceslb=[]
def listelabelresistances(label,xpos):
    img = Image.open('images/types/empty.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=310)
    listelabelresistanceslb.append(label)

listelabeldbresistanceslb=[]
def listelabeldbresistances(label,xpos):
    img = Image.open('images/types/empty.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=342)
    listelabeldbresistanceslb.append(label)

listelabelfaiblesseslb=[]
def listelabelfaiblesses(label,xpos):
    img = Image.open('images/types/empty.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=374)
    listelabelfaiblesseslb.append(label)

listelabeldbfaiblesseslb=[]
def listelabeldbfaiblesses(label,xpos):
    img = Image.open('images/types/empty.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=406)
    listelabeldbfaiblesseslb.append(label)

listelabelimmuniteslb=[]
def listelabelimmunites(label,xpos):
    img = Image.open('images/types/empty.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=438)
    listelabelimmuniteslb.append(label)

numero_icone_choisi=-1

place=0
xpos=636
for i in range(5):
    listelabelversion((('label')+str(place)),xpos)
    xpos+=12
    place+=1

for i in listelabelversionlb:
        i.place_forget()

place=0
xpos=42
for i in range(6):
    listelabelresistances((('label')+str(place)),xpos)
    xpos+=66
for i in listelabelresistanceslb:
    i.place_forget()

place=0
xpos=42
for i in range(6):
    listelabeldbresistances((('label')+str(place)),xpos)
    xpos+=66
    place+=1
for i in listelabeldbresistanceslb:
    i.place_forget()

place=0
xpos=42
for i in range(6):
    listelabelfaiblesses((('label')+str(place)),xpos)
    xpos+=66
    place+=1
for i in listelabelfaiblesseslb:
    i.place_forget()

place=0
xpos=42
for i in range(6):
    listelabeldbfaiblesses((('label')+str(place)),xpos)
    xpos+=66
    place+=1
for i in listelabeldbfaiblesseslb:
    i.place_forget()

place=0
xpos=42
for i in range(6):
    listelabelimmunites((('label')+str(place)),xpos)
    xpos+=66
    place+=1
for i in listelabelimmuniteslb:
    i.place_forget()

def afficher_les_types():

    listelabelstypes=[listelabelresistanceslb,listelabeldbresistanceslb,listelabelfaiblesseslb,listelabeldbfaiblesseslb,listelabelimmuniteslb]

    for i in range(6):
        for liste in listelabelstypes:
            img = Image.open('images/types/empty.png')
            img = ImageTk.PhotoImage(img)

            liste[i].config(image=img,bg='#f8b0a0')
            liste[i].im=img
            
    xpos=42
    for i in range(6):
        listelabelresistanceslb[i].place(x=xpos,y=310)
        xpos+=66

    xpos=42
    for i in range(6):
        listelabeldbresistanceslb[i].place(x=xpos,y=342)
        xpos+=66

    xpos=42
    for i in range(6):
        listelabelfaiblesseslb[i].place(x=xpos,y=374)
        xpos+=66

    xpos=42
    for i in range(6):
        listelabeldbfaiblesseslb[i].place(x=xpos,y=406)
        xpos+=66

    xpos=42
    for i in range(6):
        listelabelimmuniteslb[i].place(x=xpos,y=438)
        xpos+=66

    for i in listepokemon:
        if i.nom == nom_du_pokemon.get():
            if i.faiblesses != False:

                faiblesses=i.faiblesses

                for i2 in range(len(faiblesses)):

                    img = Image.open('images/types/'+faiblesses[i2]+'.png')
                    img = ImageTk.PhotoImage(img)

                    listelabelfaiblesseslb[i2].config(image=img,bg='#f8b0a0')
                    listelabelfaiblesseslb[i2].im=img

            if i.dbfaiblesses != False:

                dbfaiblesses=i.dbfaiblesses

                for i2 in range(len(dbfaiblesses)):

                    img = Image.open('images/types/'+dbfaiblesses[i2]+'.png')
                    img = ImageTk.PhotoImage(img)
                    listelabeldbfaiblesseslb[i2].config(image=img,bg='#f8b0a0')
                    listelabeldbfaiblesseslb[i2].im=img

            if i.resistances != False:

                resistances=i.resistances

                for i2 in range(len(resistances)):

                    img = Image.open('images/types/'+resistances[i2]+'.png')
                    img = ImageTk.PhotoImage(img)
                    listelabelresistanceslb[i2].config(image=img,bg='#f8b0a0')
                    listelabelresistanceslb[i2].im=img

            if i.dbresistances != False:

                dbresistances=i.dbresistances

                for i2 in range(len(dbresistances)):

                    img = Image.open('images/types/'+dbresistances[i2]+'.png')
                    img = ImageTk.PhotoImage(img)
                    listelabeldbresistanceslb[i2].config(image=img,bg='#f8b0a0')
                    listelabeldbresistanceslb[i2].im=img

            if i.immunites != False:

                immunites=i.immunites

                for i2 in range(len(immunites)):

                    img = Image.open('images/types/'+immunites[i2]+'.png')
                    img = ImageTk.PhotoImage(img)
                    listelabelimmuniteslb[i2].config(image=img,bg='#f8b0a0')
                    listelabelimmuniteslb[i2].im=img

def cacher_les_types():
    for i in listelabelresistanceslb:
        i.place_forget()
    for i in listelabeldbresistanceslb:
        i.place_forget()
    for i in listelabelfaiblesseslb:
        i.place_forget()
    for i in listelabeldbfaiblesseslb:
        i.place_forget()
    for i in listelabelimmuniteslb:
        i.place_forget()

def afficher_version():

    file=open('version.txt')
    vers=str(file.read())
    file.close

    for i in range(len(vers)):

        if vers[i] == '.':
            img = Image.open('images/font3g/nombres/point.png')
            img = ImageTk.PhotoImage(img)
            listelabelversionlb[i].config(image=img)
            listelabelversionlb[i].im=img
        else:
            img = Image.open('images/font3g/nombres/'+vers[i]+'.png')
            img = ImageTk.PhotoImage(img)
            listelabelversionlb[i].config(image=img)
            listelabelversionlb[i].im=img
        
def choisir_icone(num):

    for i in listepokemon:
        if i.nom == nom_du_pokemon.get():
            if i.condition_evolution != False:
                cond_ev=i.condition_evolution

    global numero_icone_choisi
    numero_icone_choisi = num

    if (numero_icone_choisi)+1 <= len(cond_ev):

        for i in listelabelflechelb:
            i.place_forget()

        position_x= (numero_icone_choisi*64)+25
        listelabelflechelb[numero_icone_choisi].place(x=position_x,y=152)
        img = Image.open('images/fonds/select.png')
        img = ImageTk.PhotoImage(img)
        listelabelflechelb[numero_icone_choisi].config(image=img,bg='#f8b0a0')
        listelabelflechelb[numero_icone_choisi].im=img
        afficher_condition_evolution()

listelabeliconeavancelb=[]
def listelabeliconeavance(label,xpos,bg):
    global numero_icone_choisi
    img = Image.open('images/sprites3g/icones/empty.png')
    img = ImageTk.PhotoImage(img)
    label=Label(root,image=img,bg=bg,borderwidth=0, highlightthickness=0)
    label.im=img
    label.place(x=xpos,y=88)
    listelabeliconeavancelb.append(label)
    label.bind("<Button-1>", lambda event:choisir_icone(int(xpos/64)))
    
#condition evolution    

xpos=0
place=0
for i in range(37):
    bg='#f8b0a0'
    listelabelcondition(('label'+str(place)),xpos,bg)
    xpos+=12
    place+=1
    
for i in listelabelconditionlb:
    i.place_forget()
    
xpos=0
place=0
for i in range(5):
    bg='#f8b0a0'
    listelabelfleche(('label'+str(place)),xpos,bg)
    xpos+=64
    place+=1

for i in listelabelflechelb:
    i.place_forget()

xpos=0
place=0
for i in range(5):
    bg='#f8b0a0'
    listelabeliconeavance(('label'+str(place)),xpos,bg)
    xpos+=64
    place+=1
    
for i in listelabeliconeavancelb:
    i.place_forget()
    
#fin
    
def lettrecondition(label,mot,i):

    if mot[i] == ' ':

        img = Image.open('images/font3g/minuscule/espace.png')
        img = ImageTk.PhotoImage(img)
        
        label.config(image=img)
        label.im=img
        
    elif mot[i] in listemaj:

        img = Image.open('images/font3g/minuscule/maj/'+mot[i]+'.png')
        img = ImageTk.PhotoImage(img)
        
        label.config(image=img)
        label.im=img

    else:

        img = Image.open('images/font3g/minuscule/'+mot[i]+'.png')
        img = ImageTk.PhotoImage(img)
        
        label.config(image=img)
        label.im=img
        
def afficher_levolution(label,pokemon):

    img = Image.open('images/sprites3g/icones/'+pokemon+'1.png')
    img = ImageTk.PhotoImage(img)
        
    label.config(image=img)
    label.im=img

def chercher_pokemon():
    choix_equipe_plus('choix_plus_equipes','chercher',combobox_nom,nom_du_pokemon)
        
root.bind('<Control-s>',lambda event:cri_pokemon())
root.bind('<Control-S>',lambda event:cri_pokemon())
root.bind('<Control-o>',lambda event:choix_equipe_plus('choix_plus_equipes','voir',None,None))
root.bind('<Control-O>',lambda event:choix_equipe_plus('choix_plus_equipes','voir',None,None))
root.bind('<Control-f>',lambda event:chercher_pokemon())
root.bind('<Control-F>',lambda event:chercher_pokemon())

nompokemon.bind("<<ComboboxSelected>>", combobox_nom)

url = 'https://raw.githubusercontent.com/Rhubarb06150/Rhubarb06150.github.io/main/version.txt'
#for line in urllib.request.urlopen(url):
#    version_check=(line.decode('utf-8'))

file=open('txts/maj.txt','r')
verifier_les_maj.set(int(file.read()))
file.close

if verifier_les_maj.get() == 1:
    file2=open('version.txt','r')
    if str(file2.read()) != version_check:
        nouvelle_maj = tkinter.messagebox.askquestion(title='Nouvelle mise à jour disponible!',message='Une nouvelle mise à jour du Pokédex est disponible, souhaitez-vous la télécharger?')
        if nouvelle_maj == 'yes':
            webbrowser.open('https://github.com/Rhubarb06150/Pok-dex')
            root.destroy()
    file2.close
        
file.close

place=0
posx1=2

root.mainloop()