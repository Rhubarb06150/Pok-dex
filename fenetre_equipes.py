import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from liste_pokemon import listenompokemon
from liste_pokemon import *
from threading import Thread
import winsound

def fenetre_equipe(master,equipechoisie,nom):
    
    equipe=[]

    for i in range(6):
        file=open('txts/'+str(equipechoisie)+'/membre'+str(i+1)+'.txt')
        equipe.append(file.read())
        file.close
    
    master=tk.Toplevel()
    master.geometry('500x450+1000+500')
    master.resizable(False,False)
    background=PhotoImage(file='images/fonds/fondequipes.png')
    bg=Label(master, image=background)
    bg.place(x=-2,y=-2)
    master.title(nom)
    master.iconbitmap('images/sprites3g/icones/hyperball.ico')
    
    
    global posx
    posx=5
    place=0
    
    def lettre(label,img,i,y):
        
        global posx
        posx+=12
        
        if i == ' ':
            
            path = ('images/font3g/espace.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(master,image=img,borderwidth=0, highlightthickness=0)
            label.pack()
            label.place(x=posx,y=y)
            label.photo=img
        else:
            
            path = ('images/font3g/'+i+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(master,image=img,borderwidth=0, highlightthickness=0)
            label.pack()
            label.place(x=posx,y=y)
            label.photo=img
            
    def lettre_shiny(label,img,i,y):
        
        global posx
        posx+=12
        
        if i == ' ':
            
            path = ('images/font3g/shiny/espace.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(master,image=img,borderwidth=0, highlightthickness=0)
            label.pack()
            label.place(x=posx,y=y)
            label.photo=img
        else:
            
            path = ('images/font3g/shiny/'+i+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(master,image=img,borderwidth=0, highlightthickness=0)
            label.pack()
            label.place(x=posx,y=y)
            label.photo=img 
    
    def afficher_equipe():
        
        shiny=False
        
        place=0
        global posx
        
        for membre in equipe:
            

            if membre[0] != '':
                
                y=156
                posx=6
                for i in equipe[0]:
                    
                    if ((equipe[0])[-1]) == '1':
                    
                        shiny=True
                    
                    if i == '1':
                        path = ('images/sprites3g/shiny/'+str(equipe[0]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=16,y=16)
                        pklabel.photo=pokemonimg
                    
                    else:
                    
                        path = ('images/sprites3g/'+str(equipe[0]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=16,y=16)
                        pklabel.photo=pokemonimg
                        
                    if shiny == True and i != '1':
                        place+=1
                        lettre_shiny(('label'+str(place)),('img'+str(place)),i,y)
                    elif shiny == False and i != '1':
                        place+=1
                        lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
                    
            if membre[1] != '':
                
                shiny=False
                
                y=156
                posx=176
                for i in equipe[1]:
                    
                    if ((equipe[1])[-1]) == '1':
                    
                        shiny=True

                    if i == '1':
                        
                        path = ('images/sprites3g/shiny/'+str(equipe[1]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=186,y=16)
                        pklabel.photo=pokemonimg
                    
                    else:
                    
                        path = ('images/sprites3g/'+str(equipe[1]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=186,y=16)
                        pklabel.photo=pokemonimg
                        
                    if shiny == True and i != '1':
                        place+=1
                        lettre_shiny(('label'+str(place)),('img'+str(place)),i,y)
                    elif shiny == False and i != '1':
                        place+=1
                        lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if membre[2] != '':
                
                shiny=False
                
                y=156
                posx=346
                for i in equipe[2]:
                    
                    if ((equipe[2])[-1]) == '1':
                    
                        shiny=True
                    
                    if i == '1':
                        
                        path = ('images/sprites3g/shiny/'+str(equipe[2]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=356,y=16)
                        pklabel.photo=pokemonimg
                    
                    else:
                    
                        path = ('images/sprites3g/'+str(equipe[2]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=356,y=16)
                        pklabel.photo=pokemonimg
                        
                    if shiny == True and i != '1':
                        place+=1
                        lettre_shiny(('label'+str(place)),('img'+str(place)),i,y)
                    elif shiny == False and i != '1':
                        place+=1
                        lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if membre[3] != '':
                
                shiny=False
                
                y=340
                posx=6
                for i in equipe[3]:
                    
                    if ((equipe[3])[-1]) == '1':
                    
                        shiny=True
                    
                    if i == '1':
                        
                        path = ('images/sprites3g/shiny/'+str(equipe[3]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=16,y=200)
                        pklabel.photo=pokemonimg
                    
                    else:
                    
                        path = ('images/sprites3g/'+str(equipe[3]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=16,y=200)
                        pklabel.photo=pokemonimg
                        
                    if shiny == True and i != '1':
                        place+=1
                        lettre_shiny(('label'+str(place)),('img'+str(place)),i,y)
                    elif shiny == False and i != '1':
                        place+=1
                        lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if membre[4] != '':
                
                shiny=False
                
                y=340
                posx=176
                for i in equipe[4]:
                    
                    if ((equipe[4])[-1]) == '1':
                    
                        shiny=True
                    
                    if i == '1':
                        
                        path = ('images/sprites3g/shiny/'+str(equipe[4]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=186,y=200)
                        pklabel.photo=pokemonimg
                    
                    else:
                    
                        path = ('images/sprites3g/'+str(equipe[4]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=186,y=200)
                        pklabel.photo=pokemonimg
                    
                    if shiny == True and i != '1':
                        place+=1
                        lettre_shiny(('label'+str(place)),('img'+str(place)),i,y)
                    elif shiny == False and i != '1':
                        place+=1
                        lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if membre[5] != '':
                
                shiny=False
                
                y=340
                posx=346
                for i in equipe[5]:
                    
                    if ((equipe[5])[-1]) == '1':
                    
                        shiny=True
                    
                    if i == '1':
                        
                        path = ('images/sprites3g/shiny/'+str(equipe[5]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=356,y=200)
                        pklabel.photo=pokemonimg
                    
                    else:
                    
                        path = ('images/sprites3g/'+str(equipe[5]).replace('1','')+'.png')
                        pokemonimg = ImageTk.PhotoImage(Image.open(path))
                        pklabel=Label(master,image=pokemonimg,borderwidth=0, highlightthickness=0, bg='#f8b0a0')
                        pklabel.pack()
                        pklabel.place(x=356,y=200)
                        pklabel.photo=pokemonimg
                        
                    if shiny == True and i != '1':
                        place+=1
                        lettre_shiny(('label'+str(place)),('img'+str(place)),i,y)
                    elif shiny == False and i != '1':
                        place+=1
                        lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            break
    

                
        
            
    afficher_equipe()
    master.mainloop()
    
def choix_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")
    master.geometry('224x232+100+100')
    master.resizable(False,False)
    background=PhotoImage(file='images/fonds/fondchoixequipes.png')
    bg=Label(master, image=background)
    bg.place(x=-2,y=-2)
    master.iconbitmap('images/sprites3g/icones/hyperball.ico')
    
    #Équipe 1
    
    equipe1img = Image.open('images/fonds/equipe1.png')
    equipe1img = ImageTk.PhotoImage(equipe1img)
    equipe1=Label(master, image=equipe1img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe1.config(image=equipe1img)
    equipe1.im=equipe1img
    equipe1.place(x=4,y=4)
    equipe1.bind('<Button-1>',lambda event:fenetre_equipe('equipe1','equipe1','Équipe 1'))
    
    #Équipe 2
    
    equipe2img = Image.open('images/fonds/equipe2.png')
    equipe2img = ImageTk.PhotoImage(equipe2img)
    equipe2=Label(master, image=equipe2img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe2.config(image=equipe2img)
    equipe2.im=equipe2img
    equipe2.place(x=114,y=4)
    equipe2.bind('<Button-1>',lambda event:fenetre_equipe('equipe2','equipe2','Équipe 2'))
    

    master.mainloop()
    
numero_membre_choisi=0
    
def creation_equipe(master,equipechoisie):
    
    global numero_membre_choisi
    numero_membre_choisi=0
    
    master=tk.Toplevel()
    master.title("Création de l'équipe")
    master.geometry('500x400+100+100')
    master.resizable(False,False)
    background=PhotoImage(file='images/fonds/fondcreationequipe.png')
    bg=Label(master, image=background)
    bg.place(x=-2,y=-2)
    master.iconbitmap('images/sprites3g/icones/hyperball.ico')
    
    #variables
    
    nom_du_pokemon = tk.StringVar()
    nom_du_pokemon.set('Bulbizarre')
    isshiny = tk.IntVar()
    
    equipe=[]

    for i in range(6):
        file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt')
        equipe.append(file.read())
        file.close
    
    
    membre=1
        
    #fonctions
                
    def afficher_pokemon():
    
        if isshiny.get() == 1:
            
            imgpokemon = Image.open('images/sprites3g/shiny/'+nom_du_pokemon.get()+'.png')
            imgpokemon = ImageTk.PhotoImage(imgpokemon)

            
        else:
            
            imgpokemon = Image.open('images/sprites3g/'+nom_du_pokemon.get()+'.png')
            imgpokemon = ImageTk.PhotoImage(imgpokemon)
        
        pokemon=Label(master, image=imgpokemon,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
        pokemon.config(image=imgpokemon)
        pokemon.im=imgpokemon
        pokemon.place(x=2,y=230)
        
        
        pokemon.bind("<Button-1>", lambda event:cri_pokemon())

    def combobox_num():
    
        etiquettenumimg=PhotoImage(file='images/fonds/etiquettenumequipe.png')
        etiquettenum=Label(master,image=etiquettenumimg,borderwidth=0, highlightthickness=0)
        etiquettenum.place(x=140,y=228)
        etiquettenum.photo=etiquettenumimg
        
        global posx
        posx=128
        place=0
        
        def lettre(label,img,i):
            
            global posx
            posx+=12
            path = ('images/font3g/'+i+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(master,image=img,borderwidth=0, highlightthickness=0)
            label.place(x=posx,y=232)
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
            
    def combobox_nom(event):
    
        etiquetteimg=PhotoImage(file='images/fonds/etiquette3g.png')
        etiquette=Label(master,image=etiquetteimg,borderwidth=0, highlightthickness=0)
        etiquette.place(x=0,y=170)
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
                label=Label(master,image=img,borderwidth=0, highlightthickness=0)
                label.pack()
                label.place(x=posx,y=180)
                label.photo=img
            else:
                path = ('images/font3g/'+i+'.png')
                img = ImageTk.PhotoImage(Image.open(path))
                label=Label(master,image=img,borderwidth=0, highlightthickness=0)
                label.pack()
                label.place(x=posx,y=180)
                label.photo=img 
            
        
        for i in nom_du_pokemon.get():
            
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i)
        
        
        
        combobox_num()
        afficher_pokemon()
        #afficher_icone()
        stats_num()
    
    def stats_num():
    
        etiquettenumimg=PhotoImage(file='images/fonds/etiquettestatsequipe.png')
        etiquettenum=Label(master,image=etiquettenumimg,borderwidth=0, highlightthickness=0)
        etiquettenum.place(x=312,y=174)
        etiquettenum.photo=etiquettenumimg
        
        global posx
        posx=342
        place=0
        
        def lettre(label,img,i,y):
            
            global posx
            posx+=12
            path = ('images/font3g/'+i+'.png')
            img = ImageTk.PhotoImage(Image.open(path))
            label=Label(master,image=img,borderwidth=0, highlightthickness=0)
            label.place(x=posx,y=y)
            label.photo=img
        
        pv = str(get_pv(str(nom_du_pokemon.get())))
            
        for i in pv:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,180)
            
        posx=402
            
        force = str(get_force(str(nom_du_pokemon.get())))
            
        for i in force:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,206)
            
        posx=402
            
        defense = str(get_defense(str(nom_du_pokemon.get())))
            
        for i in defense:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,232)
            
        posx=402
            
        vitesse = str(get_vitesse(str(nom_du_pokemon.get())))
            
        for i in vitesse:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,258)
            
        posx=402
            
        special = str(get_specialgen1(str(nom_du_pokemon.get())))
            
        for i in special:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,284)
            
        posx=442
            
        attspecial = str(get_attspec(str(nom_du_pokemon.get())))
            
        for i in attspecial:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,310)
            
        posx=442
            
        defspecial = str(get_defspec(str(nom_du_pokemon.get())))
            
        for i in defspecial:
            place+=1
            lettre(('label'+str(place)),('img'+str(place)),i,336)
        
            
    def afficher_equipe():
        
        path = ('images/fonds/etiquetteequipe'+str(equipechoisie)+'.png')
        equipeimg = ImageTk.PhotoImage(Image.open(path))
        labeequipe=Label(master,image=equipeimg,borderwidth=0, highlightthickness=0)
        labeequipe.place(x=398,y=4)
        labeequipe.photo=equipeimg
        
        def icone_membre(membre,posx,posy,nb_membre):
            
            path = ('images/sprites3g/icones/'+str((membre).replace('1',''))+'1.png')
            membreequipeimg = ImageTk.PhotoImage(Image.open(path))
            membrequipe=Label(master,image=membreequipeimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
            membrequipe.place(x=posx,y=posy)
            membrequipe.photo=membreequipeimg
            membrequipe.bind('<Button-1>',lambda event:choisir_pokemon())
            nbmembre=Label(master,text=str(nb_membre))
            
            def choisir_pokemon():
                
                global numero_membre_choisi
                
                if membre[-1] == '1':
                    isshiny.set(1)
                else:
                    isshiny.set(0)
                nom_du_pokemon.set(str(membre).replace('1',''))
                numero_membre_choisi=(nbmembre.cget('text'))
                combobox_nom('e')
            
            
        
        for membre in equipe:
            
            if equipe[0] != '':
                
                icone_membre(equipe[0],14,14,1)
                
                
            if equipe[1] != '':
                
                icone_membre(equipe[1],96,14,2)
                
                
            if equipe[2] != '':
                
                icone_membre(equipe[2],178,14,3)
                
                
            if equipe[3] != '':
                
                icone_membre(equipe[3],14,94,4)
                
                
            if equipe[4] != '':
                
                icone_membre(equipe[4],96,94,5)

                
            if equipe[5] != '':
                
                icone_membre(equipe[5],178,94,6)
                
            break
        
    def inclure_pokemon():
        
        global numero_membre_choisi
        
        if numero_membre_choisi == 0:
            
            tkinter.messagebox.showinfo(title='Action Impossible', message="Vous n'avez aucun Pokémon sélectionné!",)
            
        else:
            
            file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','w')
            if isshiny.get() == 1:
                file.write(nom_du_pokemon.get()+'1')
            else:
                file.write(nom_du_pokemon.get())
            file.close()
        afficher_equipe()
            
    
    def pokemon_suivant():
        
        if get_num(nom_du_pokemon.get()) < 251:
            for i in range(len(listenompokemon)):
                if listenompokemon[i] == nom_du_pokemon.get():
                    nom_du_pokemon.set(listenompokemon[i+1])
                    combobox_nom('event')
                    break
                    
                    
    def pokemon_precedent():
        
        if get_num(nom_du_pokemon.get()) > 1:
            for i in range(len(listenompokemon)):
                if listenompokemon[i] == nom_du_pokemon.get():
                    nom_du_pokemon.set(listenompokemon[i-1])
                    combobox_nom('event')
                    break
            
    #bouttons
    
    nompokemon=ttk.Combobox(values=listenompokemon,textvariable=nom_du_pokemon,state='readlonly',command=combobox_num())
    shiny=tk.Checkbutton(master, text='Shiny',variable=isshiny, onvalue=1, offvalue=0)
    master.bind('<Right>',lambda event:pokemon_suivant())
    master.bind('<Left>',lambda event:pokemon_precedent())
    
    path = ('images/fonds/etiquetteinclure.png')
    inclureimg = ImageTk.PhotoImage(Image.open(path))
    inclure=Label(master,image=inclureimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    inclure.place(x=146,y=322)
    inclure.photo=inclureimg
    inclure.bind('<Button-1>',lambda event:inclure_pokemon())

    #fonctions du début
    
    afficher_equipe()
    
    print(len(equipe))
    
    
    master.mainloop()