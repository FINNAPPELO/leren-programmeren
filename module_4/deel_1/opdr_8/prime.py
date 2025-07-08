from functions import priemgetallen_tot_en_met, eerste_n_priemgetallen, priemgetallen_tussen

def start_priemgetallen_programma():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Welke functie wil je gebruiken?")
    print("1: Alle priemgetallen tot en met een getal")
    print("2: Een aantal priemgetallen")
    print("3: Priemgetallen tussen twee getallen")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    keuze = input("Voer een nummer in (1-3): ")

    if keuze == "1":
        getal = int(input("Tot en met welk getal? "))
        resultaat = priemgetallen_tot_en_met(getal)

    elif keuze == "2":
        aantal = int(input("Hoeveel priemgetallen wil je? "))
        resultaat = eerste_n_priemgetallen(aantal)

    elif keuze == "3":
        start = int(input("Van welk getal? "))
        einde = int(input("Tot welk getal? "))
        resultaat = priemgetallen_tussen(start, einde)


    else:
        print("Ongeldige keuze.")
        return

    if resultaat:
        print("Resultaat:", resultaat)
    else:
        print("Geen priemgetallen gevonden.")

start_priemgetallen_programma()
