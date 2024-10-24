import random
kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
aantalinZak = int(input("Hoeveel M&M's wil je in een zak?: "))
zak_Ms = []
for i in range(aantalinZak):
    kleur = random.choice(kleuren)
    zak_Ms.append(kleur)
print(zak_Ms)