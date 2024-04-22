import os 
os.system("cls")

def eldontes(szam):
    if szam>0:
        print("Pozitiv")
    elif szam<0:
        print("negativ")
    else:
        print("nulla")

eldontes(25)
eldontes(32)
eldontes(-18)
eldontes(0)