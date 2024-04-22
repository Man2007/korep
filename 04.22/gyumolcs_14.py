def gyumolcsGeneralas():
    gyumolcsok = []
    while True:
        gyumolcs = input("")
        if not gyumolcs:
            break
        gyumolcsok.append(gyumolcs)
    return gyumolcsok

def kimutatas(fruits):
    db = len(fruits)
    print(f"Gyümölcsök száma a listában: {db} db")
    dbm = 0 
    for egyGyumolcs in fruits:
        if egyGyumolcs.find("m")>-1:
            dbm += 1
    print(f"Az m karakteret tartalmazo gyumolcsnevek szama: {dbm} db")


m = gyumolcsGeneralas()
kimutatas(m)