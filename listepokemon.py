import tkinter as tk, threading
from tkinter import *
fenetrelistepokemon = None

def page_1_from_2():#2 ----> 1

    fenetre_listepokemon(fenetrelistepokemon)
    
def page_2_from_1():#1 ----> 2

    fenetre_listepokemon2(fenetrelistepokemon)
    
def ouvrir():
    global fenetrelistepokemon
    fenetrelistepokemon = tk.Toplevel()
    fenetre_listepokemon(fenetrelistepokemon)
    nomlistepokemon = fenetrelistepokemon

def fenetre_listepokemon(master):
    
    master.title('Liste des Pokémon (Page 1)')
    master.iconbitmap('images/icones/icone.ico')
    master.geometry('700x400+740+20')
    master.resizable(False,False)
    
    bg=PhotoImage(file='images/fonds/fondlistepokemon.png')
    fond=Label(master, image=bg)
    fond.place(x=-2,y=-2)
    
    
    pokemon1=Label(master,text='Bublizarre')
    pokemon1.place(x=70,y=25)
    pokemon2=Label(master,text='Herbizarre')
    pokemon2.place(x=70,y=75)
    pokemon3=Label(master,text='Florizarre')
    pokemon3.place(x=70,y=125)
    
    pokemon4=Label(master,text='Salamèche')
    pokemon4.place(x=70,y=165)
    pokemon5=Label(master,text='Reptincel')
    pokemon5.place(x=70,y=205)
    pokemon6=Label(master,text='Dracaufeu')
    pokemon6.place(x=70,y=255)
    
    pokemon7=Label(master,text='Carapuce')
    pokemon7.place(x=70,y=295)
    pokemon8=Label(master,text='Carabaffe')
    pokemon8.place(x=70,y=345)
    pokemon9=Label(master,text='Tortank')
    pokemon9.place(x=70,y=385)
    
    page2=Button(master,text='>>>', command = page_2_from_1)
    page2.place(x=653,y=360)
    
    master.bind('<Left>',lambda event:None)
    master.bind('<Right>',lambda event:page_2_from_1())
    
    master.mainloop()

def fenetre_listepokemon2(master):
    
    master.title('Liste des Pokémon (Page 2)')
    master.iconbitmap('images/icones/icone.ico')
    master.geometry('700x400+740+20')
    master.resizable(False,False)
    
    bg=PhotoImage(file='images/fonds/fondlistepokemon2.png')
    fond=Label(master, image=bg)
    fond.place(x=-2,y=-2)
    
    
    pokemon1=Label(master,text='Grodoudou')
    pokemon1.place(x=70,y=25)
    pokemon2=Label(master,text='Nosferapti')
    pokemon2.place(x=70,y=75)
    pokemon3=Label(master,text='Nosferalto')
    pokemon3.place(x=70,y=125)
    
    pokemon4=Label(master,text='Mystherbe')
    pokemon4.place(x=70,y=165)
    pokemon5=Label(master,text='Ortide')
    pokemon5.place(x=70,y=205)
    pokemon6=Label(master,text='Raflésia')
    pokemon6.place(x=70,y=255)
    
    pokemon7=Label(master,text='Paras')
    pokemon7.place(x=70,y=295)
    pokemon8=Label(master,text='Parasect')
    pokemon8.place(x=70,y=345)
    
    
    
    page3=Button(master,text='>>>')
    page3.place(x=642,y=360)
    page2=Button(master,text='<<<', command = page_1_from_2)
    page2.place(x=20,y=360)
    
    master.bind('<Left>',lambda event:page_1_from_2())
    master.bind('<Right>',lambda event:pk_suivant())
    
    master.mainloop()
    
    