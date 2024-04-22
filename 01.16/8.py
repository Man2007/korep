import os 
os.system

evek = []
for x in range(5):
    evszam = input("Adj meg egy évszámot: ")
    evszam = int(evszam)
    evek.append(evszam)
kis = min(evek)
nagy = max(evek)
print(evszam)    
print(kis)
print(nagy)
