import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pokedex2proto import listenompokemon

listenompokemon2=['Aucun']
for i in listenompokemon:
    listenompokemon2.append(i)

listeversion2=['Aucune','Or','Argent']

file=open('txts/maj.txt','r')
maj_active=int(file.read())
file.close

file=open('txts/pkmn.txt','r')
pkmn_pref=(file.read())
file.close

file=open('txts/vers.txt','r')
vers=(file.read())
file.close

def fenetre_parametres():
    
    
    def callback(recherche):
        x = parametres.winfo_pointerx() - parametres.winfo_rootx()
        y = parametres.winfo_pointery() - parametres.winfo_rooty()
        print(x)
        print(y)
        if y > 74 or y < 125 or x < 75 or x > 151:
            parametres.focus()
    
    parametres = tk.Toplevel()
    parametres.title('Paramètres')
    parametres.iconbitmap('images/icones/icone.ico')
    parametres.geometry('400x300+340+570')
    parametres.resizable(False,False)
    bg=PhotoImage(file='images/fonds/fondparametres.png')
    
    bg2=Label(parametres, image=bg)
    bg2.place(x=-2,y=-2)
    
    global maj_check
    maj_check=tk.IntVar()
    
    def afficher_maj():
        global maj_check
        global maj_active
        
        file=open('txts/maj.txt','w')
        file.write(str(maj_check.get()))
        maj_active=maj_check.get()
        file.close
    
        if maj_check.get() == 0:
            messagebox.showinfo(title="Mise à jour",message="Vous ne receverez plus les informations sur les dernières mises à jours sorties")
    
    def pkmn_prefere(event):
        global pkmn_pref
        
        file=open('txts/pkmn.txt','w')
        file.write(str(pokemon_favori.get()))
        pkmn_pref=pokemon_favori.get()
        file.close
        
    def vers_prefere(event):
        global vers
        
        file=open('txts/vers.txt','w')
        file.write(str(version_favorite.get()))
        vers=version_favorite.get()
        file.close
    
    file=open('txts/maj.txt','r')
    maj_check.set(file.read())
    print(file.read())
    file.close
    
    
    
    maj_verif=tk.Checkbutton(parametres,text='Vérifier les mises à jour',variable=maj_check,onvalue=1,offvalue=0,command=afficher_maj)
    maj_verif.place(x=50,y=50)
    
    pokemon_favori=ttk.Combobox(parametres, values=listenompokemon2, state='readonly',width=13)
    pokemon_favori_label=Label(parametres, text='Pokémon Favori:')
    
    version_favorite=ttk.Combobox(parametres, values=listeversion2, state='readonly',width=13)
    version_favorite_label=Label(parametres, text='Version Favorite:')
    
    pokemon_favori_label.place(x=50,y=75)
    pokemon_favori.place(x=150,y=75)
    version_favorite_label.place(x=50,y=100)
    version_favorite.place(x=150,y=100)
    
    pokemon_favori.bind("<<ComboboxSelected>>", pkmn_prefere)
    
    file=open('txts/pkmn.txt','r')
    pokemon_favori.set(file.read())
    print(file.read())
    file.close
    
    version_favorite.bind("<<ComboboxSelected>>", vers_prefere)
    
    file=open('txts/vers.txt','r')
    version_favorite.set(file.read())
    print(file.read())
    file.close
    
    
    parametres.bind('<Button-1>',lambda event:callback(parametres))
    
    parametres.mainloop()