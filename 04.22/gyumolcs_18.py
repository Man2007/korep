import random
class Fa:
    def __init__(self,fajnev,kerulet,telepulesnev,feljegyzesEv):
        self.fajnev = fajnev
        self.kerulet = kerulet
        self.telepulesnev = telepulesnev
        self.feljegyzesEv = feljegyzesEv
        self.kor = 0
        self.hatralevoIdo = 0

    def eltelIdo(self):
        self.kor = 2024-self.feljegyzesEv

    def becsles(self):
        szam = random.randint(10,100)
        return szam

falistaja = []

f = open("faforr.txt","r",encoding="utf-8")
for sor in f:
    sor =sor.strip()
    adatok = sor.split("\t")
    fa1 = Fa(adatok[0],int(adatok[1]),adatok[2],int(adatok[3]))
    fa1.eltelIdo()
    fa1.hatralevoIdo = fa1.becsles()
    falistaja.append(fa1)
    del fa1
f.close()

w = open("kimutatas.txt","w",encoding="utf-8")
for egyFa in faklistaja:
    w.write(f"Feljegyzés éeve: {egyFa.jeljegyzesEv}")
    w.write



    if egyFa
w.close