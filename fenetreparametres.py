import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

file=open('txts/maj.txt','r')
maj_active=int(file.read())
file.close

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
    
    def afficher_maj():
        global maj_check
        global maj_active
        
        file=open('txts/maj.txt','w')
        file.write(str(maj_check.get()))
        maj_active=maj_check.get()
        file.close
    
        if maj_check.get() == 0:
            messagebox.showinfo(title="Mise à jour",message="Vous ne receverez plus les informations sur les dernières mises à jours sorties")
    
    file=open('txts/maj.txt','r')
    maj_check.set(file.read())
    print(file.read())
    file.close
    
    maj_verif=tk.Checkbutton(parametres,text='Vérifier les mises à jour',variable=maj_check,onvalue=1,offvalue=0,command=afficher_maj)
    maj_verif.place(x=50,y=50)
    
    parametres.mainloop()