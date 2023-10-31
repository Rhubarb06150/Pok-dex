#Pokédex 2 proto
#4/10/23
#Rhubarb

import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk, Tk, Frame, Canvas
from PIL import ImageTk, Image

#classes
class Pokemon:
    def __init__(self,num,rawnom,nom,pv,force,defense,vitesse,specialgen1,attaquespeciale,defensespeciale,pre_evolution,evolution,condition_evolution,type1,type2,pasoeuf,male,femelle,taux_capture,faiblesses,dbfaiblesses,resistances,dbresistances,immunites):
        self.num=num
        self.rawnom=rawnom
        self.nom=nom
        self.pv=pv
        self.force=force
        self.defense=defense
        self.vitesse=vitesse
        self.specialgen1=specialgen1
        self.attaquespeciale=attaquespeciale
        self.defensespeciale=defensespeciale
        self.pre_evolution=pre_evolution
        self.evolution=evolution
        self.condition_evolution=condition_evolution
        self.type1=type1
        self.type2=type2
        self.pasoeuf=pasoeuf
        self.male=male
        self.femelle=femelle
        self.taux_capture=taux_capture
        self.faiblesses=faiblesses
        self.dbfaiblesses=dbfaiblesses
        self.resistances=resistances
        self.dbresistances=dbresistances
        self.immunites=immunites

def loc():
    localisation = input('Quelle localisation? ')
    print()
    if generation == 1:
        print('Pokémon Bleu:')
        print()
        for i in range(len(listepokemon)):
            for i2 in range(len(listepokemon[i].zonegen1bleu)):
                if listepokemon[i].zonegen1bleu[i2] == localisation:
                    print(listepokemon[i].nom)
        print()
        print('Pokémon Rouge:')
        print()
        for i in range(len(listepokemon)):
            for i2 in range(len(listepokemon[i].zonegen1rouge)):
                if listepokemon[i].zonegen1rouge[i2] == localisation:
                    print(listepokemon[i].nom)
        print()
        print('Pokémon Jaune:')
        print()
        for i in range(len(listepokemon)):
            for i2 in range(len(listepokemon[i].zonegen1jaune)):
                if listepokemon[i].zonegen1jaune[i2] == localisation:
                    print(listepokemon[i].nom)
    else:
        print('Pokémon Or:')
        print()

        for i in range(len(listepokemon)):
            for i2 in range(len(listepokemon[i].zonegen2or)):
                if listepokemon[i].zonegen2or[i2] == localisation:
                    print(listepokemon[i].nom)
        print()
        print('Pokémon Argent:')
        print()
        for i3 in range(len(listepokemon[i].zonegen2argent)):
            if listepokemon[i].zonegen2argent[i3] == localisation:
                print(listepokemon[i].nom)
        print()
        print('Pokémon Cristal:')
        print()
        for i3 in range(len(listepokemon[i].zonegen2cristal)):
            if listepokemon[i].zonegen2cristal[i3] == localisation:
                print(listepokemon[i].nom)
        
def get_nom(num):
    for i in range(len(listepokemon)):
        if listepokemon[i].num == num:
            return listepokemon[i].nom
        
def get_num(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].num

def get_types(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            if listepokemon[i].type2==False:
                return ('Type: '+listepokemon[i].type1)
            else:
                return ('Types: '+listepokemon[i].type1+' et '+listepokemon[i].type2)
    
def get_pv(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].pv
        
def get_force(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].force
        
def get_defense(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].defense
        
def get_vitesse(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].vitesse
        
def get_specialgen1(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].specialgen1

def get_pre_evo(nom):
    for i in listepokemon:
        if i.nom == nom:
            if i.pre_evolution != False:
                return (i.pre_evolution)
            if i.pre_evolution2 != False:
                return (i.pre_evolution2)
            if i.pre_evolution == False and i.pre_evolution2 == False:
                return 'Aucune pré-évolution'
        
def get_evo(nom):
    nbevolutions=0
    evolutions=[]
    for i in range(len(listepokemon)):
        
        if listepokemon[i].nom == nom:
            
            if listepokemon[i].evolution != False:
                for i2 in range(len(listepokemon[i].evolution)):
                    evolutions.append(listepokemon[i].evolution[i2])
    return evolutions
            
def get_evo_nb(nom):
    nbevolutions=0
    for i in listepokemon:
        if i.nom == nom:
            if i.evolution!=False:
                for i2 in i.evolution:
                    nbevolutions+=1
            if i.evolution2!=False:
                for i2 in i.evolution2:
                    nbevolutions+=1
    return nbevolutions
            
def get_specialgen1(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].specialgen1
        
def get_attspec(nom):
    for i in listepokemon:
        if i.nom == nom:
            return i.attaquespeciale
            
def get_defspec(nom):
    for i in listepokemon:
        if i.nom == nom:
            return i.defensespeciale
        
def get_male(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].male
        
def get_femelle(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].femelle

class Attaque:
    def __init__(self,nom,typeattaque,puissance,precision,ppmax,effetsecondaires):
        self.nom=nom
        self.typeattaque=typeattaque
        self.puissance=puissance
        self.precision=precision
        self.ppmax=ppmax
        self.effetsecondaires=effetsecondaires
        
        
listeattaque=[]

listeattaque.append(Attaque('Griffe Acier','Physique',50,95,35,False))
        
def get_type1(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].type1
        
def get_type2(nom):
    for i in range(len(listepokemon)):
        if listepokemon[i].nom == nom:
            return listepokemon[i].type2
        
def get_faiblesses(nom):
    
    
    if get_type2(nom) == False:
        
        
        if get_type1(nom) == 'Normal':
            
            return ['Combat']
        
        elif get_type1(nom) == 'Feu':
            
            return ['Eau','Sol','Roche'] 
        
        elif get_type1(nom) == 'Eau':
            
            return ['Plante','Électrik']
        
        elif get_type1(nom) == 'Plante':
            
            return ['Feu','Glace','Poison','Vol','Insecte']
        
        elif get_type1(nom) == 'Électrik':
            
            return ['Sol']
        
        elif get_type1(nom) == 'Glace':
            
            return ['Feu','Combat','Roche','Acier']
        
        elif get_type1(nom) == 'Combat':
            
            return ['Vol','Psy']
        
        elif get_type1(nom) == 'Poison':
            
            return ['Sol','Psy']
        
        elif get_type1(nom) == 'Sol':
            
            return ['Eau','Plante','Glace']
        
        elif get_type1(nom) == 'Vol':
            
            return ['Électrik','Glace','Roche']
        
        elif get_type1(nom) == 'Psy':
            
            return ['Insecte','Spectre','Ténèbres']
        
        elif get_type1(nom) == 'Insecte':
            
            return ['Feu','Vol','Roche']
        
        elif get_type1(nom) == 'Roche':
            
            return ['Eau','Plante','Combat','Sol','Acier']
        
        elif get_type1(nom) == 'Spectre':
            
            return ['Spectre','Ténèbres']
        
        elif get_type1(nom) == 'Dragon':
            
            return ['Glace','Dragon']
        
        elif get_type1(nom) == 'Ténèbres':
            
            return ['Combat','Insecte']
        
        elif get_type1(nom) == 'Acier':
            
            return ['Feu','Combat','Sol']
        
        
    else:
        
        if get_type1(nom) == 'Feu':
            if get_type2(nom) == 'Vol':
                return ['Eau','Électrik']
            
        if get_type1(nom) == 'Eau':
            if get_type2(nom) == 'Glace':
                return ['Plante','Électrik','Combat','Roche']
            elif get_type2(nom) == 'Vol':
                return ['Roche']
                
                
            
    
#listage des pokémons

#FAIBLESSES____________

#FEU FALSE
#['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))

#FEU VOL
#['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))

#PLANTE FALSE
#['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],['Plante'],False))

#EAU FALSE
#['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
    
listepokemon=[]

    #KANTO

listepokemon.append(Pokemon(1,['bulbizarre','bublizarre','Bublizarre','bublizzare','bublizzarre','Bublizzare','Bublizzarre'],'Bulbizarre',45,49,49,45,65,65,65,False,['Herbizarre'],[16],'Plante','Poison',5100,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],False,False))
listepokemon.append(Pokemon(2,['herbizarre','herbizzare','herbizzarre','Herbizzare','Herbizzarre'],'Herbizarre',60,62,63,60,80,80,80,'Bulbizarre',['Florizarre'],[32],'Plante','Poison',5100,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],False,False))
listepokemon.append(Pokemon(3,['florizarre','florizzare','florizzarre','Florizzare','Florizzarre'],'Florizarre',80,82,83,80,100,100,100,'Herbizarre',False,False,'Plante','Poison',5100,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],False,False))

listepokemon.append(Pokemon(4,['salameche','salamèche','Salameche'],'Salamèche',39,52,43,65,50,60,50,False,['Reptincel'],[16],'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(5,['reptincel','Reptincel'],'Reptincel',58,64,58,80,80,80,65,'Salamèche',['Dracaufeu'],[36],'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(6,['dracaufeu'],'Dracaufeu',78,84,78,100,85,80,65,'Reptincel',False,False,'Feu','Vol',5100,87,13,45,['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))

listepokemon.append(Pokemon(7,['carapuce'],'Carapuce',44,48,65,43,50,50,65,False,['Carabaffe'],[16],'Eau',False,5100,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(8,['carabaffe'],'Carabaffe',59,63,80,58,65,65,80,'Carapuce',['Tortank'],[36],'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(9,['tortank'],'Tortank',79,83,100,78,85,105,85,'Carabaffe',False,False,'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))

listepokemon.append(Pokemon(10,['chenipan'],'Chenipan',45,30,35,45,20,20,20,False,['Chrysacier'],[7],'Insecte',False,3825,50,50,255,['Feu','Roche','Vol'],False,['Combat','Plante','Sol'],False,False))
listepokemon.append(Pokemon(11,['chrysacier'],'Chrysacier',50,20,55,30,25,25,25,'Chenipan',['Papillusion'],[10],'Insecte',False,3825,50,50,120,['Feu','Roche','Vol'],False,['Combat','Plante','Sol'],False,False))
listepokemon.append(Pokemon(12,['papillusion'],'Papillusion',60,45,50,75,80,90,80,'Chrysacier',False,False,'Insecte','Vol',3825,50,50,45,['Électrik','Feu','Glace','Vol'],['Roche'],['Insecte'],['Combat','Plante'],['Sol']))

listepokemon.append(Pokemon(13,['aspicot'],'Aspicot',40,35,30,50,20,20,20,False,['Coconfort'],[7],'Insecte','Poison',3825,50,50,255,['Feu','Psy','Roche','Vol'],False,['Insecte','Poison'],['Combat','Plante'],False))
listepokemon.append(Pokemon(14,['coconfort'],'Coconfort',45,25,50,35,25,25,25,'Aspicot',['Dardagnan'],[10],'Insecte','Poison',3825,50,50,255,['Feu','Psy','Roche','Vol'],False,['Insecte','Poison'],['Combat','Plante'],False))
listepokemon.append(Pokemon(15,['dardagnan'],'Dardagnan',65,80,40,75,45,80,45,'Coconfort',False,False,'Insecte','Poison',3825,50,50,255,['Feu','Psy','Roche','Vol'],False,['Insecte','Poison'],['Combat','Plante'],False))

listepokemon.append(Pokemon(16,['roucoul','roucool','Roucoul'],'Roucool',40,45,40,56,35,35,35,False,['Roucoups'],[18],'Normal','Vol',3825,50,50,255,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(17,['roucoups'],'Roucoups',63,60,55,71,50,50,50,'Roucool',['Roucarnage'],[36],'Normal','Vol',3825,50,50,120,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(18,['roucarnage'],'Roucarnage',83,80,75,91,70,70,70,'Roucoups',False,False,'Normal','Vol',3825,50,50,45,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))

listepokemon.append(Pokemon(19,['ratata','rattata'],'Rattata',30,56,35,72,25,25,35,False,['Rattatac'],[20],'Normal',False,3825,50,50,255,['Combat'],False,False,False,['Spectre']))
listepokemon.append(Pokemon(20,['rattatac'],'Rattatac',55,81,60,97,50,50,70,'Rattata',False,False,'Normal',False,3825,50,50,255,['Combat'],False,False,False,['Spectre']))

listepokemon.append(Pokemon(21,['piafabec'],'Piafabec',40,60,30,70,31,31,31,False,['Rapasdepic'],[20],'Normal','Vol',3825,50,50,255,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(22,['rapasdepic'],'Rapasdepic',65,90,65,61,61,61,100,'Piafabec',False,False,'Normal','Vol',3825,50,50,255,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))

listepokemon.append(Pokemon(23,['abo'],'Abo',35,60,44,55,40,40,54,False,['Arbok'],[22],'Poison',False,3825,50,50,255,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(24,['arbok'],'Arbok',60,95,69,80,65,65,79,'Abo',False,False,'Poison',False,3825,50,50,90,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))

listepokemon.append(Pokemon(25,['pikachu'],'Pikachu',35,55,40,90,50,50,50,'Pichu',['Raichu'],['Utiliser une Pierre Foudre'],'Électrik',False,2295,50,50,190,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(26,['raichu'],'Raichu',60,90,55,110,90,90,80,'Pikachu',False,False,'Électrik',False,2295,50,50,75,['Sol'],False,['Acier','Électrik','Vol'],False,False))

listepokemon.append(Pokemon(27,['sabelette'],'Sabelette',50,75,85,40,30,20,30,False,['Sablaireau'],[22],'Sol',False,5100,50,50,255,['Eau','Glace','Plante'],False,['Poison','Roche'],False,['Électrik']))
listepokemon.append(Pokemon(28,['sablaireau'],'Sablaireau',75,100,110,65,55,45,55,'Sabelette',False,False,'Sol',False,5100,50,50,900,['Eau','Glace','Plante'],False,['Poison','Roche'],False,['Électrik']))

listepokemon.append(Pokemon(29,['nidoran F','Nidoran F','nidoran f'],'Nidoran F',55,47,52,41,40,40,40,False,['Nidorina'],[16],'Poison',False,5100,0,100,235,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(30,['nidorina'],'Nidorina',70,62,67,56,55,55,55,'Nidoran F',['Nidoqueen'],['Utiliser une Pierre Lune'],'Poison',False,5100,0,100,120,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(31,['nidoqueen'],'Nidoqueen',90,92,87,76,75,75,85,'Nidorina',False,False,'Poison','Sol',5100,0,100,45,['Eau','Glace','Sol','Psy'],False,['Combat','Insecte','Roche'],['Poison'],['Électrik']))

listepokemon.append(Pokemon(32,['nidoran M','nidoran m','Nidoran M'],'Nidoran M',46,57,40,50,40,40,40,False,['Nidorino'],[16],'Poison',False,5100,100,0,235,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(33,['nidorino'],'Nidorino',61,72,57,65,55,55,55,'Nidoran M',['Nidoking'],['Utiliser une Pierre Lune'],'Poison',False,5100,100,0,120,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(34,['nidoking'],'Nidoking',81,102,77,85,75,85,75,'Nidorino',False,False,'Poison','Sol',5100,100,0,45,['Eau','Glace','Sol','Psy'],False,['Combat','Insecte','Roche'],['Poison'],['Électrik']))

listepokemon.append(Pokemon(35,['mélofée','melofee','Mélofée','Melofee',],'Mélofée',70,45,48,35,60,60,65,'Mélo',['Mélodelefe'],['Utiliser une Pierre Lune'],'Normal',False,2560,25,75,150,['Combat'],False,False,False,['Spectre']))
listepokemon.append(Pokemon(36,['mélodelfe','mélodelfe'],'Mélodelfe',95,90,73,60,85,90,85,'Mélofée',False,False,'Normal',False,2560,25,75,25,['Combat'],False,False,False,['Spectre']))

listepokemon.append(Pokemon(37,['goupix'],'Goupix',38,41,40,65,65,50,65,False,['Feunard'],['Utiliser une Pierre Feu'],'Feu',False,5100,25,75,190,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(38,['feunard'],'Feunard',373,76,75,100,100,81,100,'Goupix',False,False,'Feu',False,5100,25,75,75,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))

listepokemon.append(Pokemon(39,['rondoudou'],'Rondoudou',115,45,20,20,25,45,25,'Toudoudou','Grodoudou',['Utiliser une Pierre Lune'],'Normal',False,2560,25,75,170,['Combat'],False,False,False,['Spectre']))

listepokemon.append(Pokemon(63,['abra'],'Abra',25,20,15,90,105,105,55,False,['Kadabra'],[16],'Psy',False,5120,75,25,200,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))
listepokemon.append(Pokemon(64,['kadabra'],'Kadabra',40,35,30,105,120,120,70,'Abra',['Alakazam'],['Échange'],'Psy',False,5120,75,25,100,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))
listepokemon.append(Pokemon(65,['alakazam'],'Alakazam',55,50,45,120,135,135,85,'Kadabra',False,False,'Psy',False,5120,75,25,50,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))

listepokemon.append(Pokemon(92,['fantominus'],'Fantominus',30,35,30,80,100,100,35,False,['Spectrum'],[25],'Spectre','Poison',5120,50,50,190,['Sol','Psy','Spectre','Ténèbres'],False,['Plante'],['Poison','Insecte'],['Normal','Combat']))
listepokemon.append(Pokemon(93,['spectrum'],'Spectrum',45,50,45,95,115,115,55,'Fantominus',['Ectoplasma'],['Échange'],'Spectre','Poison',5120,50,50,90,['Sol','Psy','Spectre','Ténèbres'],False,['Plante'],['Poison','Insecte'],['Normal','Combat']))
listepokemon.append(Pokemon(94,['ectoplasma'],'Ectoplasma',60,65,60,110,130,130,75,'Spectrum',False,False,'Spectre','Poison',5120,50,50,45,['Sol','Psy','Spectre','Ténèbres'],False,['Plante'],['Poison','Insecte'],['Normal','Combat']))

listepokemon.append(Pokemon(102,['noeunoeuf'],'Noeunoeuf',60,40,80,40,60,60,45,False,['Noadkoko'],['Utiliser une Pierre Plante'],'Plante','Psy',5120,50,50,90,['Feu','Glace','Poison','Vol','Spectre','Ténèbres'],['Insecte'],['Plante','Eau','Électrik','Combat','Sol','Psy'],False,False))
listepokemon.append(Pokemon(103,['noadkoko'],'Noadkoko',95,95,85,55,125,125,65,'Noeunoeuf',False,False,'Plante','Psy',5120,50,50,45,['Feu','Glace','Poison','Vol','Spectre','Ténèbres'],['Insecte'],['Plante','Eau','Électrik','Combat','Sol','Psy'],False,False))

listepokemon.append(Pokemon(128,['tauros'],'Tauros',75,100,95,110,70,40,70,False,False,False,'Normal',False,5120,100,0,45,['Combat'],False,False,False,['Spectre']))

listepokemon.append(Pokemon(127,['scarabrute'],'Scarabrute',65,125,100,85,55,55,70,False,False,False,'Insecte',False,6400,50,50,45,['Feu','Vol','Roche',],False,['Plante','Combat','Sol'],False,False))

listepokemon.append(Pokemon(129,['magicarpe'],'Magicarpe',20,10,55,80,20,15,20,False,['Léviator'],[20],'Eau',False,1280,50,50,255,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],['Plante'],False))
listepokemon.append(Pokemon(130,['leviator','léviathor','leviathor'],'Léviator',95,125,79,81,100,60,100,'Magicarpe',False,False,'Eau','Vol',1280,50,50,45,['Roche'],['Électrik'],['Feu','Eau','Combat','Insecte','Acier'],False,['Sol']))

listepokemon.append(Pokemon(131,['lokhlass'],'Lokhlass',130,85,80,60,95,85,95,False,False,False,'Eau','Glace',9945,50,50,90,['Combat','Électrik','Plante','Roche'],False,['Eau'],['Glace'],False))        

listepokemon.append(Pokemon(133,['evoli','Evoli','évoli'],'Évoli',55,55,50,55,65,45,65,False,['Aquali','Voltali','Pyroli','Mentali','Noctali'],['Utiliser une Pierre Eau','Utiliser une Pierre Foudre','Utiliser une Pierre Feu','+1 NV avec bonheur assez élevé (jour)','+1 NV avec bonheur assez élevé (nuit)'],'Normal',False,8670,87,13,45,['Combat'],False,False,False,['Spectre']))
listepokemon.append(Pokemon(134,['aquali'],'Aquali',130,65,60,65,110,110,95,'Évoli',False,False,'Eau',False,8670,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(135,['voltali'],'Voltali',65,65,60,95,110,110,95,'Évoli',False,False,'Électrik',False,8670,87,13,45,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(136,['pyroli'],'Pyroli',65,130,60,65,110,95,110,'Évoli',False,False,'Feu',False,8670,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))

listepokemon.append(Pokemon(143,['ronflex'],'Ronflex',160,110,65,30,65,65,110,False,False,False,'Normal',False,11240,13,87,25,['Combat'],False,False,False,['Spectre']))

listepokemon.append(Pokemon(144,['artikodin'],'Artikodin',90,85,100,85,125,95,125,False,False,False,'Glace','Vol',30345,0,0,3,['Feu','Électrik','Acier'],['Roche'],['Plante'],['Insecte','Plante'],['Sol']))
listepokemon.append(Pokemon(145,['électhor'],'Électhor',90,90,85,100,125,125,90,False,False,False,'Électrik','Vol',30345,0,0,3,['Glace','Roche'],False,['Plante','Combat','Vol','Insecte','Acier'],False,['Sol']))
listepokemon.append(Pokemon(146,['sulfura'],'Sulfura',90,100,90,90,125,125,85,False,False,False,'Feu','Vol',30345,0,0,3,['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))

listepokemon.append(Pokemon(147,['minidraco'],'Minidraco',41,64,45,50,50,50,50,False,['Draco'],[30],'Dragon',False,9945,50,50,45,['Dragon','Glace'],False,['Eau','Électrik','Feu','Plante'],False,False))
listepokemon.append(Pokemon(148,['draco'],'Draco',61,84,65,70,70,70,70,'Minidraco',['Dracolosse'],[55],'Dragon',False,9945,50,50,45,['Dragon','Glace'],False,['Eau','Électrik','Feu','Plante'],False,False))
listepokemon.append(Pokemon(149,['dracolosse'],'Dracolosse',91,134,95,80,100,100,100,'Draco',False,False,'Dragon','Vol',9945,50,50,45,['Dragon','Roche'],['Glace'],['Combat','Feu','Eau','Insecte'],['Plante'],['Sol']))

listepokemon.append(Pokemon(150,['mewtwo'],'Mewtwo',106,110,90,130,154,154,90,False,False,False,'Psy',False,30345,0,0,3,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))
listepokemon.append(Pokemon(151,['mew'],'Mew',100,100,100,100,100,100,100,False,False,False,'Psy',False,30345,0,0,3,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))

    #JOTHO

listepokemon.append(Pokemon(152,['germignon'],'Germignon',48,49,65,45,0,49,65,False,['Macronium'],[16],'Plante',False,5100,87,13,45,['Feu','Glace','Insecte','Poison','Vol'],False,['Eau','Électrik','Plante','Sol'],False,False))
listepokemon.append(Pokemon(153,['macronium'],'Macronium',60,62,80,60,0,63,80,'Germignon',['Méganium'],[32],'Plante',False,5100,87,13,45,['Feu','Glace','Insecte','Poison','Vol'],False,['Eau','Électrik','Plante','Sol'],False,False))
listepokemon.append(Pokemon(154,['meganium','méganium'],'Méganium',80,82,100,80,0,83,10,'Macronium',False,False,'Plante',False,5100,87,13,45,['Feu','Glace','Insecte','Poison','Vol'],False,['Eau','Électrik','Plante','Sol'],False,False))

listepokemon.append(Pokemon(155,['hericendre','héricendre','Hericendre'],'Héricendre',39,52,43,65,0,60,50,False,['Feurisson'],[14],'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(156,['feurisson'],'Feurisson',58,64,58,80,0,80,65,'Héricendre',['Typhlosion'],[36],'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(157,['typhlosion'],'Typhlosion',78,84,78,100,0,109,85,'Feurisson',False,False,'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))

listepokemon.append(Pokemon(158,['kaiminus'],'Kaiminus',50,65,64,43,0,44,48,False,['Crocrodil'],[18],'Eau',False,5100,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(159,['crocrodil'],'Crocrodil',65,80,80,58,0,59,63,'Kaiminus',['Aligatueur'],[30],'Eau',False,5100,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(160,['aligatueur'],'Aligatueur',85,105,100,78,0,79,83,'Crocrodil',False,False,'Eau',False,5100,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))

listepokemon.append(Pokemon(179,['wattouat'],'Wattouat',55,50,50,35,0,65,45,False,['Lainergie'],[15],'Électrik',False,5120,50,50,235,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(180,['lainergie'],'Lainergie',70,55,55,45,0,80,60,'Wattouat',['Pharamp'],[30],'Électrik',False,5120,50,50,120,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(181,['pharamp'],'Pharamp',90,75,75,55,0,115,90,'Lainergie',False,False,'Électrik',False,5120,50,50,45,['Sol'],False,['Acier','Électrik','Vol'],False,False))

listepokemon.append(Pokemon(196,['mentali'],'Mentali',65,65,60,110,0,130,95,'Évoli',False,False,'Psy',False,8670,87,13,45,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))
listepokemon.append(Pokemon(197,['noctali'],'Noctali',95,64,110,65,0,60,130,'Évoli',False,False,'Ténèbres',False,8670,87,13,45,['Combat','Insecte'],False,['Spectre','Ténèbres'],False,['Psy']))

listepokemon.append(Pokemon(243,['raiku','raikou','Raiku'],'Raikou',90,85,75,115,0,115,100,False,False,False,'Électrik',False,30345,0,0,3,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(244,['entei'],'Entei',115,115,85,100,0,90,75,False,False,False,'Feu',False,30345,0,0,3,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(245,['suicune'],'Suicune',100,75,115,85,0,90,115,False,False,False,'Eau',False,30345,0,0,3,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))

listepokemon.append(Pokemon(246,['embrylex'],'Embrylex',50,64,50,41,0,45,50,False,['Ymphect'],[30],'Roche','Ténèbres',10240,50,50,45,['Plante','Eau','Sol','Insecte','Acier'],['Combat'],['Normal','Feu','Poison','Vol','Spectre','Ténèbres'],False,['Psy']))
listepokemon.append(Pokemon(247,['ymphect'],'Ymphect',70,84,70,51,0,65,70,'Embrylex',['Tyranocif'],[55],'Roche','Ténèbres',10240,50,50,45,['Plante','Eau','Sol','Insecte','Acier'],['Combat'],['Normal','Feu','Poison','Vol','Spectre','Ténèbres'],False,['Psy']))
listepokemon.append(Pokemon(248,['tyranocif'],'Tyranocif',100,134,100,61,0,65,100,'Ymphect',False,False,'Roche','Ténèbres',10240,50,50,45,['Plante','Eau','Sol','Insecte','Acier'],['Combat'],['Normal','Feu','Poison','Vol','Spectre','Ténèbres'],False,['Psy']))

listepokemon.append(Pokemon(249,['lugia'],'Lugia',106,90,130,110,0,90,154,False,False,False,'Psy','Vol',30345,0,0,3,['Électrik','Glace','Roche','Spectre','Ténèbres'],False,['Plante','Psy'],['Combat'],['Sol']))
listepokemon.append(Pokemon(250,['hooh','ho-oh'],'Ho-Oh',106,130,90,90,0,110,154,False,False,False,'Feu','Vol',30345,0,0,3,['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))
listepokemon.append(Pokemon(251,['celebi','célébi','Célébi'],'Celebi',100,100,100,100,0,100,100,False,False,False,'Psy','Plante',30345,0,0,3,['Feu','Glace','Poison','Spectre','Ténèbres','Vol'],['Insecte'],['Combat','Eau','Électrik','Plante','Psy','Sol'],False,False))

    #HOENN

listepokemon.append(Pokemon(252,['arcko'],'Arcko',40,45,35,70,0,65,55,False,['Massko'],[16],'Plante',False,5120,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],False,False))
listepokemon.append(Pokemon(253,['massko'],'Massko',50,65,45,95,0,85,65,'Arcko',['Jungko'],[36],'Plante',False,5120,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],False,False))
listepokemon.append(Pokemon(254,['jungko'],'Jungko',70,85,65,120,0,105,85,'Massko',False,False,'Plante',False,5120,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],False,False))

listepokemon.append(Pokemon(255,['poussifeu'],'Poussifeu',45,60,40,45,0,70,50,False,['Galifeu'],[16],'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(256,['galifeu'],'Galifeu',60,85,60,55,0,85,60,'Poussifeu',['Braségali'],[36],'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(257,['braségali'],'Braségali',80,120,70,80,0,110,70,'Galifeu',False,False,'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))

listepokemon.append(Pokemon(258,['gobou'],'Gobou',50,70,50,40,0,50,50,False,['Flobio'],[16],'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(259,['flobio'],'Flobio',70,85,70,50,0,60,70,'Gobou',['Laggron'],[36],'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(260,['laggron'],'Laggron',100,110,90,60,0,85,90,'Flobio',False,False,'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))

listepokemon.append(Pokemon(304,['galekid','galékid'],'Galekid',50,70,100,30,0,40,40,False,['Galegon'],[32],'Acier','Roche',8960,50,50,180,['Glace','Psy','Insecte','Roche','Dragon'],['Normal','Vol'],['Eau'],['Combat','Sol'],['Poison']))
listepokemon.append(Pokemon(305,['galegon','galégon'],'Galegon',60,90,140,40,0,50,50,'Galekid',['Galeking'],[42],'Acier','Roche',8960,50,50,90,['Glace','Psy','Insecte','Roche','Dragon'],['Normal','Vol'],['Eau'],['Combat','Sol'],['Poison']))
listepokemon.append(Pokemon(306,['galeking','galéking'],'Galeking',70,110,180,50,0,60,60,'Galegon',False,False,'Acier','Roche',8960,50,50,45,['Glace','Psy','Insecte','Roche','Dragon'],['Normal','Vol'],['Eau'],['Combat','Sol'],['Poison']))

listepokemon.append(Pokemon(362,['oniglali'],'Oniglali',80,80,80,80,0,80,80,'Stalgamin',False,False,'Glace',False,5120,50,50,75,['Feu','Combat','Roche','Acier'],False,['Glace'],False,False))

listepokemon.append(Pokemon(382,['kyogre'],'Kyogre',100,100,90,90,0,150,140,False,False,False,'Eau',False,30345,0,0,3,['Plante','Électrik'],False,['Feu','Eau','Glace','Acier'],False,False))
listepokemon.append(Pokemon(383,['groudon'],'Groudon',100,150,140,90,0,100,90,False,False,False,'Feu',False,30345,0,0,3,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(384,['rayquaza'],'Rayquaza',105,150,90,95,0,150,90,False,False,False,'Dragon','Vol',30345,0,0,3,['Dragon','Roche'],['Glace'],['Combat','Feu','Eau','Insecte'],['Plante'],['Sol']))

#FONCTIONS

for i in listepokemon:
    i.rawnom.append(str(i.num))

listenompokemon=[]

for i in listepokemon:
    listenompokemon.append(i.nom)
    
def positionlistepokemon(nom):
    for i in listenompokemon:
        if i == nom:
            return get_num(i)
listeversion=['Or','Argent']

def checktypes(typeachercher):
    for i in listepokemon:
        if i.type1 == typeachercher or i.type2 == typeachercher:
            print(i.nom+'    '+str(i.type1)+'   '+str(i.type2))
            
liste1g=[]
for i in listepokemon:
    if i.num <= 151:
        liste1g.append(i)
print(str(int((int(len(liste1g))/151)*100))+'% des Pokémons 1G implémantés')
        
liste2g=[]
for i in listepokemon:
    if i.num <= 251 and i.num >=152:
        liste2g.append(i)
print(str(int((int(len(liste2g))/100)*100))+'% des Pokémons 2G implémantés')

liste3g=[]
for i in listepokemon:
    if i.num >= 252:
        liste3g.append(i)
print(str(int((int(len(liste3g))/135)*100))+'% des Pokémons 3G implémantés')


for i in listepokemon:
    gererimg = Image.open('images/sprites3g/'+i.nom+'.png')
for i in listepokemon:
    gererimg = Image.open('images/sprites3g/back/'+i.nom+'.png')
for i in listepokemon:
    gererimg = Image.open('images/sprites3g/shiny/'+i.nom+'.png')
for i in listepokemon:
    gererimg = Image.open('images/sprites3g/shiny/back/'+i.nom+'.png')
for i in listepokemon:
    gererimg = Image.open('images/sprites3g/icones/'+i.nom+'1.png')
for i in listepokemon:
    gererimg = Image.open('images/sprites3g/icones/'+i.nom+'2.png')