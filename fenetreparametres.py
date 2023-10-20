import tkinter as tk, threading
from tkinter import *

def fenetre_parametres():
    
    parametres = tk.Toplevel()
    parametres.title('Paramètres')
    parametres.iconbitmap('images/icones/icone.ico')
    parametres.geometry('400x300+50+50')
    parametres.resizable(False,False)
    bg=PhotoImage(file='images/fonds/fondparametres.png')
    
    bg2=Label(parametres, image=bg)
    bg2.place(x=-2,y=-2)
    
    parametres.mainloop()