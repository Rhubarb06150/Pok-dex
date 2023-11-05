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
    def __init__(self,num,rawnom,nom,pv,force,defense,vitesse,specialgen1,attaquespeciale,defensespeciale,pre_evolution,evolution,condition_evolution,type1,type2,pasoeuf,male,femelle,taux_capture):
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
          
#listage des pokémons
    
class Types:

    def __init__(self,type1,faiblesses,resistances,immunites):
        
        self.type1=type1
        self.faiblesses=faiblesses
        self.resistances=resistances
        self.immunites=immunites

def get_fai(typew):
    for i in listetypes:
        if i.type1 == typew:
            return i.faiblesses
def get_res(typew):
    for i in listetypes:
        if i.type1 == typew:
            return i.resistances
def get_imm(typew):
    for i in listetypes:
        if i.type1 == typew:
            return i.immunites
        
listetypes=[]

listetypes.append(Types('Feu',['Eau','Roche','Sol'],['Acier','Feu','Glace','Insecte','Plante'],False))
listetypes.append(Types('Vol',['Électrik','Glace','Roche'],['Combat','Insecte','Plante'],['Sol']))
listetypes.append(Types('Roche',['Acier','Combat','Eau','Plante'],['Feu','Normal','Poison','Vol'],False))
listetypes.append(Types('Eau',['Plante','Électrik'],['Acier','Eau','Feu','Glace'],False))
listetypes.append(Types('Sol',['Eau','Glace','Plante'],['Poison','Roche'],['Électrik']))
listetypes.append(Types('Électrik',['Sol'],['Acier','Électrik','Vol'],False))
listetypes.append(Types('Plante',['Feu','Glace','Insecte','Poison','Vol'],['Sol','Plante','Électrik','Eau'],False))
listetypes.append(Types('Poison',['Psy','Sol'],['Combat','Insecte','Plante','Poison'],False))
listetypes.append(Types('Glace',['Acier','Combat','Feu','Roche'],['Glace'],False))
listetypes.append(Types('Psy',['Insecte','Spectre','Ténèbres'],['Combat','Psy'],False))
listetypes.append(Types('Combat',['Psy','Vol'],['Ténèbres','Roche','Insecte'],False))
listetypes.append(Types('Ténèbres',['Combat','Insecte'],['Ténèbres','Spectre'],['Psy']))
listetypes.append(Types('Normal',['Combat'],[],['Spectre']))
listetypes.append(Types('Acier',['Combat','Feu','Sol'],['Acier','Dragon','Glace','Insecte','Normal','Plante','Psy','Roche','Vol'],['Poison']))
listetypes.append(Types('Insecte',['Feu','Roche','Vol'],['Combat','Plante','Sol'],False))
listetypes.append(Types('Spectre',['Spectre','Ténèbres'],['Insecte','Poison'],['Combat','Normal']))

listepokemon=[]

    #KANTO

listepokemon.append(Pokemon(1,['bulbizarre'],'Bulbizarre',45,49,49,45,65,65,65,False,['Herbizarre'],[16],'Plante','Poison',5100,87,13,45))
listepokemon.append(Pokemon(2,['herbizarre'],'Herbizarre',60,62,63,60,80,80,80,'Bulbizarre',['Florizarre'],[32],'Plante','Poison',5100,87,13,45))
listepokemon.append(Pokemon(3,['florizarre'],'Florizarre',80,82,83,80,100,100,100,'Herbizarre',False,False,'Plante','Poison',5100,87,13,45))

listepokemon.append(Pokemon(4,['salameche'],'Salamèche',39,52,43,65,50,60,50,False,['Reptincel'],[16],'Feu',False,5100,87,13,45,))
listepokemon.append(Pokemon(5,['reptincel'],'Reptincel',58,64,58,80,80,80,65,'Salamèche',['Dracaufeu'],[36],'Feu',False,5100,87,13,45))
listepokemon.append(Pokemon(6,['dracaufeu'],'Dracaufeu',78,84,78,100,85,80,65,'Reptincel',False,False,'Feu','Vol',5100,87,13,45))

listepokemon.append(Pokemon(7,['carapuce'],'Carapuce',44,48,65,43,50,50,65,False,['Carabaffe'],[16],'Eau',False,5100,87,13,45))
listepokemon.append(Pokemon(8,['carabaffe'],'Carabaffe',59,63,80,58,65,65,80,'Carapuce',['Tortank'],[36],'Eau',False,5400,87,13,45))
listepokemon.append(Pokemon(9,['tortank'],'Tortank',79,83,100,78,85,105,85,'Carabaffe',False,False,'Eau',False,5400,87,13,45))

listepokemon.append(Pokemon(10,['chenipan'],'Chenipan',45,30,35,45,20,20,20,False,['Chrysacier'],[7],'Insecte',False,3825,50,50,255))
listepokemon.append(Pokemon(11,['chrysacier'],'Chrysacier',50,20,55,30,25,25,25,'Chenipan',['Papillusion'],[10],'Insecte',False,3825,50,50,120))
listepokemon.append(Pokemon(12,['papillusion'],'Papillusion',60,45,50,75,80,90,80,'Chrysacier',False,False,'Insecte','Vol',3825,50,50,45))

listepokemon.append(Pokemon(13,['aspicot'],'Aspicot',40,35,30,50,20,20,20,False,['Coconfort'],[7],'Insecte','Poison',3825,50,50,255))
listepokemon.append(Pokemon(14,['coconfort'],'Coconfort',45,25,50,35,25,25,25,'Aspicot',['Dardagnan'],[10],'Insecte','Poison',3825,50,50,255))
listepokemon.append(Pokemon(15,['dardagnan'],'Dardagnan',65,80,40,75,45,80,45,'Coconfort',False,False,'Insecte','Poison',3825,50,50,255))

listepokemon.append(Pokemon(16,['roucoul','roucool','Roucoul'],'Roucool',40,45,40,56,35,35,35,False,['Roucoups'],[18],'Normal','Vol',3825,50,50,255))
listepokemon.append(Pokemon(17,['roucoups'],'Roucoups',63,60,55,71,50,50,50,'Roucool',['Roucarnage'],[36],'Normal','Vol',3825,50,50,120))
listepokemon.append(Pokemon(18,['roucarnage'],'Roucarnage',83,80,75,91,70,70,70,'Roucoups',False,False,'Normal','Vol',3825,50,50,45))

listepokemon.append(Pokemon(19,['rattata'],'Rattata',30,56,35,72,25,25,35,False,['Rattatac'],[20],'Normal',False,3825,50,50,255))
listepokemon.append(Pokemon(20,['rattatac'],'Rattatac',55,81,60,97,50,50,70,'Rattata',False,False,'Normal',False,3825,50,50,255))

listepokemon.append(Pokemon(21,['piafabec'],'Piafabec',40,60,30,70,31,31,31,False,['Rapasdepic'],[20],'Normal','Vol',3825,50,50,255))
listepokemon.append(Pokemon(22,['rapasdepic'],'Rapasdepic',65,90,65,61,61,61,100,'Piafabec',False,False,'Normal','Vol',3825,50,50,255))

listepokemon.append(Pokemon(23,['abo'],'Abo',35,60,44,55,40,40,54,False,['Arbok'],[22],'Poison',False,3825,50,50,255))
listepokemon.append(Pokemon(24,['arbok'],'Arbok',60,95,69,80,65,65,79,'Abo',False,False,'Poison',False,3825,50,50,90))

listepokemon.append(Pokemon(25,['pikachu'],'Pikachu',35,55,40,90,50,50,50,'Pichu',['Raichu'],['Utiliser une Pierre Foudre'],'Électrik',False,2295,50,50,190))
listepokemon.append(Pokemon(26,['raichu'],'Raichu',60,90,55,110,90,90,80,'Pikachu',False,False,'Électrik',False,2295,50,50,75))

listepokemon.append(Pokemon(27,['sabelette'],'Sabelette',50,75,85,40,30,20,30,False,['Sablaireau'],[22],'Sol',False,5100,50,50,255))
listepokemon.append(Pokemon(28,['sablaireau'],'Sablaireau',75,100,110,65,55,45,55,'Sabelette',False,False,'Sol',False,5100,50,50,900))

listepokemon.append(Pokemon(29,['nidoran f'],'Nidoran F',55,47,52,41,40,40,40,False,['Nidorina'],[16],'Poison',False,5100,0,100,235))
listepokemon.append(Pokemon(30,['nidorina'],'Nidorina',70,62,67,56,55,55,55,'Nidoran F',['Nidoqueen'],['Utiliser une Pierre Lune'],'Poison',False,5100,0,100,120))
listepokemon.append(Pokemon(31,['nidoqueen'],'Nidoqueen',90,92,87,76,75,75,85,'Nidorina',False,False,'Poison','Sol',5100,0,100,45))

listepokemon.append(Pokemon(32,['nidoran M','nidoran m','Nidoran M'],'Nidoran M',46,57,40,50,40,40,40,False,['Nidorino'],[16],'Poison',False,5100,100,0,235))
listepokemon.append(Pokemon(33,['nidorino'],'Nidorino',61,72,57,65,55,55,55,'Nidoran M',['Nidoking'],['Utiliser une Pierre Lune'],'Poison',False,5100,100,0,120))
listepokemon.append(Pokemon(34,['nidoking'],'Nidoking',81,102,77,85,75,85,75,'Nidorino',False,False,'Poison','Sol',5100,100,0,45))

listepokemon.append(Pokemon(35,['melofee'],'Mélofée',70,45,48,35,60,60,65,'Mélo',['Mélodelefe'],['Utiliser une Pierre Lune'],'Normal',False,2560,25,75,150))
listepokemon.append(Pokemon(36,['melodelfe'],'Mélodelfe',95,90,73,60,85,90,85,'Mélofée',False,False,'Normal',False,2560,25,75,25))

listepokemon.append(Pokemon(37,['goupix'],'Goupix',38,41,40,65,65,50,65,False,['Feunard'],['Utiliser une Pierre Feu'],'Feu',False,5100,25,75,190))
listepokemon.append(Pokemon(38,['feunard'],'Feunard',373,76,75,100,100,81,100,'Goupix',False,False,'Feu',False,5100,25,75,75))

listepokemon.append(Pokemon(39,['rondoudou'],'Rondoudou',115,45,20,20,25,45,25,'Toudoudou','Grodoudou',['Utiliser une Pierre Lune'],'Normal',False,2560,25,75,170))
listepokemon.append(Pokemon(40,['grondoudou'],'Grodoudou',140,70,45,45,50,75,50,'Rondoudou',False,False,'Normal',False,2560,25,75,50))

listepokemon.append(Pokemon(41,['nosferapti'],'Nosférapti',40,45,35,55,40,30,40,False,['Nosféralto'],[22],'Poison','Vol',3840,50,50,90))
listepokemon.append(Pokemon(42,['nosferalto'],'Nosféralto',75,80,70,90,75,65,75,'Nosférapti',['Nostenfer'],['+1 Niveau avec bonheur assez élevé'],'Poison','Vol',3840,50,50,50))

listepokemon.append(Pokemon(43,['mystherbe'],'Mystherbe',45,50,55,30,75,75,65,False,['Ortide'],[21],'Plante','Poison',5120,50,50,255))
listepokemon.append(Pokemon(44,['ortide'],'Ortide',60,65,70,40,85,85,75,'Mystherbe',['Raflésia','Joliflor'],['Utiliser une Pierre Plante','Utiliser une Pierre Soleil'],'Plante','Poison',5120,50,50,120))
listepokemon.append(Pokemon(45,['raflésia'],'Raflésia',75,80,85,50,100,110,90,'Ortide',False,False,'Plante','Poison',5120,50,50,45))

listepokemon.append(Pokemon(46,['paras'],'Paras',35,70,55,25,55,45,55,False,['Parasect'],[24],'Insecte','Plante',5120,50,50,190))
listepokemon.append(Pokemon(47,['parasect'],'Parasect',60,95,80,30,80,60,80,'Paras',False,False,'Insecte','Plante',5120,50,50,75))

listepokemon.append(Pokemon(48,['mimitoss'],'Mimitoss',60,55,50,45,40,40,55,False,['Aéromite'],[31],'Insecte','Poison',5120,50,50,190))
listepokemon.append(Pokemon(49,['aeromite','aéromite'],'Aéromite',70,65,60,90,90,90,75,'Mimitoss',False,False,'Insecte','Poison',5120,50,50,75))

listepokemon.append(Pokemon(50,['taupiquer'],'Taupiqueur',10,55,25,95,45,35,45,False,['Triopikeur'],[26],'Sol',False,5120,50,50,255))
listepokemon.append(Pokemon(51,['triopikeur'],'Triopikeur',35,80,50,120,70,50,70,'Taupiqueur',False,False,'Sol',False,5120,50,50,50))

listepokemon.append(Pokemon(52,['miaouss'],'Miaouss',40,45,35,90,40,40,40,False,['Persian'],[28],'Normal',False,5120,50,50,255))
listepokemon.append(Pokemon(53,['persian'],'Persian',65,70,60,115,65,65,65,'Miaouss',False,False,'Normal',False,5120,50,50,90))

listepokemon.append(Pokemon(54,['psykokwak'],'Psykokwak',50,52,48,55,50,65,50,False,['Akwakwak'],[33],'Eau','Psy',5120,50,50,190))
listepokemon.append(Pokemon(55,['akwakwak'],'Akwakwak',80,82,78,85,80,95,80,'Psykokwak',False,False,'Eau','Psy',5120,50,50,75))

listepokemon.append(Pokemon(56,['férosinge','Ferosinge','ferosinge'],'Férosinge',40,80,35,70,35,35,45,False,['Colossinge'],[20],'Combat',False,5120,50,50,190))
listepokemon.append(Pokemon(57,['colossinge'],'Colossinge',65,105,60,95,60,60,70,'Férosinge',False,False,'Combat',False,5120,50,50,75))

listepokemon.append(Pokemon(58,['caninos'],'Caninos',55,70,45,60,50,70,50,False,['Arcanin'],['Utiliser une Pierre Feu'],'Feu',False,5120,75,25,190))
listepokemon.append(Pokemon(59,['arcanin'],'Arcanin',90,110,80,95,80,100,80,'Caninos',False,False,'Feu',False,5120,75,25,75))

listepokemon.append(Pokemon(60,['ptitard'],'Ptitard',40,50,40,90,40,40,40,False,['Tétârte'],[25],'Eau',False,5120,50,50,255))
listepokemon.append(Pokemon(61,['tetarte','tétarte'],'Tétârte',65,65,65,90,50,50,50,'Ptitard',['Tartard','Tarpaud'],['Utiliser une Pierre Eau','Échange en tenant une Roche Royale'],'Eau',False,5120,50,50,120))
listepokemon.append(Pokemon(62,['tartard'],'Tartard',90,95,95,70,000,70,90,'Tétârte',False,False,'Eau','Combat',5120,50,50,45))

listepokemon.append(Pokemon(63,['abra'],'Abra',25,20,15,90,105,105,55,False,['Kadabra'],[16],'Psy',False,5120,75,25,200))
listepokemon.append(Pokemon(64,['kadabra'],'Kadabra',40,35,30,105,120,120,70,'Abra',['Alakazam'],['Échange'],'Psy',False,5120,75,25,100))
listepokemon.append(Pokemon(65,['alakazam'],'Alakazam',55,50,45,120,135,135,85,'Kadabra',False,False,'Psy',False,5120,75,25,50))

listepokemon.append(Pokemon(66,['machoc'],'Machoc',70,80,50,35,35,35,35,False,['Machopeur'],[28],'Combat',False,5120,75,25,255))
listepokemon.append(Pokemon(67,['machopeur'],'Machopeur',80,100,70,45,50,50,60,'Machoc',['Mackogneur'],['Échange'],'Combat',False,5120,75,25,90))
listepokemon.append(Pokemon(68,['mackogneur'],'Mackogneur',90,130,80,55,64,64,85,'Machopeur',False,False,'Combat',False,5120,75,25,45))

listepokemon.append(Pokemon(69,['chetiflor'],'Chétiflor',50,75,35,40,70,70,30,False,['Boustiflor'],[21],'Plante','Poison',5120,50,50,255))
listepokemon.append(Pokemon(70,['boustiflor'],'Boustiflor',65,90,50,40,85,85,45,'Chétiflor',['Empiflor'],['Utiliser une Pierre Plante'],'Plante','Poison',5120,50,50,90))
listepokemon.append(Pokemon(71,['empiflor'],'Empiflor',80,105,65,70,100,100,60,'Boustiflor',False,False,'Plante','Poison',5120,50,50,45))

listepokemon.append(Pokemon(72,['tentacool'],'Tentacool',40,40,35,70,100,50,100,False,['Tentacruel'],[30],'Eau','Poison',5120,50,50,190))
listepokemon.append(Pokemon(73,['tentacruel'],'Tentacruel',80,70,65,100,120,80,120,'Tentacool',False,False,'Eau','Poison',5120,50,50,60))

listepokemon.append(Pokemon(74,['racaillou'],'Racaillou',40,80,100,20,30,30,30,False,['Gravalanch'],[25],'Roche','Sol',3840,50,50,255))
listepokemon.append(Pokemon(75,['gravalanch'],'Gravalanch',55,95,115,35,45,45,45,'Racaillou',['Grolem'],['Échange'],'Roche','Sol',3840,50,50,120))
listepokemon.append(Pokemon(76,['grolem'],'Grolem',80,110,130,45,55,55,55,'Gravalanch',False,False,'Roche','Sol',3840,50,50,45))

listepokemon.append(Pokemon(77,['ponyta'],'Ponyta',50,85,55,90,65,65,65,False,['Galopa'],[40],'Feu',False,5120,50,50,190))
listepokemon.append(Pokemon(78,['galopa'],'Galopa',65,100,70,105,80,80,80,'Ponyta',False,False,'Feu',False,5120,50,50,60))

listepokemon.append(Pokemon(92,['fantominus'],'Fantominus',30,35,30,80,100,100,35,False,['Spectrum'],[25],'Spectre','Poison',5120,50,50,190))
listepokemon.append(Pokemon(93,['spectrum'],'Spectrum',45,50,45,95,115,115,55,'Fantominus',['Ectoplasma'],['Échange'],'Spectre','Poison',5120,50,50,90))
listepokemon.append(Pokemon(94,['ectoplasma'],'Ectoplasma',60,65,60,110,130,130,75,'Spectrum',False,False,'Spectre','Poison',5120,50,50,45))

listepokemon.append(Pokemon(102,['noeunoeuf'],'Noeunoeuf',60,40,80,40,60,60,45,False,['Noadkoko'],['Utiliser une Pierre Plante'],'Plante','Psy',5120,50,50,90))
listepokemon.append(Pokemon(103,['noadkoko'],'Noadkoko',95,95,85,55,125,125,65,'Noeunoeuf',False,False,'Plante','Psy',5120,50,50,45))

listepokemon.append(Pokemon(127,['scarabrute'],'Scarabrute',65,125,100,85,55,55,70,False,False,False,'Insecte',False,6400,50,50,45))

listepokemon.append(Pokemon(128,['tauros'],'Tauros',75,100,95,110,70,40,70,False,False,False,'Normal',False,5120,100,0,45))

listepokemon.append(Pokemon(129,['magicarpe'],'Magicarpe',20,10,55,80,20,15,20,False,['Léviator'],[20],'Eau',False,1280,50,50,255,))
listepokemon.append(Pokemon(130,['leviator','léviathor','leviathor'],'Léviator',95,125,79,81,100,60,100,'Magicarpe',False,False,'Eau','Vol',1280,50,50,45))

listepokemon.append(Pokemon(131,['lokhlass'],'Lokhlass',130,85,80,60,95,85,95,False,False,False,'Eau','Glace',9945,50,50,90))        

listepokemon.append(Pokemon(132,['métamorph','Metamorph','metamorph'],'Métamorph',48,48,48,48,48,48,48,False,False,False,'Normal',False,5120,100,0,35))

listepokemon.append(Pokemon(133,['evoli'],'Évoli',55,55,50,55,65,45,65,False,['Aquali','Voltali','Pyroli','Mentali','Noctali'],['Utiliser une Pierre Eau','Utiliser une Pierre Foudre','Utiliser une Pierre Feu','+1 NV avec bonheur assez élevé (jour)','+1 NV avec bonheur assez élevé (nuit)'],'Normal',False,8670,87,13,45))
listepokemon.append(Pokemon(134,['aquali'],'Aquali',130,65,60,65,110,110,95,'Évoli',False,False,'Eau',False,8670,87,13,45))
listepokemon.append(Pokemon(135,['voltali'],'Voltali',65,65,60,95,110,110,95,'Évoli',False,False,'Électrik',False,8670,87,13,45))
listepokemon.append(Pokemon(136,['pyroli'],'Pyroli',65,130,60,65,110,95,110,'Évoli',False,False,'Feu',False,8670,87,13,45))

listepokemon.append(Pokemon(137,['porygon'],'Porygon',65,60,70,40,75,85,75,False,['Porygon 2'],["Au contact d'un Améliorator"],'Normal',False,5120,0,0,45))

listepokemon.append(Pokemon(138,['amonita'],'Amonita',35,40,100,35,90,90,55,False,['Amonistar'],[40],'Normal',False,7860,87,13,45))
listepokemon.append(Pokemon(139,['amonistar'],'Amonistar',70,60,125,55,115,115,70,'Amonita',False,False,'Normal',False,7860,87,13,45))

listepokemon.append(Pokemon(140,['kabuto'],'Kabuto',30,80,90,55,45,55,45,False,['Kabutops'],[40],'Normal',False,7860,87,13,45))
listepokemon.append(Pokemon(141,['kabutops'],'Kabutops',60,115,105,80,70,65,70,'Kabuto',False,False,'Normal',False,7860,87,13,45))

listepokemon.append(Pokemon(142,['ptera','Ptéra','Ptera'],'Ptéra',80,105,65,130,60,60,75,False,False,False,'Roche','Vol',8960,13,87,45))

listepokemon.append(Pokemon(143,['ronflex'],'Ronflex',160,110,65,30,65,65,110,False,False,False,'Normal',False,11240,13,87,25))

listepokemon.append(Pokemon(144,['artikodin'],'Artikodin',90,85,100,85,125,95,125,False,False,False,'Glace','Vol',30345,0,0,3))
listepokemon.append(Pokemon(145,['électhor'],'Électhor',90,90,85,100,125,125,90,False,False,False,'Électrik','Vol',30345,0,0,3))
listepokemon.append(Pokemon(146,['sulfura'],'Sulfura',90,100,90,90,125,125,85,False,False,False,'Feu','Vol',30345,0,0,3))

listepokemon.append(Pokemon(147,['minidraco'],'Minidraco',41,64,45,50,50,50,50,False,['Draco'],[30],'Dragon',False,9945,50,50,45))
listepokemon.append(Pokemon(148,['draco'],'Draco',61,84,65,70,70,70,70,'Minidraco',['Dracolosse'],[55],'Dragon',False,9945,50,50,45))
listepokemon.append(Pokemon(149,['dracolosse'],'Dracolosse',91,134,95,80,100,100,100,'Draco',False,False,'Dragon','Vol',9945,50,50,45))

listepokemon.append(Pokemon(150,['mewtwo'],'Mewtwo',106,110,90,130,154,154,90,False,False,False,'Psy',False,30345,0,0,3))
listepokemon.append(Pokemon(151,['mew'],'Mew',100,100,100,100,100,100,100,False,False,False,'Psy',False,30345,0,0,3))

    #JOTHO

listepokemon.append(Pokemon(152,['germignon'],'Germignon',48,49,65,45,0,49,65,False,['Macronium'],[16],'Plante',False,5100,87,13,45))
listepokemon.append(Pokemon(153,['macronium'],'Macronium',60,62,80,60,0,63,80,'Germignon',['Méganium'],[32],'Plante',False,5100,87,13,45))
listepokemon.append(Pokemon(154,['meganium','méganium'],'Méganium',80,82,100,80,0,83,10,'Macronium',False,False,'Plante',False,5100,87,13,45))

listepokemon.append(Pokemon(155,['hericendre'],'Héricendre',39,52,43,65,0,60,50,False,['Feurisson'],[14],'Feu',False,5100,87,13,45))
listepokemon.append(Pokemon(156,['feurisson'],'Feurisson',58,64,58,80,0,80,65,'Héricendre',['Typhlosion'],[36],'Feu',False,5100,87,13,45))
listepokemon.append(Pokemon(157,['typhlosion'],'Typhlosion',78,84,78,100,0,109,85,'Feurisson',False,False,'Feu',False,5100,87,13,45))

listepokemon.append(Pokemon(158,['kaiminus'],'Kaiminus',50,65,64,43,0,44,48,False,['Crocrodil'],[18],'Eau',False,5100,87,13,45))
listepokemon.append(Pokemon(159,['crocrodil'],'Crocrodil',65,80,80,58,0,59,63,'Kaiminus',['Aligatueur'],[30],'Eau',False,5100,87,13,45))
listepokemon.append(Pokemon(160,['aligatueur'],'Aligatueur',85,105,100,78,0,79,83,'Crocrodil',False,False,'Eau',False,5100,87,13,45))

listepokemon.append(Pokemon(179,['wattouat'],'Wattouat',55,50,50,35,0,65,45,False,['Lainergie'],[15],'Électrik',False,5120,50,50,235))
listepokemon.append(Pokemon(180,['lainergie'],'Lainergie',70,55,55,45,0,80,60,'Wattouat',['Pharamp'],[30],'Électrik',False,5120,50,50,120))
listepokemon.append(Pokemon(181,['pharamp'],'Pharamp',90,75,75,55,0,115,90,'Lainergie',False,False,'Électrik',False,5120,50,50,45))

listepokemon.append(Pokemon(196,['mentali'],'Mentali',65,65,60,110,0,130,95,'Évoli',False,False,'Psy',False,8670,87,13,45))
listepokemon.append(Pokemon(197,['noctali'],'Noctali',95,64,110,65,0,60,130,'Évoli',False,False,'Ténèbres',False,8670,87,13,45))

listepokemon.append(Pokemon(208,['steelix'],'Steelix',75,85,200,30,0,55,65,'Onyx',False,False,'Acier','Sol',6400,50,50,25))

listepokemon.append(Pokemon(243,['raiku','raikou','Raiku'],'Raikou',90,85,75,115,0,115,100,False,False,False,'Électrik',False,30345,0,0,3))
listepokemon.append(Pokemon(244,['entei'],'Entei',115,115,85,100,0,90,75,False,False,False,'Feu',False,30345,0,0,3))
listepokemon.append(Pokemon(245,['suicune'],'Suicune',100,75,115,85,0,90,115,False,False,False,'Eau',False,30345,0,0,3))

listepokemon.append(Pokemon(246,['embrylex'],'Embrylex',50,64,50,41,0,45,50,False,['Ymphect'],[30],'Roche','Ténèbres',10240,50,50,45))
listepokemon.append(Pokemon(247,['ymphect'],'Ymphect',70,84,70,51,0,65,70,'Embrylex',['Tyranocif'],[55],'Roche','Ténèbres',10240,50,50,45))
listepokemon.append(Pokemon(248,['tyranocif'],'Tyranocif',100,134,100,61,0,65,100,'Ymphect',False,False,'Roche','Ténèbres',10240,50,50,45))

listepokemon.append(Pokemon(249,['lugia'],'Lugia',106,90,130,110,0,90,154,False,False,False,'Psy','Vol',30345,0,0,3))
listepokemon.append(Pokemon(250,['hooh','ho-oh'],'Ho-Oh',106,130,90,90,0,110,154,False,False,False,'Feu','Vol',30345,0,0,3))
listepokemon.append(Pokemon(251,['celebi','célébi','Célébi'],'Celebi',100,100,100,100,0,100,100,False,False,False,'Psy','Plante',30345,0,0,3))

    #HOENN

listepokemon.append(Pokemon(252,['arcko'],'Arcko',40,45,35,70,0,65,55,False,['Massko'],[16],'Plante',False,5120,87,13,45,))
listepokemon.append(Pokemon(253,['massko'],'Massko',50,65,45,95,0,85,65,'Arcko',['Jungko'],[36],'Plante',False,5120,87,13,45,))
listepokemon.append(Pokemon(254,['jungko'],'Jungko',70,85,65,120,0,105,85,'Massko',False,False,'Plante',False,5120,87,13,45,))

listepokemon.append(Pokemon(255,['poussifeu'],'Poussifeu',45,60,40,45,0,70,50,False,['Galifeu'],[16],'Feu',False,5100,87,13,45))
listepokemon.append(Pokemon(256,['galifeu'],'Galifeu',60,85,60,55,0,85,60,'Poussifeu',['Braségali'],[36],'Feu',False,5100,87,13,45))
listepokemon.append(Pokemon(257,['braségali'],'Braségali',80,120,70,80,0,110,70,'Galifeu',False,False,'Feu',False,5100,87,13,45))

listepokemon.append(Pokemon(258,['gobou'],'Gobou',50,70,50,40,0,50,50,False,['Flobio'],[16],'Eau',False,5400,87,13,45))
listepokemon.append(Pokemon(259,['flobio'],'Flobio',70,85,70,50,0,60,70,'Gobou',['Laggron'],[36],'Eau',False,5400,87,13,45))
listepokemon.append(Pokemon(260,['laggron'],'Laggron',100,110,90,60,0,85,90,'Flobio',False,False,'Eau',False,5400,87,13,45))

listepokemon.append(Pokemon(304,['galekid','galékid'],'Galekid',50,70,100,30,0,40,40,False,['Galegon'],[32],'Acier','Roche',8960,50,50,180))
listepokemon.append(Pokemon(305,['galegon','galégon'],'Galegon',60,90,140,40,0,50,50,'Galekid',['Galeking'],[42],'Acier','Roche',8960,50,50,90))
listepokemon.append(Pokemon(306,['galeking','galéking'],'Galeking',70,110,180,50,0,60,60,'Galegon',False,False,'Acier','Roche',8960,50,50,45))

listepokemon.append(Pokemon(362,['oniglali'],'Oniglali',80,80,80,80,0,80,80,'Stalgamin',False,False,'Glace',False,5120,50,50,75))

listepokemon.append(Pokemon(382,['kyogre'],'Kyogre',100,100,90,90,0,150,140,False,False,False,'Eau',False,30345,0,0,3))
listepokemon.append(Pokemon(383,['groudon'],'Groudon',100,150,140,90,0,100,90,False,False,False,'Feu',False,30345,0,0,3))
listepokemon.append(Pokemon(384,['rayquaza'],'Rayquaza',105,150,90,95,0,150,90,False,False,False,'Dragon','Vol',30345,0,0,3))

#FONCTIONS

for i in listepokemon:
    i.rawnom.append(str(i.num))

listenompokemon=[]

for i in listepokemon:
    listenompokemon.append(i.nom)

listenomtypes=[]

for i in listetypes:
    listenomtypes.append(i.type1)
    
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

print(str(len(listepokemon))+' Pokémons ('+str(len(liste1g))+' de la 1G, '+str(len(liste2g))+' de la 2G, '+str(len(liste3g))+' de la 3G)')

def get_faiblesses(pokemon):

    res=[]

    for i in listepokemon:
        if i.nom == pokemon:
            if i.type2 != False:
                
                listefaiblesses1=get_fai(i.type1)
                listefaiblesses2=get_fai(i.type2)

                for types in listenomtypes:

                    if types in listefaiblesses1:
                        if types not in listefaiblesses2:
                            res.append(types)
                    elif types in listefaiblesses2:
                        if types not in listefaiblesses1:
                            res.append(types)

                for i3 in range(len(res)):
                    if res[i3-1] == get_imm(i.type1):
                        res.remove(res[i3-1])
                    elif res[i3-1] == get_imm(i.type2):
                        res.remove(res[i3-1])

                for i3 in range(len(get_res(i.type1))):
                    for i4 in range(len(res)):
                        if get_res(i.type1)[i3-1] == res[i4-1]:
                            res.remove(res[i4-1])

                for i3 in range(len(get_res(i.type2))):
                    for i4 in range(len(res)):
                        if get_res(i.type2)[i3-1] == res[i4-1]:
                            res.remove(res[i4-1])

                for i3 in range(len(res)):
                    if res[i3-1] in listefaiblesses1 and res[i3-1] in listefaiblesses2:
                        res.remove(res[i3-1])
            else:
                
                res=get_fai(i.type1)
    if res==[]:
        return False
    else:
        return res

def get_db_faiblesses(pokemon):

    res=[]

    for i in listepokemon:
        if i.nom == pokemon:
            if i.type2 != False:
                
                listefaiblesses1=get_fai(i.type1)
                listefaiblesses2=get_fai(i.type2)

                for i in listenomtypes:
                    if i in listefaiblesses1 and i in listefaiblesses2:
                        res.append(i)
            else:

                return False
    if res==[]:
        return False
    else:
        return res

def get_resistances(pokemon):

    res=[]

    for i in listepokemon:
        if i.nom == pokemon:
            if i.type2 != False:
                
                listeresistances1=get_res(i.type1)
                listeresistances2=get_res(i.type2)

                for types in listenomtypes:

                    if types in listeresistances1:
                        if types not in listeresistances2:
                            res.append(types)
                    elif types in listeresistances2:
                        if types not in listeresistances1:
                            res.append(types)

                for i3 in range(len(res)):
                    if res[i3-1] == get_imm(i.type1):
                        res.remove(res[i3-1])
                    elif res[i3-1] == get_imm(i.type2):
                        res.remove(res[i3-1])

                for i3 in range(len(get_fai(i.type1))):
                    for i4 in range(len(res)):
                        if get_fai(i.type1)[i3-1] == res[i4-1]:
                            res.remove(res[i4-1])

                for i3 in range(len(get_fai(i.type2))):
                    for i4 in range(len(res)):
                        if get_fai(i.type2)[i3-1] == res[i4-1]:
                            res.remove(res[i4-1])

                for i3 in range(len(res)):
                    if res[i3-1] in listeresistances1 and res[i3-1] in listeresistances2:
                        res.remove(res[i3-1])
            else:
                
                res=get_res(i.type1)

    if res==[]:
        return False
    else:
        return res

def get_db_resistances(pokemon):

    res=[]

    for i in listepokemon:
        if i.nom == pokemon:
            if i.type2 != False:
                
                listeresistances1=get_res(i.type1)
                listeresistances2=get_res(i.type2)

                for i in listenomtypes:
                    if i in listeresistances1 and i in listeresistances2:
                        res.append(i)
            else:

                return False
            
    if res==[]:
        return False
    else:
        return res
    
def get_immunites(pokemon):

    res=[]

    for i in listepokemon:
        if i.nom == pokemon:
            if get_imm(i.type1) != False:
                for types in get_imm(i.type1):
                    res.append(types)
            if i.type2 != False:
                if get_imm(i.type2) != False:
                    for types in get_imm(i.type2):
                        res.append(types)
    if res==[]:
        return False
    else:
        return res