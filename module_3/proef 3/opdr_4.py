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
print("De lootjes zijn verdeeld! Alleen jij kunt zien wie je hebt door je naam in te voeren.")
print("Typ 'stop' om te stoppen.")
while True:
    naam = input("Voer je naam in om te zien wie je hebt (of typ 'stop' om te stoppen): ").strip().lower()
    if naam.lower() == "stop":
        
        print("Programma beëindigd.")
        break
    elif naam in verdeling:
        print(f"{naam}, jij hebt {verdeling[naam]}!")
    else:
        print("Naam niet gevonden. Controleer of je de juiste naam hebt ingevoerd.")
