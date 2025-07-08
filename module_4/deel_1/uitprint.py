from opdr_3 import verzamel_gegevens

resultaten = verzamel_gegevens()

for persoon in resultaten:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar  ")
