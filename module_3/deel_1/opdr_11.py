from fruitmandd import fruitmand
kleuren = []
for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])
while True:
    kleur = input(f"Kies een kleur uit de beschikbare kleuren: {', '.join(kleuren)}: ").lower()
    if kleur in kleuren:
        break
    else:
        print(f"De kleur {kleur} zit er niet in de fruitmand.")
ronde = 0
niet_ronde = 0
for fruit in fruitmand:
    if fruit['color'] == kleur:
        if fruit['round']:
            ronde += 1
        else:
            niet_ronde += 1
verschil = abs(ronde - niet_ronde)
if ronde > niet_ronde:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
elif ronde < niet_ronde:
    print(f"Er zijn {verschil} minder ronde vruchten dan iet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn {ronde} ronde vruchten en {ronde} nie ronde vruchten in de kleur {kleur}")
