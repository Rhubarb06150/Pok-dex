import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from pokedex2proto import listenompokemon
from pokedex2proto import *
from threading import Thread
import winsound

def fenetre_equipe(master,equipechoisie):
    
    equipe=[]

    for i in range(6):
        file=open('txts/'+str(equipechoisie)+'/membre'+str(i+1)+'.txt')
        equipe.append(file.read())
        file.close
    
    master=tk.Toplevel()
    master.geometry('500x450+1000+500')
    background=PhotoImage(file='images/fonds/fondequipes.png')
    bg=Label(master, image=background)
    bg.place(x=-2,y=-2)
    master.title('Équipe')
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