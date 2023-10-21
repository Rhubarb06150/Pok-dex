import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def afficher_maj():
    global maj_check
    if maj_check.get() == 0:
        messagebox.showinfo(title="Mise à jour",message="Vous ne receverez plus les informations sur les dernières mises à jours sorties")
        

def fenetre_parametres():
    
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
    maj_verif=tk.Checkbutton(parametres,text='Vérifier les mises à jour',variable=maj_check,onvalue=1,offvalue=0,command=afficher_maj)
    maj_verif.place(x=50,y=50)
    
    parametres.mainloop()