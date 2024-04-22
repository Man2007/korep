import os
os.system("cls")

nev = input("adj meg egy pokemon nevet: ")
ero = input("Add meg az erő pontszámod: ")
ero = int(ero)
utesipontszam = ero/2*0.43
rugasipontszam = ero/3*0.9
print(f"A pokemon neve {nev}")
print(f"Ero. {ero}")
print(f"Rugas ->{rugasipontszam} pont, Utes ->{utesipontszam} pont")