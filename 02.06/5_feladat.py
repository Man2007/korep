import os
os.system("cls")

def pokemonrogzites():
    pokemonok = []
    while True:
        pokemon = input("Add meg az állat nevét: ")
        if pokemon == "":
            break
        pokemonok.append(pokemon)
    return pokemonok

def kezdoBetuSzamolas(pokemontLista): 
    db = len(pokemontLista)
    b=[]
    c=[]
    mm = []
    for egypokemon in pokemontLista:
        if egypokemon.startswith("a") == True:
            b.append(egypokemon)
        elif egypokemon.startswith("b") == True:
            c.append(egypokemon)
        else:
            mm.append(egypokemon)

    bBb = (b)
    cDc = (c)
    mmb = (mm)

    print(f"Összesen: {db} db")
    print(f"b betűvel: {bBb}")
    print(f"c betűvel: {cDc}")
    print(f"minden más: {mmb}")


l = pokemonrogzites()
kezdoBetuSzamolas(l)