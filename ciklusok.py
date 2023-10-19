import math

def szamok(szam1: float, szam2: float):
    if szam1 == szam2:
        print("A két szám egyenlő")
        return
    
    if szam1 > szam2:
        csere: float = szam1
        szam1 = szam2
        szam2 = csere
    
    i: int = math.ceil(szam1)

    while szam2 > i:
        if (i == szam2 - 1):
            print(i)
        else:    
            print(i, end = ", ")
        i += 1