import os 
os.system("cls")



koleszosok = []

while len(koleszosok <  10):
    nev = input("Add meg a nevét: ")
    tavolsag = input("Add meg a távolságod: ")
    tavolsag = int(tavolsag)
    atlag = input("Add meg az atlagot: ")
    atlag = float(atlag)
    if atlag>2.7 and tavolsag>=50:
        koleszos = {}
        koleszos['nev'] = nev 
        koleszos['km'] = tavolsag
        koleszos['atlag'] = atlag
        koleszosok.append(koleszos)
        print("A diak rogzitese megtortent")
        maradt -= 1 
        print(f"Szabad helyek szama: {maradt")


