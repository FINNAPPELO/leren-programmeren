

PIZZA_GROOTTES = {
    "S": {"naam": "Klein", "prijs": 7.99, "grootte_cm": 20},
    "M": {"naam": "Middelgroot", "prijs": 10.99, "grootte_cm": 30},
    "L": {"naam": "Groot", "prijs": 13.99, "grootte_cm": 35},
    "XL": {"naam": "Extra groot", "prijs": 16.99, "grootte_cm": 40}
}

BELEGGINGEN = {
    "1": {"naam": "Mozzarella", "prijs": 0.50},
    "2": {"naam": "Pepperoni", "prijs": 1.00},
    "3": {"naam": "Champignons", "prijs": 0.75},
    "4": {"naam": "Uien", "prijs": 0.50},
    "5": {"naam": "Paprika", "prijs": 0.75},
    "6": {"naam": "Olijven", "prijs": 0.75},
    "7": {"naam": "Spek", "prijs": 1.25},
    "8": {"naam": "Ananas", "prijs": 0.50}
}


def toon_menu(items, titel):
    """Toon een genummerd menu van items."""
    print(f"\n{titel}")
    print("-" * 40)
    for key, value in items.items():
        if isinstance(value, dict) and "naam" in value:
            print(f"  {key}: {value['naam']} (€{value['prijs']:.2f})")
        else:
            print(f"  {key}: {value}")
    print("-" * 40)


def verkrijg_geldige_invoer(prompt, geldige_opties):
    """Ontvang en valideer gebruikersinvoer tegen geldige opties."""
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in geldige_opties:
            return user_input
        print(f" Ongeldige invoer. Kies uit: {', '.join(geldige_opties)}")


def kies_pizza_grootte():
    """Laat de gebruiker een pizzagrootte kiezen."""
    toon_menu(PIZZA_GROOTTES, " KIES PIZZAGROOTTE")
    grootte = verkrijg_geldige_invoer("Kies een grootte (S/M/L/XL): ", PIZZA_GROOTTES.keys())
    return grootte


def kies_beleggingen():
    """Laat de gebruiker meerdere beleggingen kiezen."""
    toon_menu(BELEGGINGEN, " KIES BELEGGINGEN (Optioneel)")
    geselecteerde_beleggingen = []
    
    while True:
        keuze = input("Voer beleggingsnummer in (of Enter om te stoppen): ").strip()
        
        if not keuze:  
            break
        
        if keuze in BELEGGINGEN:
            beleg_naam = BELEGGINGEN[keuze]["naam"]
            if keuze not in geselecteerde_beleggingen:
                geselecteerde_beleggingen.append(keuze)
                print(f"Toegevoegd: {beleg_naam}")
            else:
                print(f"{beleg_naam} al geselecteerd")
        else:
            print("Ongeldig beleggingsnummer. Probeer opnieuw.")
    
    return geselecteerde_beleggingen


def vraag_aantal():
    """Vraag het aantal pizza's."""
    while True:
        try:
            aantal = int(input("\nHoeveel pizza's wilt u? "))
            if aantal > 0:
                return aantal
            print("Voer een getal groter dan 0 in")
        except ValueError:
            print("Voer een geldig getal in")


def bereken_pizza_prijs(grootte, beleggingen):
    """Bereken de prijs van één pizza."""
    pizza_prijs = PIZZA_GROOTTES[grootte]["prijs"]
    beleg_prijs = sum(BELEGGINGEN[beleg]["prijs"] for beleg in beleggingen)
    return pizza_prijs + beleg_prijs


def toon_bestelling_samenvatting(grootte, beleggingen, aantal, totaal_prijs):
    """Toon een geformatteerde samenvatting van de bestelling."""
    print("\n" + "=" * 50)
    print(" BESTELLINGSSAMENVATTING")
    print("=" * 50)
    
    grootte_naam = PIZZA_GROOTTES[grootte]["naam"]
    pizza_prijs = PIZZA_GROOTTES[grootte]["prijs"]
    
    print(f"\nPizzagrootte: {grootte_naam} - €{pizza_prijs:.2f}")
    
    if beleggingen:
        print("Beleggingen:")
        totaal_beleg = 0
        for beleg in beleggingen:
            beleg_naam = BELEGGINGEN[beleg]["naam"]
            beleg_prijs = BELEGGINGEN[beleg]["prijs"]
            print(f"  - {beleg_naam} - €{beleg_prijs:.2f}")
            totaal_beleg += beleg_prijs
        print(f"  Totaal beleg: €{totaal_beleg:.2f}")
    else:
        print("Beleggingen: Geen")
    
    prijs_per_pizza = bereken_pizza_prijs(grootte, beleggingen)
    print(f"\nPrijs per pizza: €{prijs_per_pizza:.2f}")
    print(f"Aantal: {aantal}")
    print(f"\n{'TOTALE PRIJS':<30} €{totaal_prijs:.2f}")
    print("=" * 50)


def start_rekenmachine():
    """Hoofdlus van de rekenmachine."""
    print("\n" + "=" * 50)
    print(" WELKOM BIJ DE ULTIEME PIZZAREKENMACHINE ")
    print("=" * 50)
    
    bestellingen = []
    
    while True:
        # Verkrijg bestelgegevens
        grootte = kies_pizza_grootte()
        beleggingen = kies_beleggingen()
        aantal = vraag_aantal()
        
        # Bereken totalen
        prijs_per_pizza = bereken_pizza_prijs(grootte, beleggingen)
        totaal_bestelling = prijs_per_pizza * aantal
        
        # Sla bestelling op
        bestelling = {
            "grootte": grootte,
            "beleggingen": beleggingen,
            "aantal": aantal,
            "prijs_per_pizza": prijs_per_pizza,
            "totaal_bestelling": totaal_bestelling
        }
        bestellingen.append(bestelling)
        
        # Toon samenvatting
        toon_bestelling_samenvatting(grootte, beleggingen, aantal, totaal_bestelling)
        
        # Vraag of nog een bestelling
        nog = input("\nWilt u nog een bestelling toevoegen? (ja/nee): ").strip().lower()
        if nog not in ("ja", "j", "yes", "y"):
            break
    
    # Toon eindoverzicht
    if bestellingen:
        toon_eindoverzicht(bestellingen)


def toon_eindoverzicht(bestellingen):
    """Toon samenvatting van alle bestellingen."""
    print("\n" + "=" * 50)
    print(" EINDOVERZICHT - ALLE BESTELLINGEN")
    print("=" * 50)
    
    totaal_algemeen = 0
    
    for i, bestelling in enumerate(bestellingen, 1):
        grootte_naam = PIZZA_GROOTTES[bestelling["grootte"]]["naam"]
        print(f"\nBestelling {i}:")
        print(f"  Grootte: {grootte_naam} × {bestelling['aantal']}")
        print(f"  Totaal: €{bestelling['totaal_bestelling']:.2f}")
        totaal_algemeen += bestelling['totaal_bestelling']
    
    print("\n" + "-" * 50)
    print(f"{'EINDTOTAAL':<30} €{totaal_algemeen:.2f}")
    print("=" * 50)
    print("\nBedankt voor uw bestelling!")


if __name__ == "__main__":
    start_rekenmachine()
