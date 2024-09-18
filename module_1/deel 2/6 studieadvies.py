from time import sleep
from studieadviestext import *

lang= int(input("hoeveel weeken studeert u al? "))
if lang <10:
    print(OPTIES)
    s1=int(input(COMPETENTIE_STELLING_1))
    print(OPTIES)
    s2=int(input(COMPETENTIE_STELLING_2))
    print(OPTIES)
    s3=int(input(COMPETENTIE_STELLING_3))
    print(OPTIES)
    s4=int(input(COMPETENTIE_STELLING_4))
    print(OPTIES)
    s5=int(input(COMPETENTIE_STELLING_5))
    print(OPTIES)
    s6=int(input(COMPETENTIE_STELLING_6))
    print(OPTIES)
    s7=int(input(COMPETENTIE_STELLING_7))
    punten = s1+s2+s3+s4+s5+s6+s7
    gemideld = punten/7
elif lang >= 10:
    print(OPTIES)
    s6=int(input(COMPETENTIE_STELLING_6))
    print(OPTIES)
    s7=int(input(COMPETENTIE_STELLING_7))
    gemideld = (s6 + s7) /2
for i in range (3):
    print("we zijn je advies aan het berekenen...")
    sleep(1)
print(COMPETENTIE_ADVIES_TITEL )
if gemideld  <= 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemideld <= 3:
     print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)