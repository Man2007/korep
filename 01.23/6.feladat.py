import os 
os.system("cls")

import random

def veletlen_szamok_lista(darab, minimum, maximum):
    szamok_lista = [random.randint(minimum, maximum) for _ in range(darab)]
    return szamok_lista


darab = 5
minimum = 1
maximum = 10

veletlen_lista = veletlen_szamok_lista(darab, minimum, maximum)
print(f'Véletlen számok lista: {veletlen_lista}')
