import os 
os.system("cls")

utaslista = []

while True:
    nev = input("Add meg az utas nevét: ")
    if nev == "":
        break
    ev = input("Adja meg a szuletési evet: ")
    ev = int(ev)
    km = input("adja meg az utazot kilometerek szamat: ")
    km = int(km)
    utas = {}
    utas['nev'] = nev 
    utas{'ev'} =  ev 
    utas['km'] =  km 
    utaslista.append(utas)
    
print(utaslista)