import os 
os.system("cls")


def paros_szamokat_kivlogato(bemenet_lista):
    paros_szamok = [szam for szam in bemenet_lista if szam % 2 == 0]
    return paros_szamok


bemenet_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eredmeny = paros_szamokat_kivlogato(bemenet_lista)

print("Bemeneti lista:", bemenet_lista)
print("Páros számok:", eredmeny)
