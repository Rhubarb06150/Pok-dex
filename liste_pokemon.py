#Pokédex 2 proto
#4/10/23
#Rhubarb

#classes
class Pokemon:
    def __init__(self,num,rawnom,nom,pv,force,defense,vitesse,specialgen1,attaquespeciale,defensespeciale,pre_evolution,evolution,evolution2,pre_evolution2,niveau_evolution,niveau_evolution2,condition_evolution,condition_evolution2,type1,type2,pasoeuf,male,femelle,taux_capture,faiblesses,dbfaiblesses,resistances,dbresistances,immunites):
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
        self.evolution2=evolution2
        self.pre_evolution2=pre_evolution2
        self.niveau_evolution=niveau_evolution
        self.niveau_evolution2=niveau_evolution2
        self.condition_evolution=condition_evolution
        self.condition_evolution2=condition_evolution2
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
    listeevolution=''
    for i in range(len(listepokemon)):
        
        if listepokemon[i].nom == nom:
            
            if listepokemon[i].evolution != False:
                for i2 in range(len(listepokemon[i].evolution)):
                    if nbevolutions > 0:
                        listeevolution += ', '
                    listeevolution += str(listepokemon[i].evolution[i2])
                    nbevolutions+=1
                    
                if listepokemon[i].evolution2 != False:
                    for i2 in range(len(listepokemon[i].evolution2)):
                        if nbevolutions > 0:
                            listeevolution += ', '
                        listeevolution += str(listepokemon[i].evolution2[i2])
                        nbevolutions+=1
                if nbevolutions > 1:
                    resultat=(listeevolution)
                    return resultat
                else:
                    resultat=(listeevolution)
                    return resultat
            if listepokemon[i].evolution == False and listepokemon[i].evolution == False:
                return 'Aucune évolution'
            
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
    
listepokemon=[]

    #KANTO

listepokemon.append(Pokemon(1,['bulbizarre','bublizarre','Bublizarre','bublizzare','bublizzarre','Bublizzare','Bublizzarre'],'Bulbizarre',45,49,49,45,65,65,65,False,['Herbizarre'],False,False,16,False,False,False,'Plante','Poison',5100,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],['Plante'],False))
listepokemon.append(Pokemon(2,['herbizarre','herbizzare','herbizzarre','Herbizzare','Herbizzarre'],'Herbizarre',60,62,63,60,80,80,80,'Bulbizarre',['Florizarre'],False,False,32,False,False,False,'Plante','Poison',5100,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],['Plante'],False))
listepokemon.append(Pokemon(3,['florizarre','florizzare','florizzarre','Florizzare','Florizzarre'],'Florizarre',80,82,83,80,100,100,100,'Herbizarre',False,False,False,False,False,False,False,'Plante','Poison',5100,87,13,45,['Feu','Glace','Psy','Vol'],False,['Combat','Eau','Électrik'],['Plante'],False))
listepokemon.append(Pokemon(4,['salameche','salamèche','Salameche'],'Salamèche',39,52,43,65,50,60,50,False,['Reptincel'],False,False,16,False,False,False,'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(5,['reptincel','Reptincel'],'Reptincel',58,64,58,80,80,80,65,'Salamèche',['Dracaufeu'],False,False,36,False,False,False,'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(6,['dracaufeu'],'Dracaufeu',78,84,78,100,85,80,65,'Reptincel',False,False,False,False,False,False,False,'Feu','Vol',5100,87,13,45,['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))
listepokemon.append(Pokemon(7,['carapuce'],'Carapuce',44,48,65,43,50,50,65,False,['Carabaffe'],False,False,16,False,False,False,'Eau',False,5100,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(8,['carabaffe'],'Carabaffe',59,63,80,58,65,65,80,'Carapuce',['Tortank'],False,False,36,False,False,False,'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(9,['tortank'],'Tortank',79,83,100,78,85,105,85,'Carabaffe',False,False,False,False,False,False,False,'Eau',False,5400,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(10,['chenipan'],'Chenipan',45,30,35,45,20,20,20,False,['Chrysacier'],False,False,7,False,False,False,'Insecte',False,3825,50,50,255,['Feu','Roche','Vol'],False,['Combat','Plante','Sol'],False,False))
listepokemon.append(Pokemon(11,['chrysacier'],'Chrysacier',50,20,55,30,25,25,25,'Chenipan',['Papillusion'],False,False,10,False,False,False,'Insecte',False,3825,50,50,120,['Feu','Roche','Vol'],False,['Combat','Plante','Sol'],False,False))
listepokemon.append(Pokemon(12,['papillusion'],'Papillusion',60,45,50,75,80,90,80,'Chrysacier',False,False,False,False,False,False,False,'Insecte','Vol',3825,50,50,45,['Électrik','Feu','Glace','Vol'],['Roche'],['Insecte'],['Combat','Plante'],['Sol']))
listepokemon.append(Pokemon(13,['aspicot'],'Aspicot',40,35,30,50,20,20,20,False,['Coconfort'],False,False,7,False,False,False,'Insecte','Poison',3825,50,50,255,['Feu','Psy','Roche','Vol'],False,['Insecte','Poison'],['Combat','Plante'],False))
listepokemon.append(Pokemon(14,['coconfort'],'Coconfort',45,25,50,35,25,25,25,'Aspicot',['Dardagnan'],False,False,10,False,False,False,'Insecte','Poison',3825,50,50,255,['Feu','Psy','Roche','Vol'],False,['Insecte','Poison'],['Combat','Plante'],False))
listepokemon.append(Pokemon(15,['dardagnan'],'Dardagnan',65,80,40,75,45,80,45,'Coconfort',False,False,False,False,False,False,False,'Insecte','Poison',3825,50,50,255,['Feu','Psy','Roche','Vol'],False,['Insecte','Poison'],['Combat','Plante'],False))
listepokemon.append(Pokemon(16,['roucoul','roucool','Roucoul'],'Roucool',40,45,40,56,35,35,35,False,['Roucoups'],False,False,18,False,False,False,'Normal','Vol',3825,50,50,255,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(17,['roucoups'],'Roucoups',63,60,55,71,50,50,50,'Roucool',['Roucarnage'],False,False,36,False,False,False,'Normal','Vol',3825,50,50,120,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(18,['roucarnage'],'Roucarnage',83,80,75,91,70,70,70,'Roucoups',False,False,False,False,False,False,False,'Normal','Vol',3825,50,50,45,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(19,['ratata','rattata'],'Rattata',30,56,35,72,25,25,35,False,['Rattatac'],False,False,20,False,False,False,'Normal',False,3825,50,50,255,['Combat'],False,False,False,['Spectre']))
listepokemon.append(Pokemon(20,['rattatac'],'Rattatac',55,81,60,97,50,50,70,'Rattata',False,False,False,False,False,False,False,'Normal',False,3825,50,50,255,['Combat'],False,False,False,['Spectre']))
listepokemon.append(Pokemon(21,['piafabec'],'Piafabec',40,60,30,70,31,31,31,False,['Rapasdepic'],False,False,20,False,False,False,'Normal','Vol',3825,50,50,255,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(22,['rapasdepic'],'Rapasdepic',65,90,65,61,61,61,100,'Piafabec',False,False,False,False,False,False,False,'Normal','Vol',3825,50,50,255,['Électrik','Glace','Roche'],False,['Insecte','Plante'],False,['Sol','Spectre']))
listepokemon.append(Pokemon(23,['abo'],'Abo',35,60,44,55,40,40,54,False,['Arbok'],False,False,22,False,False,False,'Poison',False,3825,50,50,255,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(24,['arbok'],'Arbok',60,95,69,80,65,65,79,'Abo',False,False,False,False,False,False,False,'Poison',False,3825,50,50,90,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(25,['pikachu'],'Pikachu',35,55,40,90,50,50,50,False,['Raichu'],False,'Pichu',False,False,['Utiliser une Pierre Foudre'],False,'Électrik',False,2295,50,50,190,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(26,['raichu'],'Raichu',60,90,55,110,90,90,80,'Pikachu',False,False,False,False,False,False,False,'Électrik',False,2295,50,50,75,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(27,['sabelette'],'Sabelette',50,75,85,40,30,20,30,False,['Sablaireau'],False,False,22,False,False,False,'Sol',False,5100,50,50,255,['Eau','Glace','Plante'],False,['Poison','Roche'],False,['Électrik']))
listepokemon.append(Pokemon(28,['sablaireau'],'Sablaireau',75,100,110,65,55,45,55,'Sabelette',False,False,False,False,False,False,False,'Sol',False,5100,50,50,900,['Eau','Glace','Plante'],False,['Poison','Roche'],False,['Électrik']))
listepokemon.append(Pokemon(29,['nidoran F','Nidoran F','nidoran f'],'Nidoran F',55,47,52,41,40,40,40,False,['Nidorina'],False,False,16,False,False,False,'Poison',False,5100,0,100,235,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(30,['nidorina'],'Nidorina',70,62,67,56,55,55,55,'Nidoran F',['Nidoqueen'],False,False,False,False,['Utiliser une Pierre Lune'],False,'Poison',False,5100,0,100,120,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(31,['nidoqueen'],'Nidoqueen',90,92,87,76,75,75,85,'Nidorina',False,False,False,False,False,False,False,'Poison','Sol',5100,0,100,45,['Eau','Glace','Sol','Psy'],False,['Combat','Insecte','Roche'],['Poison'],['Électrik']))
listepokemon.append(Pokemon(32,['nidoran M','nidoran m','Nidoran M'],'Nidoran M',46,57,40,50,40,40,40,False,['Nidorino'],False,False,16,False,False,False,'Poison',False,5100,100,0,235,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(33,['nidorino'],'Nidorino',61,72,57,65,55,55,55,'Nidoran M',['Nidoking'],False,False,False,False,['Utiliser une Pierre Lune'],False,'Poison',False,5100,100,0,120,['Psy','Sol'],False,['Combat','Insecte','Plante','Poison'],False,False))
listepokemon.append(Pokemon(34,['nidoking'],'Nidoking',81,102,77,85,75,85,75,'Nidorino',False,False,False,False,False,False,False,'Poison','Sol',5100,100,0,45,['Eau','Glace','Sol','Psy'],False,['Combat','Insecte','Roche'],['Poison'],['Électrik']))
#listepokemon.append(Pokemon(35,['mélofée','melofee','Mélofée','Melofee',],'Mélofée',70,45,48,35,
#listepokemon.append(Pokemon(35,['ectoplasma'],'Ectoplasma',30,35,30,80,100,100,35,False,['Spectrum'],False,False


listepokemon.append(Pokemon(131,['lokhlass'],'Lokhlass',130,85,80,60,95,85,95,False,False,False,False,False,False,False,False,'Eau','Glace',9945,50,50,90,['Combat','Électrik','Plante','Roche'],False,['Eau'],['Glace'],False))        
listepokemon.append(Pokemon(133,['evoli','Evoli','évoli'],'Évoli',55,55,50,55,65,45,65,False,['Aquali','Voltali','Pyroli'],['Mentali','Noctali'],False,False,False,['Utiliser une Pierre Eau','Utiliser une Pierre Foudre','Utiliser une Pierre Feu'],['Prendre un niveau avec le bonheur suffisamment élevé, pendant la journée','Prendre un niveau avec le bonheur suffisamment élevé, pendant la nuit'],'Normal',False,8670,87,13,45,['Combat'],False,False,False,['Spectre']))
listepokemon.append(Pokemon(134,['aquali'],'Aquali',130,65,60,65,110,110,95,'Évoli',False,False,False,False,False,False,False,'Eau',False,8670,87,13,45,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
listepokemon.append(Pokemon(135,['voltali'],'Voltali',65,65,60,95,110,110,95,'Évoli',False,False,False,False,False,False,False,'Électrik',False,8670,87,13,45,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(136,['pyroli'],'Pyroli',65,130,60,65,110,95,110,'Évoli',False,False,False,False,False,False,False,'Feu',False,8670,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(144,['artikodin'],'Artikodin',90,85,100,85,125,95,125,False,False,False,False,False,False,False,False,'Glace','Vol',30345,0,0,3,['Feu','Électrik','Acier'],['Roche'],['Plante'],['Insecte','Plante'],['Sol']))
listepokemon.append(Pokemon(146,['sulfura'],'Sulfura',90,100,90,90,125,125,85,False,False,False,False,False,False,False,False,'Feu','Vol',30345,0,0,3,['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))
listepokemon.append(Pokemon(147,['minidraco'],'Minidraco',41,64,45,50,50,50,50,False,['Draco'],False,False,30,False,False,False,'Dragon',False,9945,50,50,45,['Dragon','Glace'],False,['Eau','Électrik','Feu','Plante'],False,False))
listepokemon.append(Pokemon(148,['draco'],'Draco',61,84,65,70,70,70,70,'Minidraco',['Dracolosse'],False,False,55,False,False,False,'Dragon',False,9945,50,50,45,['Dragon','Glace'],False,['Eau','Électrik','Feu','Plante'],False,False))
listepokemon.append(Pokemon(149,['dracolosse'],'Dracolosse',91,134,95,80,100,100,100,'Draco',False,False,False,False,False,False,False,'Dragon','Vol',9945,50,50,45,['Dragon','Roche'],['Glace'],['Combat','Feu','Eau','Insecte'],['Plante'],['Sol']))
listepokemon.append(Pokemon(150,['mewtwo'],'Mewtwo',106,110,90,130,154,154,90,False,False,False,False,False,False,False,False,'Psy',False,30345,0,0,3,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))

    #JOHTO

listepokemon.append(Pokemon(151,['mew'],'Mew',100,100,100,100,100,100,100,False,False,False,False,False,False,False,False,'Psy',False,30345,0,0,3,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))
listepokemon.append(Pokemon(152,['germignon'],'Germignon',48,49,65,45,0,49,65,False,['Macronium'],False,False,16,False,False,False,'Plante',False,5100,87,13,45,['Feu','Glace','Insecte','Poison','Vol'],False,['Eau','Électrik','Plante','Sol'],False,False))
listepokemon.append(Pokemon(155,['hericendre','héricendre','Hericendre'],'Héricendre',39,52,43,65,0,60,50,False,['Feurisson'],False,False,14,False,False,False,'Feu',False,5100,87,13,45,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(179,['wattouat'],'Wattouat',55,50,50,35,0,65,45,False,['Lainergie'],False,False,15,False,False,False,'Électrik',False,5120,50,50,235,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(180,['lainergie'],'Lainergie',70,55,55,45,0,80,60,'Wattouat',['Pharamp'],False,False,30,False,False,False,'Électrik',False,5120,50,50,120,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(181,['pharamp'],'Pharamp',90,75,75,55,0,115,90,'Lainergie',False,False,False,False,False,False,False,'Électrik',False,5120,50,50,45,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(196,['mentali'],'Mentali',65,65,60,110,0,130,95,'Évoli',False,False,False,False,False,False,False,'Psy',False,8670,87,13,45,['Insecte','Spectre','Ténèbres'],False,['Combat','Psy'],False,False))
listepokemon.append(Pokemon(197,['noctali'],'Noctali',95,64,110,65,0,60,130,'Évoli',False,False,False,False,False,False,False,'Ténèbres',False,8670,87,13,45,['Combat','Insecte'],False,['Spectre','Ténèbres'],False,['Psy']))
listepokemon.append(Pokemon(243,['raiku','raikou','Raiku'],'Raikou',90,85,75,115,0,115,100,False,False,False,False,False,False,False,False,'Électrik',False,30345,0,0,3,['Sol'],False,['Acier','Électrik','Vol'],False,False))
listepokemon.append(Pokemon(244,['entei'],'Entei',115,115,85,100,0,90,75,False,False,False,False,False,False,False,False,'Feu',False,30345,0,0,3,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(245,['suicune'],'Suicune',100,75,115,85,0,90,115,False,False,False,False,False,False,False,False,'Eau',False,30345,0,0,3,['Électrik','Plante'],False,['Acier','Eau','Feu','Glace'],False,False))
<<<<<<< HEAD
#listepokemon.append(Pokemon(246,['embrylex'],'Embrylex',50,64,50,41,0,45,50,False,['Ymphect'],False,False,30,False,False,False,'Roche','Ténèbres'


=======
listepokemon.append(Pokemon(246,['embrylex'],'Embrylex',50,64,50,41,0,45,50,False,['Ymphect'],False,False,30,False,False,False,'Roche','Ténèbres',10240,50,50,45,['Normal','Feu','Vol','Roche'],['Poison'],['Glace','Combat','Sol','Acier'],['Plante','Eau'],['Électrik']))
listepokemon.append(Pokemon(247,['ymphect'],'Ymphect',70,84,70,51,0,65,70,'Embrylex',['Tyranocif'],False,False,55,False,False,False,'Roche','Ténèbres',10240,50,50,45,['Normal','Feu','Vol','Roche'],['Poison'],['Glace','Combat','Sol','Acier'],['Plante','Eau'],['Électrik']))
listepokemon.append(Pokemon(248,['tyranocif'],'Tyranocif',100,134,100,61,0,65,100,'Ymphect',False,False,False,False,False,False,False,'Roche','Ténèbres',10240,50,50,45,['Normal','Feu','Vol','Roche'],['Poison'],['Glace','Combat','Sol','Acier'],['Plante','Eau'],['Électrik']))
>>>>>>> 796529cdd3933e64a635825f28cb5e9e4f05e152
listepokemon.append(Pokemon(249,['lugia'],'Lugia',106,90,130,110,0,90,154,False,False,False,False,False,False,False,False,'Psy','Vol',30345,0,0,3,['Électrik','Glace','Roche','Spectre','Ténèbres'],False,['Plante','Psy'],['Combat'],['Sol']))
listepokemon.append(Pokemon(250,['hooh','ho-oh'],'Ho-Oh',106,130,90,90,0,110,154,False,False,False,False,False,False,False,False,'Feu','Vol',30345,0,0,3,['Eau','Électrik'],['Roche'],['Acier','Combat','Feu'],['Insecte','Plante'],['Sol']))
listepokemon.append(Pokemon(251,['celebi','célébi','Célébi'],'Celebi',100,100,100,100,0,100,100,False,False,False,False,False,False,False,False,'Psy','Plante',30345,0,0,3,['Feu','Glace','Poison','Spectre','Ténèbres','Vol'],['Insecte'],['Combat','Eau','Électrik','Plante','Psy','Sol'],False,False))

    #HOENN

listepokemon.append(Pokemon(382,['kyogre'],'Kyogre',100,100,90,90,0,150,140,False,False,False,False,False,False,False,False,'Eau',False,30345,0,0,3,['Plante','Électrik'],False,['Feu','Eau','Glace','Acier'],False,False))
listepokemon.append(Pokemon(383,['groudon'],'Groudon',100,150,140,90,0,100,90,False,False,False,False,False,False,False,False,'Feu',False,30345,0,0,3,['Eau','Roche','Sol'],False,['Acier','Feu','Glace','Insecte','Plante'],False,False))
listepokemon.append(Pokemon(384,['rayquaza'],'Rayquaza',105,150,90,95,0,150,90,False,False,False,False,False,False,False,False,'Dragon','Vol',30345,0,0,3,['Dragon','Roche'],['Glace'],['Combat','Feu','Eau','Insecte'],['Plante'],['Sol']))

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