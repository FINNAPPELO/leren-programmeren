import random
kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

aantalinZak = int(input("Hoeveel M&M's wil je in een zak?: "))

zak_Ms = {}

for i in range(aantalinZak):
    kleur = random.choice(kleuren)
    if kleur in zak_Ms:
        zak_Ms[kleur] += 1
    else:
        zak_Ms[kleur] = 1

print(zak_Ms)