from time import *
import random

score = 0
rondes = 20
raadgetal = 0
geheim_getal = 0
goed_geraden = "nee"
i = 0

def streeplijn():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def kies_getal():
    global geheim_getal
    geheim_getal = random.randint(1, 1000)
    return geheim_getal

streeplijn()
print("Welkom bij het spel: raad eens")
print("Gemaakt door:Finn Appelo.")
def einde_game(i):
    streeplijn()
    print(f"Helaas, na {i} pogingen mocht je niet meer verder raden... Erg jammer, probeer het later nog eens!")
    print("Bedankt voor het spelen.")
    exit()
    
def getalRaden():
    kies_getal()
    global rondes, score, geheim_getal
    for i in range(1, (rondes + 1)):
        while True:
            try:
                print(geheim_getal)
                raadgetal = int(input(f"Je {i}e poging om het getal te raden gaat zijn: "))
                break 
            except ValueError:
                print("Dat is geen geldig getal, probeer het opnieuw.")
        isHetGoedeGetal(raadgetal, i)
        if goed_geraden == "nee":
            if raadgetal < geheim_getal:
                print("Het getal ligt hoger")
            elif raadgetal > geheim_getal:
                print("Het getal ligt lager")
        if i == 20:
            print("Helaas, dat was je laatste poging...")
            einde_game(i)

def isHetGoedeGetal(raadgetal, i):
    global geheim_getal
    if raadgetal == geheim_getal:
        print(f"Je hebt het getal geraden! Het was inderdaad {raadgetal}...")
        score +1
        wilNogEenKeer = input("Wil je nog een keer? (ja/nee): ").strip().lower()
        if wilNogEenKeer == "ja":
            streeplijn()
            print("Daar gaan we nog een keer!")
            getalRaden()
        else:
            einde_game(i)
    else:
        goed_geraden = "nee"
        rondes = i
        return goed_geraden, rondes
getalRaden()
