import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from liste_pokemon import listenompokemon
from liste_pokemon import *
from threading import Thread
import winsound
import random

def fenetre_equipe(master,equipechoisie,nom):
    
    equipe=[]

    for i in range(6):
        file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt')
        equipe.append(file.read())
        file.close
    
    master=tk.Toplevel()
    master.geometry('500x450+1074+50')
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
        creation_equipe('equipe',equipechoisie,xmaster,ymaster)
        
    
    gererimg = Image.open('images/fonds/gererlequipe.png')
    gererimg = ImageTk.PhotoImage(gererimg)
    gerer=Label(master, image=gererimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    gerer.config(image=gererimg)
    gerer.im=gererimg
    gerer.place(x=10,y=424)
    gerer.bind('<Button-1>',lambda event:voir_vers_gerer())
                
    
            
    afficher_equipe()
    master.mainloop()
    
    
    
def choix_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")
    master.geometry('224x232+800+50')
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
    
    
    master.mainloop()
    
def choix_creation_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")
    master.geometry('224x232+800+342')
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
        creation_equipe('equipe',equipe,50,600)

    master.mainloop()
    
numero_membre_choisi=0
    
frames=0
frameicone=1

def creation_equipe(master,equipechoisie,x,y):
    
    
    
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
    
    path = ('images/fonds/etiquetteequipe'+str(equipechoisie)+'.png')
    etiquetteequipeimg = ImageTk.PhotoImage(Image.open(path))
    etiquetteequipe=Label(master,image=etiquetteequipeimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    etiquetteequipe.place(x=398,y=4)
    etiquetteequipe.photo=etiquetteequipeimg
           
    
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
      
                path = ('images/font3g/'+numpkmn[i]+'.png')
                img = ImageTk.PhotoImage(Image.open(path))
                        
                listelabelnum[i].configure(image=img)
                listelabelnum[i].im=img
                
    def affichage():
        
        lettre_num()
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
        
        pokemon.config(image=imgpokemon)
        pokemon.im=imgpokemon

        pokemon.bind("<Button-1>", lambda event:cri_pokemon())

    def iconesf():
        global frames
        global frameicone
        frames=0
        print()
        while frames == 8:
            frames+=1
            print(frames)
            if frameicone == 1:
                icone_membre(icone1,equipe[0],2)
                frameicone=2
            else:
                icone_membre(icone1,equipe[0],1)
                frameicone=1

    def combobox_nom(event):
        
#___________________________________________________________________________________        


        afficher_pokemon()
        chromatique()
        affichage()
        iconesf()
        
        
#___________________________________________________________________________________
          
    def choisir_pokemon(num):
                
        global numero_membre_choisi
                
        if equipe[num-1]!='':
                
            if (equipe[num-1])[-1] == '1':
                isshiny.set(1)
            else:
                isshiny.set(0)
                        
            numero_membre_choisi=num
            nom_du_pokemon.set(str(equipe[(int(numero_membre_choisi)-1)]).replace('1',''))
            combobox_nom('e')
            titre()
            chromatique()
                        
        else:
                    
            nom_du_pokemon.set('Bulbizarre')
            numero_membre_choisi=(num)
            titre()
            chromatique()      
    
    #ICONES
        
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone1=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone1.place(x=14,y=14)
    icone1text=Label(master, text='1')
    icone1.bind('<Button-1>',lambda event:choisir_pokemon(1))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone2=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone2.place(x=96,y=14)
    icone2text=Label(master, text='2')
    icone2.bind('<Button-1>',lambda event:choisir_pokemon(2))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone3=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone3.place(x=178,y=14)
    icone3text=Label(master, text='3')
    icone3.bind('<Button-1>',lambda event:choisir_pokemon(3))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone4=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone4.place(x=14,y=94)
    icone4text=Label(master, text='4')
    icone4.bind('<Button-1>',lambda event:choisir_pokemon(4))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone5=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone5.place(x=96,y=94)
    icone5text=Label(master, text='5')
    icone5.bind('<Button-1>',lambda event:choisir_pokemon(5))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone6=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone6.place(x=178,y=94)
    icone6text=Label(master, text='6')
    icone6.bind('<Button-1>',lambda event:choisir_pokemon(6))
    
    
        
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
                
                
                xmaster=master.winfo_x()
                ymaster=master.winfo_y()
                master.destroy()
                creation_equipe('equipe',equipechoisie,xmaster,ymaster)
        
    def inclure_pokemon():
        
        global numero_membre_choisi
        
        if numero_membre_choisi == 0:
            
            tkinter.messagebox.showinfo(title='Action Impossible', message="Vous n'avez aucun Slot sélectionné!",)
            
        else:
            
            file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','r')
            
            if file.read() != '':
                
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
                    creation_equipe('equipe',equipechoisie,xmaster,ymaster)
                    
            else:
            
                remplacer = tkinter.messagebox.askquestion(title='Inclure le Pokémon', message=("Voulez vous inclure "+str(nom_du_pokemon.get())+" dans le Slot "+str(numero_membre_choisi)+"?"),)
                
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
                    creation_equipe('equipe',equipechoisie,xmaster,ymaster)
            
    def pokemon_suivant():
        
        if get_num(nom_du_pokemon.get()) < 386:
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
                
    def titre():
        if str(equipe[int(numero_membre_choisi)-1]) == '':
            master.title("Gestion de l'équipe "+str(equipechoisie)+" (Aucun Pokémon selectionné) Slot: "+str(numero_membre_choisi))
        else:
            master.title("Gestion de l'équipe "+str(equipechoisie)+" ("+str(equipe[int(numero_membre_choisi)-1]).replace('1','')+") Slot: "+str(numero_membre_choisi))
            
            
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
        
        effacermsg = tkinter.messagebox.askquestion(title='Attention!', message="Voulez-vous vraiment effacer l'équipe?")
        
        if effacermsg == 'yes':
            
            for i in range(6):
                
                file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt','w')
                file.write('')
                file.close
                
            xmaster=master.winfo_x()
            ymaster=master.winfo_y()
            master.destroy()
            creation_equipe('equipe',equipechoisie,xmaster,ymaster)
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
    
    path = ('images/fonds/effacerlequipe.png')
    effacerimg = ImageTk.PhotoImage(Image.open(path))
    effacer=Label(master,image=effacerimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    effacer.place(x=4,y=374)
    effacer.photo=effacerimg
    effacer.bind('<Button-1>',lambda event:effacer_equipe())
    

    #fonctions du début
    
    afficher_equipe()
    
    master.mainloop()
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image
from liste_pokemon import listenompokemon
from liste_pokemon import *
from threading import Thread
import winsound
import random

def fenetre_equipe(master,equipechoisie,nom):
    
    equipe=[]

    for i in range(6):
        file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt')
        equipe.append(file.read())
        file.close
    
    master=tk.Toplevel()
    master.geometry('500x450+1074+50')
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
        creation_equipe('equipe',equipechoisie,xmaster,ymaster)
        
    
    gererimg = Image.open('images/fonds/gererlequipe.png')
    gererimg = ImageTk.PhotoImage(gererimg)
    gerer=Label(master, image=gererimg ,bg='#f8b0a0',borderwidth=0, highlightthickness=0)
    gerer.config(image=gererimg)
    gerer.im=gererimg
    gerer.place(x=10,y=424)
    gerer.bind('<Button-1>',lambda event:voir_vers_gerer())
                
    
            
    afficher_equipe()
    master.mainloop()
    
    
    
def choix_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")
    master.geometry('224x232+800+50')
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
    
    
    master.mainloop()
    
def choix_creation_equipe(master):
    
    master=tk.Toplevel()
    master.title("Choix de l'équipe")
    master.geometry('224x232+800+342')
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
        creation_equipe('equipe',equipe,50,600)

    master.mainloop()
    
numero_membre_choisi=0
    
frameicone=1
    
def creation_equipe(master,equipechoisie,x,y):
    
    
    
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
    
    path = ('images/fonds/etiquetteequipe'+str(equipechoisie)+'.png')
    etiquetteequipeimg = ImageTk.PhotoImage(Image.open(path))
    etiquetteequipe=Label(master,image=etiquetteequipeimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    etiquetteequipe.place(x=398,y=4)
    etiquetteequipe.photo=etiquetteequipeimg
           
    
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
      
                path = ('images/font3g/'+numpkmn[i]+'.png')
                img = ImageTk.PhotoImage(Image.open(path))
                        
                listelabelnum[i].configure(image=img)
                listelabelnum[i].im=img
                
    def affichage():
        
        lettre_num()
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
        
        pokemon.config(image=imgpokemon)
        pokemon.im=imgpokemon

        pokemon.bind("<Button-1>", lambda event:cri_pokemon())



    def combobox_nom(event):
        
#___________________________________________________________________________________        


        afficher_pokemon()
        chromatique()
        affichage()
        iconef()
        
        
#___________________________________________________________________________________
          
    def choisir_pokemon(num):
                
        global numero_membre_choisi
                
        if equipe[num-1]!='':
                
            if (equipe[num-1])[-1] == '1':
                isshiny.set(1)
            else:
                isshiny.set(0)
                        
            numero_membre_choisi=num
            nom_du_pokemon.set(str(equipe[(int(numero_membre_choisi)-1)]).replace('1',''))
            combobox_nom('e')
            titre()
            chromatique()
                        
        else:
                    
            nom_du_pokemon.set('Bulbizarre')
            numero_membre_choisi=(num)
            titre()
            chromatique()      
    
    #ICONES
        
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone1=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone1.place(x=14,y=14)
    icone1text=Label(master, text='1')
    icone1.bind('<Button-1>',lambda event:choisir_pokemon(1))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone2=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone2.place(x=96,y=14)
    icone2text=Label(master, text='2')
    icone2.bind('<Button-1>',lambda event:choisir_pokemon(2))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone3=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone3.place(x=178,y=14)
    icone3text=Label(master, text='3')
    icone3.bind('<Button-1>',lambda event:choisir_pokemon(3))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone4=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone4.place(x=14,y=94)
    icone4text=Label(master, text='4')
    icone4.bind('<Button-1>',lambda event:choisir_pokemon(4))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone5=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone5.place(x=96,y=94)
    icone5text=Label(master, text='5')
    icone5.bind('<Button-1>',lambda event:choisir_pokemon(5))
    
    path=PhotoImage(file='images/sprites3g/icones/empty.png')
    icone6=Label(master, image=path, borderwidth=0, highlightthickness=0, bg='#f8b0a0')
    icone6.place(x=178,y=94)
    icone6text=Label(master, text='6')
    icone6.bind('<Button-1>',lambda event:choisir_pokemon(6))
    
    
        
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
                
                
                xmaster=master.winfo_x()
                ymaster=master.winfo_y()
                master.destroy()
                creation_equipe('equipe',equipechoisie,xmaster,ymaster)
        
        
    def iconef():
        frames=0
        global frameicone
        while frames == 8:
            if frameicone==1:
                icone_membre(icone1,equipe[0],2)
                root.after(500)
                frameicone=2
            else:
                icone_membre(icone1,equipe[0],1)
                root.after(500)
                frameicone=1
            frames+=1
            print(frames)
            
    def inclure_pokemon():
        
        global numero_membre_choisi
        
        if numero_membre_choisi == 0:
            
            tkinter.messagebox.showinfo(title='Action Impossible', message="Vous n'avez aucun Slot sélectionné!",)
            
        else:
            
            file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(numero_membre_choisi)+'.txt','r')
            
            if file.read() != '':
                
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
                    creation_equipe('equipe',equipechoisie,xmaster,ymaster)
                    
            else:
            
                remplacer = tkinter.messagebox.askquestion(title='Inclure le Pokémon', message=("Voulez vous inclure "+str(nom_du_pokemon.get())+" dans le Slot "+str(numero_membre_choisi)+"?"),)
                
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
                    creation_equipe('equipe',equipechoisie,xmaster,ymaster)
            
    def pokemon_suivant():
        
        if get_num(nom_du_pokemon.get()) < 386:
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
                
    def titre():
        if str(equipe[int(numero_membre_choisi)-1]) == '':
            master.title("Gestion de l'équipe "+str(equipechoisie)+" (Aucun Pokémon selectionné) Slot: "+str(numero_membre_choisi))
        else:
            master.title("Gestion de l'équipe "+str(equipechoisie)+" ("+str(equipe[int(numero_membre_choisi)-1]).replace('1','')+") Slot: "+str(numero_membre_choisi))
            
            
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
        
        effacermsg = tkinter.messagebox.askquestion(title='Attention!', message="Voulez-vous vraiment effacer l'équipe?")
        
        if effacermsg == 'yes':
            
            for i in range(6):
                
                file=open('txts/equipe'+str(equipechoisie)+'/membre'+str(i+1)+'.txt','w')
                file.write('')
                file.close
                
            xmaster=master.winfo_x()
            ymaster=master.winfo_y()
            master.destroy()
            creation_equipe('equipe',equipechoisie,xmaster,ymaster)
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
    
    path = ('images/fonds/effacerlequipe.png')
    effacerimg = ImageTk.PhotoImage(Image.open(path))
    effacer=Label(master,image=effacerimg,borderwidth=0, highlightthickness=0,bg='#f8b0a0')
    effacer.place(x=4,y=374)
    effacer.photo=effacerimg
    effacer.bind('<Button-1>',lambda event:effacer_equipe())
    

    #fonctions du début
    
    afficher_equipe()
    
    master.mainloop()
    
creation_equipe('equipe',7,500,500)