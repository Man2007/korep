import os
os.system("cls")

szel = input("Add meg a szoba szelesseget: ")
szel = int(szel)
hossz = input("add meg a szoba hosszat: ")
hossz = int(hossz)
burk = input("Add meg a burkolas arat: ")
burk = int(burk)
terulet = szel*hossz
koltseg = terulet*burk*1.1

print(f"A szoba {terulet}m2, burkolasi költseg: {koltseg} Ft")
