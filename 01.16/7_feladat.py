import os 
os.system


szamok = []
stop = input("adja meg a stopolo számot: ")
while True:
    szam = input("irja be egy szánot: ")    
    szam = int(szam)
    if szam == stop:
        break
    if szam not in szamok:
        szamok.append(szam)

print(szamok)