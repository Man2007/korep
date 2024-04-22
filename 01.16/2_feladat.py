import os 
os.system

szam = input("adj meg egy számot: ")
szam = int(szam)


while szam>0:
    if szam%3==0:
        print(szam)
    szam=szam-1