import random
deelnemers = []
while len(deelnemers) < 3:
    naam = input("Voer een naam in: ")
    if naam not in deelnemers:
        deelnemers.append(naam)
    else:
        print("Deze naam is al ingevoerd.")
while True:
    antwoord = input("Wil je nog een naam invoeren? (ja/nee): ").strip().lower()
    if antwoord == "ja":
        if len(deelnemers) < 4:
            naam = input("Voer een naam in: ")
            if naam not in deelnemers:
                deelnemers.append(naam)
            else:
                print("Deze naam is al ingevoerd.")
        else:
            print("Er zijn al 4 deelnemers, er kunnen geen extra namen meer worden toegevoegd.")
            break
    elif antwoord == "nee":
        break
    else:
        print("Ongeldig antwoord. Typ 'ja' of 'nee'.")
lootjes = deelnemers[:]
random.shuffle(lootjes)
verdeling = {}
for deelnemer in deelnemers:
    while lootjes[0] == deelnemer:
        random.shuffle(lootjes)
    verdeling[deelnemer] = lootjes.pop(0)
print("De verdeling van de lootjes:")
for deelnemer, lootje in verdeling.items():
    print(f"{deelnemer} heeft {lootje} getrokken.")
