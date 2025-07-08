# Controleert of een gegeven getal even is
def is_even(getal: int) -> bool:
    return getal % 2 == 0  # Controleer of het getal deelbaar is door 2 zonder rest

# Neemt een zin en keert de volgorde van de woorden om
def omgekeerde_zin(zin: str) -> str:
    woorden = zin.split()  # Splits de zin in een lijst van woorden
    omgekeerde_woorden = woorden[::-1]  # Keer de volgorde van de woordenlijst om
    nieuwe_zin = ' '.join(omgekeerde_woorden)  # Combineer de omgekeerde woordenlijst terug tot een string
    return nieuwe_zin

# Telt het aantal unieke karakters in een tekst
def unieke_karakters_tellen(tekst: str) -> int:
    unieke_karakters = set(tekst)  # Maak een verzameling (set) van unieke karakters uit de tekst
    aantal_unieke_karakters = len(unieke_karakters)  # Tel het aantal unieke karakters in de set
    return aantal_unieke_karakters

# Berekent de gemiddelde lengte van woorden in een zin
def gemiddelde_woordlengte(zin: str) -> float:
    woorden = zin.split()  # Splits de zin in een lijst van woorden
    totale_lengte = 0  # Variabele om de totale lengte van alle woorden bij te houden
    for woord in woorden:
        totale_lengte += len(woord)  # Voeg de lengte van elk woord toe aan de totale lengte
    gemiddelde_lengte = totale_lengte / len(woorden)  # Bereken de gemiddelde lengte door de totale lengte te delen door het aantal woorden
    return gemiddelde_lengte

# Print een vermenigvuldigingstabel voor een gegeven getal tot een bepaalde limiet
def vermenigvuldigingstabel(getal: int, limiet: int = 10) -> None:
    for factor in range(1, limiet + 1):  # Loop door elke factor van 1 tot en met de limiet
        product = factor * getal  # Bereken het product van het getal en de huidige factor
        print(f'{factor} x {getal} = {product}')  # Print de huidige regel van de vermenigvuldigingstabel
