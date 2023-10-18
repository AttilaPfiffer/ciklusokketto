''' kérj be két számot a felhasználótól
Írj eljátást
    szamok néven, (ciklusok.py)
    melynek a paramétere a felhasználó által megadott két szám
    és
    az eljárás kiírja a számokat ezen a két paraméter között.
 '''



szam1: int = int(input("Adjon meg egy számmot: "))
szam2: int = int(input("Adjon meg még 1 számot: "))

import ciklusok
ciklusok.szamok(szam1, szam2)
