import os 
os.system

eletkorok = []

while True:
    eletkor = input("irja be az életkorát: ")    
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    eletkorok.append(eletkor)
print(eletkorok)
