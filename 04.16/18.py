import random
class lolhos:
    def __init__(self,az,nev,tip,stilus):
        self.az = az 
        self.nev = nev 
        self.tip = tip
        self.stilua = stilus
    
    def setnehezsegiszint(self,nehezsegifok):
        if nehezsegifok==1:
            self.nsz = "Easy"
        elif nehezsegifok==2:
            self.nsz = "Medium"
        else:
            self.nsz = "Hard"

    def setkepeseg(self):
        lehet = ["átokszórás","végítélet","halál","bájolás"]
        self.kepesseg = random.choice(lehet)

hosok = []
f = open("hosok.hsk","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split("|")
    hos1 = lolhos(adatok[0],adatok[1],adatok[2],int(adatok[3]))
    hos1.setnehezsegiszint(int(adatok[4]))
    hos1.setkepeseg()
    hosok.append(hos1)
    del hos1
f.close

i = open("hoseim.txt","w",encoding="utf-8")
for egyhos in hosok:
    i.write(f"Azonosító: {egyhos.az}\n")
    i.write(f"Hős neve: {egyhos.nev}\n")
    i.write(f"Nehézségi: {egyhos.nsz}\n")
    i.write(f"Képesség: {egyhos.kepeseg}\n")
    i.write(f"##########################\n")
i.close()