''' kérj be két számot a felhasználótól
Írj eljátást
    szamok néven, (ciklusok.py)
    melynek a paramétere a felhasználó által megadott két szám
    és
    az eljárás kiírja a számokat ezen a két paraméter között.
 '''

import ciklusok

szam1: int = int(input("Adjon meg egy számmot: "))

szam2: int = int(input("Adjon meg még 1 számot: "))
"""a felhasználó csak olyan szam2-t tudjon megadni ami nagyobb mint a szam1"""
while (szam1 >= szam2):
    print("szam2-nek nagyobbnak kell lennie mint a szam1-nek")
    szam2: int = int(input(f"Adj {szam1}-nél nagyobbat!"))



ciklusok.szamok(szam1, szam2)
