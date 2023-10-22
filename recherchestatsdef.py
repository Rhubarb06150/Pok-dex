import tkinter as tk, threading
from tkinter import *
from fenetrecontroles import *
from listepokemon import *
from pokedex2proto import *
from pokedex2proto import listenompokemon,listepokemon
    
    
listepkmn=[]
def rech_pv(pv,cond):
    global listepkmn
    listepkmn=[]
    if cond == 'plus_grand':
        for i in listenompokemon:
            for i2 in listepokemon:
                if i == i2.nom:
                    if i2.pv > pv:
                        listepkmn.append(i2.nom)
    print(listepkmn)
            


def demarrer_recherche():
    global listepkmn
    if pv.get() > 0:
        rech_pv(pv.get,'plus_grand')
    print(listepkmn)