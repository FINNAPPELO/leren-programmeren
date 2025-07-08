def vraag_naam_en_leeftijd() -> dict:
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    woonplaats = input("Wat is je woonplaats? ")
    return {"name": naam, "age": leeftijd, "city": woonplaats}

def verzamel_gegevens() -> list:
    gegevens = []
    while True:
        keuze = input("Toets enter om door te gaan of stop om te printen: ").lower()
        if keuze == "stop":
            break
        gegevens.append(vraag_naam_en_leeftijd())
    return gegevens
    return gegevens
resultaten = verzamel_gegevens()

for persoon in resultaten:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar  ")