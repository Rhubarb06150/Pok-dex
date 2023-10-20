class Zones:
    
    def __init__(self,rawnom,nom):
        self.rawnom=rawnom
        self.nom=nom
        
route1=Zones(['route 1','route1','Route1'],'Route 1')
route2=Zones(['route 2','route2','Route2'],'Route 2')
route3=Zones(['route 3','route3','Route3'],'Route 3')
route4=Zones(['route 4','route4','Route5'],'Route 4')
route5=Zones(['route 5','route5','Route5'],'Route 5')
route6=Zones(['route 6','route6','Route6'],'Route 6')
route7=Zones(['route 7','route7','Route7'],'Route 7')
route8=Zones(['route 8','route8','Route8'],'Route 8')
route9=Zones(['route 9','route9','Route9'],'Route 9')
route10=Zones(['route 10','route10','Route10'],'Route 10')
route11=Zones(['route 11','route11','Route11'],'Route 11')
route12=Zones(['route 12','route12','Route12'],'Route 12')
route13=Zones(['route 13','route13','Route13'],'Route 13')
route14=Zones(['route 14','route14','Route14'],'Route 14')
route15=Zones(['route 15','route15','Route15'],'Route 15')
route16=Zones(['route 16','route16','Route16'],'Route 16')
route17=Zones(['route 17','route17','Route17'],'Route 17')
route18=Zones(['route 18','route18','Route18'],'Route 18')

listezone=[]

listezone.append(Zones(['route 1','route1','Route1'],'Route 1'))
listezone.append(Zones(['route 2','route2','Route2'],'Route 2'))
listezone.append(Zones(['route 3','route3','Route3'],'Route 3'))
listezone.append(Zones(['route 4','route4','Route5'],'Route 4'))
listezone.append(Zones(['route 5','route5','Route5'],'Route 5'))
listezone.append(Zones(['route 6','route6','Route6'],'Route 6'))
listezone.append(Zones(['route 7','route7','Route7'],'Route 7'))
listezone.append(Zones(['route 8','route8','Route8'],'Route 8'))
listezone.append(Zones(['route 9','route9','Route9'],'Route 9'))
listezone.append(Zones(['route 10','route10','Route10'],'Route 10'))
listezone.append(Zones(['route 11','route11','Route11'],'Route 11'))
listezone.append(Zones(['route 12','route12','Route12'],'Route 12'))
listezone.append(Zones(['route 13','route13','Route13'],'Route 13'))
listezone.append(Zones(['route 14','route14','Route14'],'Route 14'))
listezone.append(Zones(['route 15','route15','Route15'],'Route 15'))
listezone.append(Zones(['route 16','route16','Route16'],'Route 16'))
listezone.append(Zones(['route 17','route17','Route17'],'Route 17'))
listezone.append(Zones(['route 18','route18','Route18'],'Route 18'))

listenomzone=[]
for i in listezone:
    listenomzone.append(i.nom)