import os 
os.system("cls")

def alapmuveletek(szam1, szam2, muvelet):
    if muvelet == 'osszeadas':
        eredmeny = szam1 + szam2
    elif muvelet == 'kivonas':
        eredmeny = szam1 - szam2
    elif muvelet == 'szorzas':
        eredmeny = szam1 * szam2
    elif muvelet == 'osztas':
        if szam2 != 0:
            eredmeny = szam1 / szam2
        else:
            eredmeny = 'Hiba: nullával való osztás!'
    else:
        eredmeny = 'Hiba: Ismeretlen művelet!'
    
    return eredmeny


eredmeny_osszeadas = alapmuveletek(5, 3, 'osszeadas')
eredmeny_kivonas = alapmuveletek(5, 3, 'kivonas')
eredmeny_szorzas = alapmuveletek(5, 3, 'szorzas')
eredmeny_osztas = alapmuveletek(5, 3, 'osztas')

print(f'Osszeadas eredmenye: {eredmeny_osszeadas}')
print(f'Kivonas eredmenye: {eredmeny_kivonas}')
print(f'Szorzas eredmenye: {eredmeny_szorzas}')
print(f'Osztas eredmenye: {eredmeny_osztas}')
