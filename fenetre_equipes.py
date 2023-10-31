import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas, NW
from PIL import ImageTk, Image
from liste_pokemon import listenompokemon,listepokemon
from liste_pokemon import *
from threading import Thread
import winsound
import random
import os
import shutil

def fenetre_equipe(master,equipechoisie,nom):
    
    equipe=[]

    for i in range(6):
        file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt')
        equipe.append(file.read())
        file.close
    
    master=tk.Toplevel()

    fenetrex=int((master.winfo_screenwidth()/2)-250)
    fenetrey=int((master.winfo_screenheight()/2)-225)
    master.geometry('500x450+'+str(fenetrex)+'+'+str(fenetrey))

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
            

            if equipe[0] != '':
                
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
                        
            else:
                
                y=156
                posx=6
                
                for i in '   vide':
                    
                    place+=1
                    lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
                    
            if equipe[1] != '':
                
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
                        
            else:
                
                y=156
                posx=176
                
                for i in '   vide':
                    
                    place+=1
                    lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if equipe[2] != '':
                
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
                        
            else:
                
                y=156
                posx=346
                
                for i in '   vide':
                    
                    place+=1
                    lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if equipe[3] != '':
                
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
                        
            else:
                
                y=340
                posx=6
                
                for i in '   vide':
                    
                    place+=1
                    lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            if equipe[4] != '':
                
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
                        
            else:
                
                y=340
                posx=176
                
                for i in '   vide':
                    
                    place+=1
                    lettre(('label'+str(place)),('img'+str(place)),i,y)
                
                    
            if equipe[5] != '':
                
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
                        
            else:
                
                y=340
                posx=346
                
                for i in '   vide':
                    
                    place+=1
                    lettre(('label'+str(place)),('img'+str(place)),i,y)
                    
            break
    
    def voir_vers_gerer():
        
        xmaster=master.winfo_x()
        ymaster=master.winfo_y()
        master.destroy()
        creation_equipe('equipe',equipechoisie,xmaster,ymaster,None)
        
    
    gererimg = Image.open('images/fonds/gererlequipe.png')
    gererimg = ImageTk.PhotoImage(gererimg)
    gerer=Label(master, image=gererimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    gerer.config(image=gererimg)
    gerer.im=gererimg
    gerer.place(x=10,y=424)
    gerer.bind('<Button-1>',lambda event:voir_vers_gerer())
                
    master.bind('<Escape>',lambda event:master.destroy())
            
    afficher_equipe()
    master.mainloop()
    
    
    
def choix_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")

    fenetrex=int((master.winfo_screenwidth()/2)-112)
    fenetrey=int((master.winfo_screenheight()/2)-116)

    master.geometry('224x232+'+str(fenetrex)+'+'+str(fenetrey))

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
    equipe1.bind('<Button-1>',lambda event:choix_voir(1))
    
    #Équipe 2
    
    equipe2img = Image.open('images/fonds/equipe2.png')
    equipe2img = ImageTk.PhotoImage(equipe2img)
    equipe2=Label(master, image=equipe2img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe2.config(image=equipe2img)
    equipe2.im=equipe2img
    equipe2.place(x=114,y=4)
    equipe2.bind('<Button-1>',lambda event:choix_voir(2))
    
    #Équipe 3
    
    equipe3img = Image.open('images/fonds/equipe3.png')
    equipe3img = ImageTk.PhotoImage(equipe3img)
    equipe3=Label(master, image=equipe3img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe3.config(image=equipe3img)
    equipe3.im=equipe3img
    equipe3.place(x=4,y=54)
    equipe3.bind('<Button-1>',lambda event:choix_voir(3))
    
    #Équipe 4
    
    equipe4img = Image.open('images/fonds/equipe4.png')
    equipe4img = ImageTk.PhotoImage(equipe4img)
    equipe4=Label(master, image=equipe4img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe4.config(image=equipe4img)
    equipe4.im=equipe2img
    equipe4.place(x=114,y=54)
    equipe4.bind('<Button-1>',lambda event:choix_voir(4))
    
    #Équipe 5
    
    equipe5img = Image.open('images/fonds/equipe5.png')
    equipe5img = ImageTk.PhotoImage(equipe5img)
    equipe5=Label(master, image=equipe5img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe5.config(image=equipe5img)
    equipe5.im=equipe5img
    equipe5.place(x=4,y=102)
    equipe5.bind('<Button-1>',lambda event:choix_voir(5))
    
    #Équipe 6
    
    equipe6img = Image.open('images/fonds/equipe6.png')
    equipe6img = ImageTk.PhotoImage(equipe6img)
    equipe6=Label(master, image=equipe6img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe6.config(image=equipe6img)
    equipe6.im=equipe6img
    equipe6.place(x=114,y=102)
    equipe6.bind('<Button-1>',lambda event:choix_voir(6))
    
    #Équipe 7
    
    equipe7img = Image.open('images/fonds/equipe7.png')
    equipe7img = ImageTk.PhotoImage(equipe7img)
    equipe7=Label(master, image=equipe7img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe7.config(image=equipe7img)
    equipe7im=equipe7img
    equipe7.place(x=4,y=152)
    equipe7.bind('<Button-1>',lambda event:choix_voir(7))
    
    #Équipe 8
    
    equipe8img = Image.open('images/fonds/equipe8.png')
    equipe8img = ImageTk.PhotoImage(equipe8img)
    equipe8=Label(master, image=equipe8img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe8.config(image=equipe8img)
    equipe8.im=equipe8img
    equipe8.place(x=114,y=152)
    equipe8.bind('<Button-1>',lambda event:choix_voir(8))
    
    
    def choix_voir(equipe):
        master.destroy()
        fenetre_equipe('equipe',equipe,('Équipe '+str(equipe)))
    
    master.bind('<p>',lambda event:choix_equipe_plus('choix_plus_equipes','voir',None,master))
    master.bind('<P>',lambda event:choix_equipe_plus('choix_plus_equipes','voir',None,master))

    master.bind('<Escape>',lambda event:master.destroy())

    master.mainloop()
    
def choix_creation_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")

    fenetrex=int((master.winfo_screenwidth()/2)-112)
    fenetrey=int((master.winfo_screenheight()/2)-116)

    master.geometry('224x232+'+str(fenetrex)+'+'+str(fenetrey))

    master.resizable(False,False)
    background=PhotoImage(file='images/fonds/fondgererequipes.png')
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
    equipe1.bind('<Button-1>',lambda event:choix_gerer(1))
    
    #Équipe 2
    
    equipe2img = Image.open('images/fonds/equipe2.png')
    equipe2img = ImageTk.PhotoImage(equipe2img)
    equipe2=Label(master, image=equipe2img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe2.config(image=equipe2img)
    equipe2.im=equipe2img
    equipe2.place(x=114,y=4)
    equipe2.bind('<Button-1>',lambda event:choix_gerer(2))
    
    #Équipe 3
    
    equipe3img = Image.open('images/fonds/equipe3.png')
    equipe3img = ImageTk.PhotoImage(equipe3img)
    equipe3=Label(master, image=equipe3img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe3.config(image=equipe3img)
    equipe3.im=equipe3img
    equipe3.place(x=4,y=54)
    equipe3.bind('<Button-1>',lambda event:choix_gerer(3))
    
    #Équipe 4
    
    equipe4img = Image.open('images/fonds/equipe4.png')
    equipe4img = ImageTk.PhotoImage(equipe4img)
    equipe4=Label(master, image=equipe4img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe4.config(image=equipe4img)
    equipe4.im=equipe2img
    equipe4.place(x=114,y=54)
    equipe4.bind('<Button-1>',lambda event:choix_gerer(4))
    
    #Équipe 5
    
    equipe5img = Image.open('images/fonds/equipe5.png')
    equipe5img = ImageTk.PhotoImage(equipe5img)
    equipe5=Label(master, image=equipe5img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe5.config(image=equipe5img)
    equipe5.im=equipe5img
    equipe5.place(x=4,y=102)
    equipe5.bind('<Button-1>',lambda event:choix_gerer(5))
    
    #Équipe 6
    
    equipe6img = Image.open('images/fonds/equipe6.png')
    equipe6img = ImageTk.PhotoImage(equipe6img)
    equipe6=Label(master, image=equipe6img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe6.config(image=equipe6img)
    equipe6.im=equipe6img
    equipe6.place(x=114,y=102)
    equipe6.bind('<Button-1>',lambda event:choix_gerer(6))
    
    #Équipe 7
    
    equipe7img = Image.open('images/fonds/equipe7.png')
    equipe7img = ImageTk.PhotoImage(equipe7img)
    equipe7=Label(master, image=equipe7img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe7.config(image=equipe7img)
    equipe7im=equipe7img
    equipe7.place(x=4,y=152)
    equipe7.bind('<Button-1>',lambda event:choix_gerer(7))
    
    #Équipe 8
    
    equipe8img = Image.open('images/fonds/equipe8.png')
    equipe8img = ImageTk.PhotoImage(equipe8img)
    equipe8=Label(master, image=equipe8img ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    equipe8.config(image=equipe8img)
    equipe8.im=equipe8img
    equipe8.place(x=114,y=152)
    equipe8.bind('<Button-1>',lambda event:choix_gerer(8))
    

    def choix_gerer(equipe):
        master.destroy()
        creation_equipe('equipe',equipe,50,600,None)

    master.bind('<p>',lambda event:choix_equipe_plus('choix_plus_equipes','gerer',None,master))
    master.bind('<P>',lambda event:choix_equipe_plus('choix_plus_equipes','gerer',None,master))

    master.bind('<Escape>',lambda event:master.destroy())

    master.mainloop()
    
numero_membre_choisi=0
    
frames=0
frameicone=0

file=open('txts/dernier.txt')
dernier_pokemon=file.read()
file.close()

def creation_equipe(master,equipechoisie,x,y,event):
    
    
    global numero_membre_choisi
    numero_membre_choisi=0
    
    master=tk.Toplevel()
    master.title("Gestion de l'équipe")
    master.geometry('500x400+'+str(x)+'+'+str(y))
    master.resizable(False,False)
    background=PhotoImage(file='images/fonds/fondcreationequipe.png')
    bg=Label(master, image=background)
    bg.place(x=-2,y=-2)
    master.iconbitmap('images/sprites3g/icones/hyperball.ico')
    
    #LABELS______________________________________________________
    
    
        #IMAGES MISES DE BASE

    #_________________________________________

    #LETTRES DU NOM

    listelabel=[]
            
    path=PhotoImage(file='images/font3g/espace.png')
            
    label1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label1)
    label1.place(x=20,y=180)
            
    label2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label2)
    label2.place(x=32,y=180)        

    label3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label3)
    label3.place(x=44,y=180)

    label4=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label4)
    label4.place(x=56,y=180)

    label5=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label5)
    label5.place(x=68,y=180)

    label6=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label6)
    label6.place(x=80,y=180)

    label7=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label7)
    label7.place(x=92,y=180)

    label8=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label8)
    label8.place(x=104,y=180)

    label9=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label9)
    label9.place(x=116,y=180)

    label10=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label10)
    label10.place(x=128,y=180)

    label11=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label11)
    label11.place(x=140,y=180)

    #________________________________________________________________
    #LETTRE DU NUMERO

    listelabelnum=[]

    labelnum1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelnum.append(labelnum1)
    labelnum1.place(x=152,y=232)

    labelnum2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelnum.append(labelnum2)
    labelnum2.place(x=164,y=232)

    labelnum3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelnum.append(labelnum3)
    labelnum3.place(x=178,y=232)

    #________________________________________________________________
    #LETTRES STATS

        #PV

    listelabelpv=[]

    path=PhotoImage(file='images/font3g/underscore.png')
            
    labelpv1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelpv.append(labelpv1)
    labelpv1.place(x=354,y=180)

    labelpv2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelpv.append(labelpv2)
    labelpv2.place(x=366,y=180)

    labelpv3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelpv.append(labelpv3)
    labelpv3.place(x=378,y=180)

        #ATTAQUE

    listelabelatt=[]

    labelatt1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelatt.append(labelatt1)
    labelatt1.place(x=414,y=206)

    labelatt2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelatt.append(labelatt2)
    labelatt2.place(x=426,y=206)

    labelatt3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelatt.append(labelatt3)
    labelatt3.place(x=438,y=206)

        #DEFENSE

    listelabeldef=[]

    labeldef1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldef.append(labeldef1)
    labeldef1.place(x=414,y=232)

    labeldef2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldef.append(labeldef2)
    labeldef2.place(x=426,y=232)

    labeldef3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldef.append(labeldef3)
    labeldef3.place(x=438,y=232)

        #VITESSE

    listelabelvit=[]

    labelvit1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelvit.append(labelvit1)
    labelvit1.place(x=414,y=258)

    labelvit2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelvit.append(labelvit2)
    labelvit2.place(x=426,y=258)

    labelvit3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelvit.append(labelvit3)
    labelvit3.place(x=438,y=258)

        #SPECIAL

    listelabelspec=[]

    labelspec1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelspec.append(labelspec1)
    labelspec1.place(x=414,y=284)

    labelspec2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelspec.append(labelspec2)
    labelspec2.place(x=426,y=284)

    labelspec3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelspec.append(labelspec3)
    labelspec3.place(x=438,y=284)

        #ATTAQUE SPECIALE

    listelabelattspec=[]

    labelattspec1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelattspec.append(labelattspec1)
    labelattspec1.place(x=454,y=310)

    labelattspec2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelattspec.append(labelattspec2)
    labelattspec2.place(x=466,y=310)

    labelattspec3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabelattspec.append(labelattspec3)
    labelattspec3.place(x=478,y=310)

        #DEFENSE SPECIALE

    listelabeldefspec=[]

    labeldefspec1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldefspec.append(labeldefspec1)
    labeldefspec1.place(x=454,y=336)

    labeldefspec2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldefspec.append(labeldefspec2)
    labeldefspec2.place(x=466,y=336)

    labeldefspec3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabeldefspec.append(labeldefspec3)
    labeldefspec3.place(x=478,y=336)

    
    
    #LABELS______________________________________________________
    
    
    #IMAGES A MODIFIER
    
    path = ('images/fonds/chromatiqueoff.png')
    chromatiqueimg = ImageTk.PhotoImage(Image.open(path))
    chromatiquelb=Label(master,image=chromatiqueimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    chromatiquelb.place(x=146,y=274)
    chromatiquelb.photo=chromatiqueimg
    
    path = PhotoImage('images/sprites3g/icones/empty.png')
    pokemon=Label(master, image=path,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    pokemon.place(x=6,y=230)

    
    path = ('images/types/empty.png')
    type1img = ImageTk.PhotoImage(Image.open(path))
    type1=Label(master,image=type1img,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    type1.place(x=214,y=202)
    type1.photo=type1img
    
    path = ('images/types/empty.png')
    type2img = ImageTk.PhotoImage(Image.open(path))
    type2=Label(master,image=type2img,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    type2.place(x=214,y=232)
    type2.photo=type2img
    
    
    
    #variables
    
    nom_du_pokemon = tk.StringVar()
    file=open('txts/dernier.txt','r')
    nom_du_pokemon.set(file.read())
    file.close
    isshiny = tk.IntVar()
    
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
    
    def lettre(mot,liste,verifshiny):
    
        if verifshiny == True:
            
            for i in range(len(mot)):
                
                if isshiny.get() == 0:
                        
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
                else:
                        
                    if mot[i] == ' ':
                                
                        path = ('images/font3g/shiny/espace.png')
                        img = ImageTk.PhotoImage(Image.open(path))
                                
                        liste[i].configure(image=img)
                        liste[i].im=img

                            
                    else:
                                
                        path = ('images/font3g/shiny/'+mot[i]+'.png')
                        img = ImageTk.PhotoImage(Image.open(path))
                                
                        liste[i].configure(image=img)
                        liste[i].im=img
        else:
            
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

    def afficher_types():
        
        path = ('images/types/'+get_type1(nom_du_pokemon.get())+'.png')
        type1img = ImageTk.PhotoImage(Image.open(path))
        type1.config(image=type1img)
        type1.photo=path
        type1.im=type1img
        
        if get_type2(nom_du_pokemon.get()) != False:
            
            path = ('images/types/'+get_type2(nom_du_pokemon.get())+'.png')
            type2img = ImageTk.PhotoImage(Image.open(path))
            type2.config(image=type2img)
            type2.photo=path
            type2.im=type2img
            
        else:
            
            path = ('images/types/empty.png')
            type2img = ImageTk.PhotoImage(Image.open(path))
            type2.config(image=type2img)
            type2.photo=path
            type2.im=type2img
            
    def lettre_num():
        
        numpkmn=int(get_num(nom_du_pokemon.get()))
        if numpkmn < 10:
            numpkmn=str('00'+str((get_num(nom_du_pokemon.get()))))
        elif numpkmn < 100:
            numpkmn=str('0'+str((get_num(nom_du_pokemon.get()))))
        else:
           numpkmn=str(numpkmn)
        
        for i in range(len(numpkmn)):
      
                path = ('images/font3g/'+numpkmn[i]+'.png')
                img = ImageTk.PhotoImage(Image.open(path))
                        
                listelabelnum[i].configure(image=img)
                listelabelnum[i].im=img
                
    def affichage():
        
        lettre_num()
        lettre('           ',listelabel,False)
        lettre('   ',listelabelpv,False)
        lettre('   ',listelabelatt,False)
        lettre('   ',listelabeldef,False)
        lettre('   ',listelabelvit,False)
        lettre('   ',listelabelspec,False)
        lettre('   ',listelabelattspec,False)
        lettre('   ',listelabeldefspec,False)
        
        pv=str(get_pv(nom_du_pokemon.get()))
        att=str(get_force(nom_du_pokemon.get()))
        defense=str(get_defense(nom_du_pokemon.get()))
        vit=str(get_vitesse(nom_du_pokemon.get()))
        spec=str(get_specialgen1(nom_du_pokemon.get()))
        attspec=str(get_attspec(nom_du_pokemon.get()))
        defspec=str(get_defspec(nom_du_pokemon.get()))
        
        lettre(nom_du_pokemon.get(),listelabel,True)
        lettre(pv,listelabelpv,False)
        lettre(att,listelabelatt,False)
        lettre(defense,listelabeldef,False)
        lettre(vit,listelabelvit,False)
        lettre(spec,listelabelspec,False)
        lettre(attspec,listelabelattspec,False)
        lettre(defspec,listelabeldefspec,False)
        
        
    
    
    
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
        
        pokemon.config(image=imgpokemon)
        pokemon.im=imgpokemon

        pokemon.bind("<Button-1>", lambda event:cri_pokemon())



    def combobox_nom(event):
        
#___________________________________________________________________________________        


        afficher_pokemon()
        chromatique()
        affichage()
        afficher_types()
        
        
#___________________________________________________________________________________
          
    def choisir_pokemon(num):
        
        global dernier_pokemon
                
        global numero_membre_choisi
                
        if equipe[num-1]!='':
                
            if (equipe[num-1])[-1] == '1':
                isshiny.set(1)
            else:
                isshiny.set(0)
                        
            numero_membre_choisi=num
            nom_du_pokemon.set(str(equipe[(int(numero_membre_choisi)-1)]).replace('1',''))
            
            file=open('txts/dernier.txt','w')
            file.write((str(equipe[(int(numero_membre_choisi)-1)]).replace('1','')))
            file.close()
            
            file=open('txts/dernier.txt','r')
            dernier_pokemon=file.read()
            file.close()
            
            for i in range(6):
                
                cheminicone = Image.open('images/fonds/icone.png')
                cheminicone = ImageTk.PhotoImage(cheminicone)
                listelabeliconefond[i-1].config(image=cheminicone)
                
                listelabelicone[i-1].config(bg='#f8b0a0')
                listelabelicone[i-1].im=cheminicone
                
            cheminiconechoisi = Image.open('images/fonds/iconechoisi.png')
            cheminiconechoisi = ImageTk.PhotoImage(cheminiconechoisi)
            listelabeliconefond[num-1].config(image=cheminiconechoisi)
            
            listelabelicone[num-1].config(bg='#f04028')
            listelabelicone[num-1].im=cheminiconechoisi
            
            
            combobox_nom('e')
            titre()
            chromatique()
                        
        else:
            
            
            
            for i in range(6):
                
                cheminicone = Image.open('images/fonds/icone.png')
                cheminicone = ImageTk.PhotoImage(cheminicone)
                listelabeliconefond[i-1].config(image=cheminicone)
                
                listelabelicone[i-1].config(bg='#f8b0a0')
                listelabelicone[i-1].im=cheminicone
                
            cheminiconechoisi = Image.open('images/fonds/iconechoisi.png')
            cheminiconechoisi = ImageTk.PhotoImage(cheminiconechoisi)
            listelabeliconefond[num-1].config(image=cheminiconechoisi)
            
            listelabelicone[num-1].config(bg='#f04028')
            listelabelicone[num-1].im=cheminiconechoisi
                    
            nom_du_pokemon.set(dernier_pokemon)
            numero_membre_choisi=(num)
            titre()
            chromatique()
    
    
    
    #ICONES
        
    listelabeliconefond=[]
        
    path=PhotoImage(file='images/fonds/icone.png')
    icone1fond=Label(master, image=path, borderwidth=0, highlightthickness=0, bg ='#b88898')
    icone1fond.place(x=10,y=10)
    icone1fond.im=path
    listelabeliconefond.append(icone1fond)
    
    path=PhotoImage(file='images/fonds/icone.png')
    icone2fond=Label(master, image=path, borderwidth=0, highlightthickness=0, bg ='#b88898')
    icone2fond.place(x=92,y=10)
    icone2fond.im=path
    listelabeliconefond.append(icone2fond)
    
    path=PhotoImage(file='images/fonds/icone.png')
    icone3fond=Label(master, image=path, borderwidth=0, highlightthickness=0, bg ='#b88898')
    icone3fond.place(x=174,y=10)
    icone3fond.im=path
    listelabeliconefond.append(icone3fond)
    
    path=PhotoImage(file='images/fonds/icone.png')
    icone4fond=Label(master, image=path, borderwidth=0, highlightthickness=0, bg ='#b88898')
    icone4fond.place(x=10,y=90)
    icone4fond.im=path
    listelabeliconefond.append(icone4fond)
    
    path=PhotoImage(file='images/fonds/icone.png')
    icone5fond=Label(master, image=path, borderwidth=0, highlightthickness=0, bg ='#b88898')
    icone5fond.place(x=92,y=90)
    icone5fond.im=path
    listelabeliconefond.append(icone5fond)
    
    path=PhotoImage(file='images/fonds/icone.png')
    icone6fond=Label(master, image=path, borderwidth=0, highlightthickness=0, bg ='#b88898')
    icone6fond.place(x=174,y=90)
    icone6fond.im=path
    listelabeliconefond.append(icone6fond)
    
    
    listelabelicone=[]
        
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone1=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone1.pack()
    icone1.place(x=14,y=14)
    icone1text=Label(master, text='1')
    icone1.bind('<Button-1>',lambda event:choisir_pokemon(1))
    listelabelicone.append(icone1)
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone2=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone2.place(x=96,y=14)
    icone2text=Label(master, text='2')
    icone2.bind('<Button-1>',lambda event:choisir_pokemon(2))
    listelabelicone.append(icone2)
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone3=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone3.place(x=178,y=14)
    icone3text=Label(master, text='3')
    icone3.bind('<Button-1>',lambda event:choisir_pokemon(3))
    listelabelicone.append(icone3)
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone4=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone4.place(x=14,y=94)
    icone4text=Label(master, text='4')
    icone4.bind('<Button-1>',lambda event:choisir_pokemon(4))
    listelabelicone.append(icone4)
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone5=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone5.place(x=96,y=94)
    icone5text=Label(master, text='5')
    icone5.bind('<Button-1>',lambda event:choisir_pokemon(5))
    listelabelicone.append(icone5)
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone6=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone6.place(x=178,y=94)
    icone6text=Label(master, text='6')
    icone6.bind('<Button-1>',lambda event:choisir_pokemon(6))
    listelabelicone.append(icone6)
    
    
        #ÉTOILES SHINY
        
    def icone_membre(label,membre,num):
            
        if membre !='':
            
            path = ('images/sprites3g/icones/'+str((membre).replace('1',''))+str(num)+'.png')
            membreequipeimg = ImageTk.PhotoImage(Image.open(path))
            label.config(image=membreequipeimg)
            label.photo=membreequipeimg
                
        else:
                
            path = ('images/sprites3g/icones/empty.png')
            membreequipeimg = ImageTk.PhotoImage(Image.open(path))
            label.config(image=membreequipeimg)
            label.photo=membreequipeimg
            
    def afficher_equipe():
        
        for membre in equipe:
            
            icone_membre(icone1,equipe[0],1)
                
            icone_membre(icone2,equipe[1],1)
                
            icone_membre(icone3,equipe[2],1)
                
            icone_membre(icone4,equipe[3],1)
                
            icone_membre(icone5,equipe[4],1)

            icone_membre(icone6,equipe[5],1)
                
            break
        titre()
        chromatique()
        
    def supprimer_pokemon():
        
        global numero_membre_choisi
        
        if numero_membre_choisi == 0:
            
            tkinter.messagebox.showinfo(title='Action Impossible', message="Vous n'avez aucun Pokémon sélectionné!",)
            
        else:
            
            remplacer = tkinter.messagebox.askquestion(title='Attention!', message=("Êtes-vous sur de vouloir supprimer "+str(equipe[int(numero_membre_choisi)-1]).replace('1',''))+" du Slot "+str(numero_membre_choisi)+"?")
            
            if remplacer == 'yes':
                
                file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','w')
                file.write('')
                file.close()
                
                    
                file=open('txts/num.txt','w+')
                file.write(str(numero_membre_choisi))
                file.close
                    
                file=open('txts/num.txt','r')
                file.close
                
                xmaster=master.winfo_x()
                ymaster=master.winfo_y()
                master.destroy()
                creation_equipe('equipe',equipechoisie,xmaster,ymaster,'select')
            
    def inclure_pokemon():
        
        global numero_membre_choisi
                    
        file=open('txts/num.txt','w+')
        file.write(str(numero_membre_choisi))
        file.close
                    
        file=open('txts/num.txt','r')
        file.close
        
        dern_poke=open('txts/dernier.txt','r')
        dernier_pokemon=str(dern_poke.read())
        dern_poke.close
        
        nom_du_pokemon.set(str(dernier_pokemon).replace('1',''))
        
        if numero_membre_choisi == 0:
            
            tkinter.messagebox.showinfo(title='Action Impossible', message="Vous n'avez aucun Slot sélectionné!",)
            
        else:
             
            fichier_membre=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','r')
            fichier_membre_txt=str(fichier_membre.read())
            fichier_membre.close
            if fichier_membre_txt != '':
                
                remplacer = tkinter.messagebox.askquestion(title='Remplacer le Pokémon', message=("Voulez vous remplacer "+str(equipe[(numero_membre_choisi)-1])+" par "+str(nom_du_pokemon.get()+" dans le Slot "+str(numero_membre_choisi)+"?")))
            
                if remplacer == 'yes':
                    
                    file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','w')
                    if isshiny.get() == 1:
                        file.write(nom_du_pokemon.get()+'1')
                    else:
                        file.write(nom_du_pokemon.get())
                    file.close()
                    
                    xmaster=master.winfo_x()
                    ymaster=master.winfo_y()
                    
                    master.destroy()
                    creation_equipe('equipe',equipechoisie,xmaster,ymaster,'select')
                    
                    
            else:
            
                remplacer = tkinter.messagebox.askquestion(title='Inclure le Pokémon', message=("Voulez vous inclure "+str(nom_du_pokemon.get())+" dans le Slot "+str(numero_membre_choisi)+"?"),)

                file=open('txts/num.txt','w+')
                file.write(str(numero_membre_choisi))
                file.close
                    
                file=open('txts/num.txt','r')
                file.close
                
                if remplacer == 'yes':
                    
                    file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','w')
                    if isshiny.get() == 1:
                        file.write(nom_du_pokemon.get()+'1')
                    else:
                        file.write(nom_du_pokemon.get())
                    file.close()
                    
                    xmaster=master.winfo_x()
                    ymaster=master.winfo_y()
                    
                    
                    
                    master.destroy()
                    creation_equipe('equipe',equipechoisie,xmaster,ymaster,'select')
                    
    master.bind('<Return>',lambda event:inclure_pokemon())
    master.bind('<Delete>',lambda event:inclure_pokemon())
    master.bind('<BackSpace>',lambda event:inclure_pokemon())
            
    def pokemon_suivant():
        
        file=open('txts/dernier.txt','r')
        nom_du_pokemon.set(file.read())
        file.close()
        
        if get_num(nom_du_pokemon.get()) < 386:
            for i in range(len(listenompokemon)):
                if listenompokemon[i] == nom_du_pokemon.get():
                    nom_du_pokemon.set(listenompokemon[i+1])
                    combobox_nom('event')
                    
                    file=open('txts/dernier.txt','w')
                    file.write((str(nom_du_pokemon.get()).replace('1','')))
                    file.close()
                    
                    file=open('txts/dernier.txt','r')
                    dernier_pokemon=file.read()
                    file.close()
                    
                    break
        nom_du_pokemon.set(nom_du_pokemon.get())
                    
                    
    def pokemon_precedent():
        
        file=open('txts/dernier.txt','r')
        nom_du_pokemon.set(file.read())
        file.close()
        
        if get_num(nom_du_pokemon.get()) > 1:
            for i in range(len(listenompokemon)):
                if listenompokemon[i] == nom_du_pokemon.get():
                    nom_du_pokemon.set(listenompokemon[i-1])
                    combobox_nom('event')
                    
                    file=open('txts/dernier.txt','w')
                    file.write((str(nom_du_pokemon.get()).replace('1','')))
                    file.close()
                    
                    file=open('txts/dernier.txt','r')
                    dernier_pokemon=file.read()
                    file.close()
                    
                    break
        nom_du_pokemon.set(nom_du_pokemon.get())
                
    def titre():
        
        if str(numero_membre_choisi) != '0':
            if str(equipe[int(numero_membre_choisi)-1]) == '':
                master.title("Gestion de l'équipe "+str(equipechoisie)+" : Slot: "+str(numero_membre_choisi)+' (Vide)')
            else:
                master.title("Gestion de l'équipe "+str(equipechoisie)+" : Slot: "+str(numero_membre_choisi)+' ('+str(equipe[int(numero_membre_choisi)-1]).replace('1','')+')')
        else:
            master.title("Gestion de l'équipe "+str(equipechoisie)+" : Aucun slot sélectionné")
            
            
    def chroma_switch():
        
        if isshiny.get()==0:
            isshiny.set(1)
        else:
            isshiny.set(0)
        chromatique()
        combobox_nom('shiny')
        file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','w')
        if isshiny.get() == 1:
            file.write(nom_du_pokemon.get()+'1')
        else:
            file.write(nom_du_pokemon.get())
        file.close()
    
            
    def chromatique():
        
        if isshiny.get() == 0:
            
            path = ('images/fonds/chromatiqueoff.png')
            chromatiqueimg = ImageTk.PhotoImage(Image.open(path))
            chromatiquelb.config(image=chromatiqueimg)
            chromatiquelb.photo=chromatiqueimg
            
            chromatiquelb.bind('<Button-1>',lambda event:chroma_switch())
            
        else:
            
            path = ('images/fonds/chromatiqueon.png')
            chromatiqueimg = ImageTk.PhotoImage(Image.open(path))
            chromatiquelb.config(image=chromatiqueimg)
            chromatiquelb.photo=chromatiqueimg
            
            chromatiquelb.bind('<Button-1>',lambda event:chroma_switch())
            
            
    def effacer_equipe():
        
        effacermsg = tkinter.messagebox.askquestion(title='Attention!', message="Voulez-vous vraiment supprimer tout les membres de l'équipe?")
        
        if effacermsg == 'yes':
            
            for i in range(6):
                
                file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt','w')
                file.write('')
                file.close
                
            xmaster=master.winfo_x()
            ymaster=master.winfo_y()
            master.destroy()
            creation_equipe('equipe',equipechoisie,xmaster,ymaster,'gerer')
            
    def renommer_equipe():
        
        if str(equipechoisie)=='1' or str(equipechoisie)=='2' or str(equipechoisie)=='3' or str(equipechoisie)=='4' or str(equipechoisie)=='5' or str(equipechoisie)=='6' or str(equipechoisie)=='7' or str(equipechoisie)=='8':
            renommer_msg = tkinter.messagebox.showinfo(title="Action impossible",message="Vous ne pouvez pas renommer l'équipe "+str(equipechoisie)+", car elle fait partie des 8 équipes par défaut, vous pouvez uniquement renommer les équipes que vous avez  vous-même créées")
        else:
            nouveau_nom=choix_equipe_plus('renommer','renommer',equipechoisie,master)
            
    def supprimer_equipe():
        if str(equipechoisie)=='1' or str(equipechoisie)=='2' or str(equipechoisie)=='3' or str(equipechoisie)=='4' or str(equipechoisie)=='5' or str(equipechoisie)=='6' or str(equipechoisie)=='7' or str(equipechoisie)=='8':
            supprimer_msg = tkinter.messagebox.showinfo(title="Action impossible",message="Vous ne pouvez pas supprimer l'équipe "+str(equipechoisie)+", car elle fait partie des 8 équipes par défaut, vous pouvez uniquement supprimer les équipes que vous avez  vous-même créées")
        else:
            supprimer_msg = tkinter.messagebox.askquestion(title="Supprimer l'équipe",message="Êtes-vous sur de vouloir supprimer l'équipe "+str(equipechoisie)+", attention, cette action est irréversible!")
            if supprimer_msg == 'yes':
                master.destroy()
                shutil.rmtree("txts/equipe"+str(equipechoisie)+"/")
                supprimer_msg = tkinter.messagebox.showinfo(title="Équipe supprimée",message="L'équipe "+str(equipechoisie)+" à bien été supprimée")
                
         
        #_________________________________________________________________________________________________________________
        #PARAMETRES __________________________________________________________________________________________
        #_________________________________________________________________________________________________________________
                
                
    path = ('images/fonds/gestionequipe.png')
    retour_gestionimg = ImageTk.PhotoImage(Image.open(path))
    retour_gestion=Label(master,image=retour_gestionimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    retour_gestion.place(x=282,y=0)
    retour_gestion.photo=retour_gestionimg
    retour_gestion.bind('<Button-1>',lambda event:parametres_vers_gestion())
    retour_gestion.place_forget()
    
    path = ('images/fonds/supprimerlesmembres.png')
    supprimerlesmembresimg = ImageTk.PhotoImage(Image.open(path))
    supprimerlesmembres=Label(master,image=supprimerlesmembresimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    supprimerlesmembres.place(x=34,y=36)
    supprimerlesmembres.photo=supprimerlesmembresimg
    supprimerlesmembres.bind('<Button-1>',lambda event:effacer_equipe())
    supprimerlesmembres.place_forget()
    
    path = ('images/fonds/renommerlequipe.png')
    renommerlequipeimg = ImageTk.PhotoImage(Image.open(path))
    renommerlequipe=Label(master,image=renommerlequipeimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    renommerlequipe.place(x=34,y=84)
    renommerlequipe.photo=renommerlequipeimg
    renommerlequipe.bind('<Button-1>',lambda event:renommer_equipe())
    renommerlequipe.place_forget()
    
    path = ('images/fonds/supprimerlequipe.png')
    suprrimerlequipeimg = ImageTk.PhotoImage(Image.open(path))
    suprrimerlequipe=Label(master,image=suprrimerlequipeimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    suprrimerlequipe.place(x=34,y=132)
    suprrimerlequipe.photo=suprrimerlequipeimg
    suprrimerlequipe.bind('<Button-1>',lambda event:supprimer_equipe())
    suprrimerlequipe.place_forget()
    
    
    def gerer_vers_parametres():
        
        master.title("Paramètres de l'équipe "+str(equipechoisie))
        background=PhotoImage(file='images/fonds/fondparametresequipe.png')
        bg.config(image=background)
        bg.im=background
        
        type1.place_forget()
        type2.place_forget()
        chromatiquelb.place_forget()
        
        for i in listelabel:
            i.place_forget()
        for i in listelabelicone:
            i.place_forget()
        for i in listelabeliconefond:
            i.place_forget()
        for i in listelabelpv:
            i.place_forget()
        for i in listelabelatt:
            i.place_forget()
        for i in listelabeldef:
            i.place_forget()
        for i in listelabelspec:
            i.place_forget()
        for i in listelabelvit:
            i.place_forget()
        for i in listelabelattspec:
            i.place_forget()
        for i in listelabeldefspec:
            i.place_forget()
        for i in listelabelnum:
            i.place_forget()
        
        inclure.place_forget()
        supprimer.place_forget()
        pokemon.place_forget()
        parametres.place_forget()
        
        retour_gestion.place(x=282,y=0)
        supprimerlesmembres.place(x=34,y=36)
        renommerlequipe.place(x=34,y=84)
        suprrimerlequipe.place(x=34,y=132)
        
        master.bind('<Right>',lambda event:None)
        master.bind('<Left>',lambda event:None)
        master.bind('<Return>',lambda event:None)
        master.bind('<Delete>',lambda event:None)
        master.bind('<BackSpace>',lambda event:None)
        
    def parametres_vers_gestion():
        
        retour_gestion.place_forget()
        supprimerlesmembres.place_forget()
        renommerlequipe.place_forget()
        suprrimerlequipe.place_forget()
        
        
        titre()
        background=PhotoImage(file='images/fonds/fondcreationequipe.png')
        bg.config(image=background)
        bg.im=background
        
        icone1fond.place(x=10,y=10)
        icone2fond.place(x=92,y=10)
        icone3fond.place(x=174,y=10)
        icone4fond.place(x=10,y=90)
        icone5fond.place(x=92,y=90)
        icone6fond.place(x=174,y=90)
        
        icone1.place(x=14,y=14)
        icone2.place(x=96,y=14)
        icone3.place(x=178,y=14)
        icone4.place(x=14,y=94)
        icone5.place(x=96,y=94)
        icone6.place(x=178,y=94)
        
        inclure.place(x=146,y=322)
        supprimer.place(x=260,y=322)
        parametres.place(x=376,y=0)
        
        label1.place(x=20,y=180)
        label2.place(x=32,y=180)        
        label3.place(x=44,y=180)
        label4.place(x=56,y=180)
        label5.place(x=68,y=180)
        label6.place(x=80,y=180)
        label7.place(x=92,y=180)
        label8.place(x=104,y=180)
        label9.place(x=116,y=180)
        label10.place(x=128,y=180)
        label11.place(x=140,y=180)

        labelnum1.place(x=152,y=232)
        labelnum2.place(x=164,y=232)
        labelnum3.place(x=178,y=232)

        labelpv1.place(x=354,y=180)
        labelpv2.place(x=366,y=180)
        labelpv3.place(x=378,y=180)

        labelatt1.place(x=414,y=206)
        labelatt2.place(x=426,y=206)
        labelatt3.place(x=438,y=206)

        labeldef1.place(x=414,y=232)
        labeldef2.place(x=426,y=232)
        labeldef3.place(x=438,y=232)

        labelvit1.place(x=414,y=258)
        labelvit2.place(x=426,y=258)
        labelvit3.place(x=438,y=258)

        labelspec1.place(x=414,y=284)
        labelspec2.place(x=426,y=284)
        labelspec3.place(x=438,y=284)

        labelattspec1.place(x=454,y=310)
        labelattspec2.place(x=466,y=310)
        labelattspec3.place(x=478,y=310)

        labeldefspec1.place(x=454,y=336)
        labeldefspec2.place(x=466,y=336)
        labeldefspec3.place(x=478,y=336)
        
        chromatiquelb.place(x=146,y=274)
        pokemon.place(x=6,y=230)
        type1.place(x=214,y=202)
        type2.place(x=214,y=232)
        
        master.bind('<Right>',lambda event:pokemon_suivant())
        master.bind('<Left>',lambda event:pokemon_precedent())
        master.bind('<Return>',lambda event:inclure_pokemon())
        master.bind('<Delete>',lambda event:inclure_pokemon())
        master.bind('<BackSpace>',lambda event:inclure_pokemon())
    
        
    #LABELS______________________________________________________
        
    #bouttons
    
    
    nompokemon=ttk.Combobox(values=listenompokemon,textvariable=nom_du_pokemon,state='readlonly',command=combobox_nom('root'))
    shiny=tk.Checkbutton(master, text='Shiny',variable=isshiny, onvalue=1, offvalue=0)
    master.bind('<Right>',lambda event:pokemon_suivant())
    master.bind('<Left>',lambda event:pokemon_precedent())
    
    path = ('images/fonds/etiquetteinclure.png')
    inclureimg = ImageTk.PhotoImage(Image.open(path))
    inclure=Label(master,image=inclureimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    inclure.place(x=146,y=322)
    inclure.photo=inclureimg
    inclure.bind('<Button-1>',lambda event:inclure_pokemon())
    
    path = ('images/fonds/etiquettesupprimer.png')
    supprimerimg = ImageTk.PhotoImage(Image.open(path))
    supprimer=Label(master,image=supprimerimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    supprimer.place(x=260,y=322)
    supprimer.photo=supprimerimg
    supprimer.bind('<Button-1>',lambda event:supprimer_pokemon())
    
    path = ('images/fonds/parametresequipe.png')
    parametresimg = ImageTk.PhotoImage(Image.open(path))
    parametres=Label(master,image=parametresimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    parametres.place(x=376,y=0)
    parametres.photo=parametresimg
    parametres.bind('<Button-1>',lambda event:gerer_vers_parametres())
    
    
    #fonctions du début
    

    afficher_equipe()
    
    if event == 'select':
        file=open('txts/num.txt')
        pokemon_a_choisir=file.read()
        choisir_pokemon(int(pokemon_a_choisir))
        file.close
        
    file=open('txts/dernier.txt')
    nom_du_pokemon.set(file.read())
    file.close
    
    afficher_types()

    master.bind('<Escape>',lambda event:master.destroy())
    
    master.mainloop()
    
def choix_equipe_plus(master,pos,equipeorigine,fenetre):
    
    master=tk.Toplevel()
    master.title("Plus d'Équipes")

    fenetrex=int((master.winfo_screenwidth()/2)-100)
    fenetrey=int((master.winfo_screenheight()/2)-50)

    master.geometry('200x100+'+str(fenetrex)+'+'+str(fenetrey))
    master.resizable(False,False)
    
    background=PhotoImage(file='images/fonds/nouveaunom.png')
    bg=Label(master, image=background)
    bg.place(x=-2,y=-2)
    
    master.iconbitmap('images/sprites3g/icones/hyperball.ico')
    
    listelabel=[]
    
    path=PhotoImage(file='images/font3g/espace.png')
    
    label01=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label01)
    label01.place(x=30,y=22)
            
    label0=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label0)
    label0.place(x=42,y=22)
    
    label1=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label1)
    label1.place(x=54,y=22)
            
    label2=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label2)
    label2.place(x=66,y=22)
    
    label3=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label3)
    label3.place(x=78,y=22)
            
    label4=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label4)
    label4.place(x=90,y=22)
    
    label5=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label5)
    label5.place(x=102,y=22)
            
    label6=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label6)
    label6.place(x=114,y=22)
    
    label7=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label7)
    label7.place(x=126,y=22)
            
    label8=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label8)
    label8.place(x=138,y=22)
    
    label9=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label9)
    label9.place(x=150,y=22)
            
    label10=Label(master,image=path,borderwidth=0, highlightthickness=0)
    listelabel.append(label10)
    label10.place(x=162,y=22)
    
    cherche=Entry(master)
    cherche.place(x=-50,y=-50)
    cherche.focus_set()
    bg.place(x=-2,y=-2)
    
    def lettre(effacer,liste):
        
        mot=cherche.get()
        cherche.delete(12,END)
        
        if effacer!='':
            
            for i in range(len(listelabel)):
            
                mot=''
                path = ('images/font3g/espace.png')
                img = ImageTk.PhotoImage(Image.open(path))
                                
                listelabel[i].configure(image=img, borderwidth=0, highlightthickness=0, bg='#f04028')
                listelabel[i].im=img
            
        else:
            
            for i in range((len(mot))):
                
                if i == 12:
                    break
                    
                if mot[i] == ' ':
                            
                    effacer_fonction(listelabel)
                    
                elif mot[i] == '':
                            
                    path = ('images/font3g/nombres/espace.png')
                    img = ImageTk.PhotoImage(Image.open(path))
                            
                    liste[i].configure(image=img, borderwidth=0, highlightthickness=0, bg='#f04028')
                    liste[i].im=img
                    
                elif mot[i] == '_':
                            
                    path = ('images/font3g/nombres/underscore.png')
                    img = ImageTk.PhotoImage(Image.open(path))
                            
                    liste[i].configure(image=img, borderwidth=0, highlightthickness=0, bg='#f04028')
                    liste[i].im=img
                    
                else:
                            
                    path = ('images/font3g/'+mot[i]+'.png')
                    img = ImageTk.PhotoImage(Image.open(path))
                            
                    liste[i].configure(image=img, borderwidth=0, highlightthickness=0, bg='#f04028')
                    liste[i].im=img
            

    def effacer_fonction(liste):
        
        mot=cherche.get()
        cherche.delete(0,len(mot))
        
        lettre('e',listelabel)
        
        path = ('images/font3g/espace.png')
        img = ImageTk.PhotoImage(Image.open(path))
                
                
        for i in range(len(mot)):
            listelabel[i].configure(image=img, borderwidth=0, highlightthickness=0, bg='#f04028')
            listelabel[i].im=img

    
    def creer_dossier(equipe_choix):
        
        os.mkdir('txts/equipe'+equipe_choix)
        
        membre1=open('txts/equipe'+equipe_choix+'/membre1.txt','x')
        membre2=open('txts/equipe'+equipe_choix+'/membre2.txt','x')
        membre3=open('txts/equipe'+equipe_choix+'/membre3.txt','x')
        membre4=open('txts/equipe'+equipe_choix+'/membre4.txt','x')
        membre5=open('txts/equipe'+equipe_choix+'/membre5.txt','x')
        membre6=open('txts/equipe'+equipe_choix+'/membre6.txt','x')
        
        
    
    def aller():
        
        if pos == None:
            a=None
        elif pos == 'gerer':
            
            if cherche.get()== '' or cherche.get()==  ' ' or cherche.get()==  '  ':
                erreur_msg = tkinter.messagebox.showinfo(title='Erreur!', message=("Veuillez entrer un nom d'équipe valide"))
                
            else:
                
                cherchetri=(cherche.get())
                path=('txts/equipe'+cherchetri)
                if not os.path.exists(path):
                    creer_dossier_msg = tkinter.messagebox.askquestion(title='Aucune équipe trouvée!', message=("Il n'y aucune équipe nommée "+cherchetri+", souhaitez vous en créer une?"))
                    if creer_dossier_msg == 'yes':
                        creer_dossier(cherchetri)
                        acceder_msg = tkinter.messagebox.askquestion(title='Équipe créée!', message=("L'équipe "+cherchetri+" à été créée souhaitez vous y accéder?"))
                        if acceder_msg == 'yes':
                            master.destroy()
                            creation_equipe('equipe',cherchetri,50,600,'gerer')
                else:
                    if fenetre!=None:
                        fenetre.destroy()
                    master.destroy()
                    creation_equipe('equipe',cherchetri,50,600,None)
                    
        elif pos == 'voir':
            
            cherchetri=(cherche.get())
            path=('txts/equipe'+cherchetri)
            if not os.path.exists(path):


                creer_dossier_msg = tkinter.messagebox.showinfo(title='Aucune équipe trouvée',message="Il n'y a aucune équipe avec cet identifiant, vous pouvez en créer une via le gestionnaire d'équipes")
                
            else:
                if fenetre!=None:
                    fenetre.destroy()
                master.destroy()
                fenetre_equipe('voir_equipe',cherchetri,('Équipe '+str(cherchetri)))
                
        elif pos == 'renommer':
            
            if str(equipeorigine)==('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8'):
                renommer_msg = tkinter.messagebox.showinfo(title="Action impossible",message="Vous ne pouvez pas renommer cette équipe car elle fait partie des 8 équipes par défaut, vous pouvez uniquement renommer les équipes que vous avez créées vous-même")
                
            else:
                
                master.title("Renommer l'équipe")
                
                cherchetri=(cherche.get())
                path=('txts/equipe'+str(cherchetri))
                
                if not os.path.exists(path):
                    renommer_msg = tkinter.messagebox.askquestion(title="Renommer l'équipe?",message=("Voulez vous renommer l'équipe "+str(equipeorigine)+" en "+str(cherchetri)+"?"))
                    if renommer_msg == 'yes':
                        xmaster=master.winfo_x()
                        ymaster=master.winfo_y()
                        fenetre.destroy()
                        master.destroy()
                        os.rename(("txts/equipe"+str(equipeorigine)+"/"),("txts/equipe"+str(cherchetri)+"/"))
                        renommer_msg = tkinter.messagebox.showinfo(title="Équipe renommée!",message=("L'équipe "+str(equipeorigine)+" à bien été renommée en "+str(cherchetri)))
                else:
                    renommer_msg = tkinter.messagebox.showinfo(title="Action impossible",message=("Une équipe nommée "+str(cherchetri)+" éxiste déja"))

        elif pos == 'chercher':

            pokemon_trouve=False
            for pokemon in listepokemon:
                if pokemon.nom == cherche.get():
                    pokemon_trouve=True
                    resultat=cherche.get()
                if pokemon.num == cherche.get():
                    pokemon_trouve=True
                    resultat=pokemon.nom   
                for i in pokemon.rawnom:
                    if i == cherche.get():
                        pokemon_trouve=True
                        resultat=pokemon.nom
            if pokemon_trouve == False:
                aucun_pokemon = tkinter.messagebox.showinfo(title="Aucun Pokémon trouvé!",message="Aucun Pokémon n'a été trouvé!")
            else:
                master.destroy()
                fenetre.set(resultat)
                equipeorigine('e')
                
    master.bind('<Key-1>',lambda event:lettre('',listelabel))
    master.bind('<Key-2>',lambda event:lettre('',listelabel))
    master.bind('<Key-3>',lambda event:lettre('',listelabel))
    master.bind('<Key-4>',lambda event:lettre('',listelabel))
    master.bind('<Key-5>',lambda event:lettre('',listelabel))
    master.bind('<Key-6>',lambda event:lettre('',listelabel))
    master.bind('<Key-7>',lambda event:lettre('',listelabel))
    master.bind('<Key-8>',lambda event:lettre('',listelabel))
    master.bind('<Key-9>',lambda event:lettre('',listelabel))
    master.bind('<Key-0>',lambda event:lettre('',listelabel))
    master.bind('<space>',lambda event:effacer_fonction(listelabel))
    master.bind('<A>',lambda event:lettre('',listelabel))
    master.bind('<a>',lambda event:lettre('',listelabel))
    master.bind('<B>',lambda event:lettre('',listelabel))
    master.bind('<b>',lambda event:lettre('',listelabel))
    master.bind('<C>',lambda event:lettre('',listelabel))
    master.bind('<c>',lambda event:lettre('',listelabel))
    master.bind('<D>',lambda event:lettre('',listelabel))
    master.bind('<d>',lambda event:lettre('',listelabel))
    master.bind('<E>',lambda event:lettre('',listelabel))
    master.bind('<e>',lambda event:lettre('',listelabel))
    master.bind('<E>',lambda event:lettre('',listelabel))
    master.bind('<e>',lambda event:lettre('',listelabel))
    master.bind('<F>',lambda event:lettre('',listelabel))
    master.bind('<f>',lambda event:lettre('',listelabel))
    master.bind('<G>',lambda event:lettre('',listelabel))
    master.bind('<g>',lambda event:lettre('',listelabel))
    master.bind('<H>',lambda event:lettre('',listelabel))
    master.bind('<h>',lambda event:lettre('',listelabel))
    master.bind('<I>',lambda event:lettre('',listelabel))
    master.bind('<i>',lambda event:lettre('',listelabel))
    master.bind('<J>',lambda event:lettre('',listelabel))
    master.bind('<j>',lambda event:lettre('',listelabel))
    master.bind('<K>',lambda event:lettre('',listelabel))
    master.bind('<k>',lambda event:lettre('',listelabel))
    master.bind('<L>',lambda event:lettre('',listelabel))
    master.bind('<l>',lambda event:lettre('',listelabel))
    master.bind('<M>',lambda event:lettre('',listelabel))
    master.bind('<m>',lambda event:lettre('',listelabel))
    master.bind('<N>',lambda event:lettre('',listelabel))
    master.bind('<n>',lambda event:lettre('',listelabel))
    master.bind('<O>',lambda event:lettre('',listelabel))
    master.bind('<o>',lambda event:lettre('',listelabel))
    master.bind('<P>',lambda event:lettre('',listelabel))
    master.bind('<p>',lambda event:lettre('',listelabel))
    master.bind('<Q>',lambda event:lettre('',listelabel))
    master.bind('<q>',lambda event:lettre('',listelabel))
    master.bind('<R>',lambda event:lettre('',listelabel))
    master.bind('<r>',lambda event:lettre('',listelabel))
    master.bind('<S>',lambda event:lettre('',listelabel))
    master.bind('<s>',lambda event:lettre('',listelabel))
    master.bind('<T>',lambda event:lettre('',listelabel))
    master.bind('<t>',lambda event:lettre('',listelabel))
    master.bind('<U>',lambda event:lettre('',listelabel))
    master.bind('<u>',lambda event:lettre('',listelabel))
    master.bind('<V>',lambda event:lettre('',listelabel))
    master.bind('<v>',lambda event:lettre('',listelabel))
    master.bind('<W>',lambda event:lettre('',listelabel))
    master.bind('<w>',lambda event:lettre('',listelabel))
    master.bind('<X>',lambda event:lettre('',listelabel))
    master.bind('<x>',lambda event:lettre('',listelabel))
    master.bind('<Y>',lambda event:lettre('',listelabel))
    master.bind('<y>',lambda event:lettre('',listelabel))
    master.bind('<Z>',lambda event:lettre('',listelabel))
    master.bind('<y>',lambda event:lettre('',listelabel))

    master.bind('<BackSpace>',lambda event:effacer_fonction(listelabel))
    
    master.bind('<Return>',lambda event:aller())
    
    master.bind('<Escape>',lambda event:master.destroy())

    master.mainloop()