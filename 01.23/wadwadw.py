feladvany = "wdagadjakndwahfzo"
megfejtes = list("_" * len(feladvany))

elet = 100000

print(f"{''.join(megfejtes)}")

while True:
    print()
    tipp = input("Tipp: ")

    talalt = False
    for sorszam, betu in enumerate(feladvany):
        if betu == tipp:
            megfejtes[sorszam] = tipp
            talalt = True
    if talalt == False:
        elet -= 1

    print(f"{''.join(megfejtes)}")

    if ''.join(megfejtes) == feladvany:
        print(f"Helyes megoldas!")
        break

    if elet == 0:
        print(f"Sajnos vesztettel!")
        print(f"A helyes megfejtes: {feladvany}")
        break