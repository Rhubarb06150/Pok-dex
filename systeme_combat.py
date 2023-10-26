from liste_pokemon import *

def degats(attaque,equipelanceur,numlanceur,equipereceveur,numreceveur):
    
    file = open('txts/equipe'+str(equipelanceur)+'/membre'+str(numlanceur)+'.txt')
    lanceur = (file.read()).replace('1','')
    file.close
    
    file = open('txts/equipe'+str(equipereceveur)+'/membre'+str(numreceveur)+'.txt')
    receveur = (file.read()).replace('1','')
    file.close
    
    file = open('txts/equipe'+str(equipelanceur)+'/membre'+str(numlanceur)+'/niveau.txt')
    niveau_lanceur = int(file.read())
    file.close()
    print(niveau_lanceur)
    
    for i in listeattaque:
        if attaque == i.nom:
            puissance_attaque=i.puissance
            break
    
    att_spec = get_attspec(lanceur)
    def_spec = get_defspec(receveur)
    
    degats_infliges=int(((niveau_lanceur*2/5)*puissance_attaque*att_spec/50)/def_spec)
    print(lanceur+' Inflige '+str(degats_infliges)+' dégats à '+receveur)
    
degats('Griffe Acier',8,1,6,5)
