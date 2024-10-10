import random
kleuren_1 = ('orange','blauw','groen','bruin')
A_mm= int(input("hoeveel m&m's wil je aan de zak toevoegen ?  ")) 
zak_mm= [ ]
for i in range (A_mm):
    kleuren = random.choice(kleuren_1)
    zak_mm.append(kleuren)
print(zak_mm)