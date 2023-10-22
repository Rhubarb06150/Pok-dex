import tkinter as tk, threading
from tkinter import *
from tkinter import messagebox
from fenetrecontroles import *
from listepokemon import *
from pokedex2proto import *
from pokedex2proto import listenompokemon,listepokemon
from PIL import Image,ImageTk

       
def fenetre_recherche_stats():
        
    def demarrer_recherche():
        
        listepkmnaretirer=[]
        listepkmnrestant=listenompokemon
        
        rech=False
        
 
        #PV
        
        if varpvcompa.get() != '' and varpv != 0 and str(varpv) != '':
            rech=True
            if varpvcompa.get() == '>':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.pv > varpv.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
                                
            if varpvcompa.get() == '>=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.pv >= varpv.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varpvcompa.get() == '=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.pv == varpv.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varpvcompa.get() == '<=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.pv <= varpv.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varpvcompa.get() == '<':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.pv < varpv.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
                
        #FORCE    
            
        if varforcecompa.get() != '' and varforce != 0 and str(varforce) != '':
            rech=True
            if varforcecompa.get() == '>':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.force > varforce.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
                                
            if varforcecompa.get() == '>=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.force >= varforce.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varforcecompa.get() == '=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.force == varforce.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varforcecompa.get() == '<=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.force <= varforce.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varforcecompa.get() == '<':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.force < varforce.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
            
        #DEFENSE
            
        if vardefensecompa.get() != '' and vardefense != 0 and str(vardefense) != '':
            rech=True
            if vardefensecompa.get() == '>':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.defense > varvitesse.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
                                
            if vardefensecompa.get() == '>=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.defense >= vardefense.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if vardefensecompa.get() == '=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.defense == vardefense.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if vardefensecompa.get() == '<=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.defense <= vardefense.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if vardefensecompa.get() == '<':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.defense < vardefense.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
            
        #VITESSE
            
        if varvitessecompa.get() != '' and varvitesse != 0 and str(varvitesse) != '':
            rech=True
            if varvitessecompa.get() == '>':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.vitesse > varvitesse.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
                                
            if varvitessecompa.get() == '>=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.vitesse >= varvitesse.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varvitessecompa.get() == '=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.vitesse == vardvitesse.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varvitessecompa.get() == '<=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.vitesse <= vardvitesse.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varvitessecompa.get() == '<':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.vitesse < vardvitesse.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
        
        #SPÉCIAL
        
        if varspecialcompa.get() != '' and varspecial != 0 and str(varspecial) != '':
            rech=True
            if varspecialcompa.get() == '>':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.specialgen1 == 0:
                                listepkmnaretirer.append(i2.nom)
                            if i2.specialgen1 > varspecial.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
                                
            if varspecialcompa.get() == '>=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.specialgen1 == 0:
                                listepkmnaretirer.append(i2.nom)
                            if i2.specialgen1 >= varspecial.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varspecialcompa.get() == '=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.specialgen1 == 0:
                                listepkmnaretirer.append(i2.nom)
                            if i2.specialgen1 == varspecial.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varspecialcompa.get() == '<=':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.specialgen1 == 0:
                                listepkmnaretirer.append(i2.nom)
                            if i2.specialgen1 <= varspecial.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            if varspecialcompa.get() == '<':
                for i in listepkmnrestant:
                    for i2 in listepokemon:
                        if i == i2.nom:
                            if i2.specialgen1 == 0:
                                listepkmnaretirer.append(i2.nom)
                            if i2.specialgen1 < varspecial.get():
                                break
                            else:
                                listepkmnaretirer.append(i2.nom)
                                
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
            
        if vartype2.get() != '':
            rech=True
            for i in listepkmnrestant:
                for i2 in listepokemon:
                    if i == i2.nom:
                        if i2.type1 == vartype2.get() or i2.type2 == vartype2.get():
                            break
                        else:
                            listepkmnaretirer.append(i2.nom)
                            
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
            
        if vartype1.get() != '':
            rech=True
            for i in listepkmnrestant:
                for i2 in listepokemon:
                    if i == i2.nom:
                        if i2.type1 == vartype1.get() or i2.type2 == vartype1.get():
                            break
                        else:
                            listepkmnaretirer.append(i2.nom)
                            
            for retire in listepkmnaretirer:
                listepkmnrestant.remove(retire)
            listepkmnaretirer=[]
            
        
        if rech==True:
            nbres=0
            resultat=''
            if len(listepkmnrestant) == 0:
                messagebox.showwarning(title="Aucun résultat",message="Aucun Pokémon n'a été trouvé avec ces conditions!")
            else:
                for i in listepkmnrestant:
                    if nbres >= 1:
                        resultat+=', '
                    resultat += i
                    nbres+=1
                print()
                messagebox.showinfo(title="Résultat",message=resultat)
        else:
            messagebox.showwarning(title="Impossible",message="Veuillez renseigner au moins une condition!")
        
        listepkmnaretirer=[]
        listepkmnrestant=listenompokemon
                
    listecompa=['','>','>=','=','<=','<']

    master2 = tk.Toplevel()
    master2.title('Recherce avancée de Pokémon')

    icon=PhotoImage(file='images/icones/recherche.gif')
    master2.tk.call('wm','iconphoto',master2._w, icon)

    master2.geometry('400x600+300+570')
    bg=PhotoImage(file='images/fonds/fondrechercheavancee.png')
    background=Label(master2, image=bg)
    background.place(x=-2,y=-2)
    master2.resizable(False,False)
        
    #pv
        
    varpv = IntVar()
    varpv.set(0)
    varpvcompa=StringVar()

    pv = Spinbox(master2, from_=0, to=250,width=4,textvariable=varpv)
    pv.place(x=130,y=170)
    pvcompa = Spinbox(master2, values=listecompa, state='readonly',width=3,textvariable=varpvcompa)
    pvcompa.place(x=90,y=170)
    pvlb=Label(master2,text='PV:')
    pvlb.place(x=30,y=170)

    #force

    varforce = tk.IntVar()
    varforce.set(0)
    varforcecompa=StringVar()

    force = Spinbox(master2, from_=0, to=250,width=4,textvariable=varforce)
    force.place(x=130,y=200)
    forcecompa = Spinbox(master2, values=listecompa, state='readonly',width=3,textvariable=varforcecompa)
    forcecompa.place(x=90,y=200)
    forcelb=Label(master2,text='Force:')
    forcelb.place(x=30,y=200)
          
    #defense

    vardefense = tk.IntVar()
    vardefense.set(0)
    vardefensecompa=StringVar()

    defense = Spinbox(master2, from_=0, to=250,width=4,textvariable=vardefense)
    defense.place(x=130,y=230)
    defensecompa = Spinbox(master2, values=listecompa, state='readonly',width=3,textvariable=vardefensecompa)
    defensecompa.place(x=90,y=230)
    defenselb=Label(master2,text='Défense:')
    defenselb.place(x=30,y=230)

    #vitesse

    varvitesse = tk.IntVar()
    varvitesse.set(0)
    varvitessecompa=StringVar()

    vitesse = Spinbox(master2, from_=0, to=250,width=4,textvariable=varvitesse)
    vitesse.place(x=130,y=260)
    vitessecompa = Spinbox(master2, values=listecompa, state='readonly',width=3,textvariable=varvitessecompa)
    vitessecompa.place(x=90,y=260)
    vitesselb=Label(master2,text='Vitesse:')
    vitesselb.place(x=30,y=260)
            
    #spécial

    varspecial = tk.IntVar()
    varspecial.set(0)
    varspecialcompa=StringVar()

    special = Spinbox(master2, from_=0, to=250,width=4,textvariable=varspecial)
    special.place(x=130,y=290)
    specialcompa = Spinbox(master2, values=listecompa, state='readonly',width=3,textvariable=varspecialcompa)
    specialcompa.place(x=90,y=290)
    speciallb=Label(master2,text='Spécial:')
    speciallb.place(x=30,y=290)
    speciallb2=Label(master2,text="(N'inclut pas les Pokémons de Jotho)")
    speciallb2.place(x=170,y=290)
            
    #types
    
    vartype1=StringVar()
    listetypes=['','Acier','Dragon','Élektrik','Feu','Insecte','Plante','Psy','Sol','Ténèbres','Combat','Eau','Glace','Normal','Poison','Roche','Spectre','Vol']
    
    type1 = Spinbox(master2, from_=0, to=17,width=8,textvariable=vartype1, values=listetypes)
    type1.place(x=90,y=320)
    type1lb=Label(master2,text='Type:')
    type1lb.place(x=30,y=320)
    
    vartype2=StringVar()
    
    type2= Spinbox(master2, from_=0, to=17,width=8,textvariable=vartype2, values=listetypes)
    type2.place(x=90,y=350)
    type2lb=Label(master2,text='2nd type:')
    type2lb.place(x=30,y=350)
    
    #recherche

    recherche=Button(master2,text='Recherche',command=demarrer_recherche)
    recherche.place(x=200,y=470)

    master2.mainloop()