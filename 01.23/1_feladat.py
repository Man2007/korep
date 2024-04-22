import os 
os.system("cls")

zenelista = []

while True:
    eloado = input("Add meg az eloado nevét: ")
    if eloado == "":
        break
    cim = input("Add meg az szam cimet: ")
    hossz = input("Add meg a szám hosszat: ")
    hossz = int(hossz)
    zene = {}
    zene['eloado'] = eloado
    zene{'cim'} = cim
    zene['hossz'] = hossz
    zenelista.append(zene)

print(zenelista)