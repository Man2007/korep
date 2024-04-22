import os 
os.system

zoldsegek = []
szam = input("Hány zoldseget szeretnél: ")
szam = int(szam)

for x in range(szam): 
    zoldseg = input("Add meg a zoldseg nevét: ")
    zoldsegek.append(zoldseg)

print(zoldsegek)


