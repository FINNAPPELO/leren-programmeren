PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

def bouncer_program():
    print("Welkom bij het evenement!")
    
    leeftijd = int(input("Hoe oud ben je? "))
    
    if leeftijd < 18:
        print("Sorry, je mag niet naar binnen. Probeer het in", 18 - leeftijd, "jaar nog eens.")
        return
    naam = input("Wat is je naam? ")
    is_vip = input("Ben je een VIP? (ja/nee) ").lower() == "ja"
    
    if leeftijd >= 21:
        bandje_kleur = "blauw"
    else:
        bandje_kleur = "rood"
    
    if leeftijd >= 21 or is_vip:
        print(f"Je krijgt van mij een {bandje_kleur} bandje.")
    else:
        print("Je krijgt van mij een stempel.")
    
    drinken = input("Wat wil je drinken? (Cola/Bier/Champagne/Anders) ").lower()
    
    if drinken == "cola":
        if bandje_kleur == "blauw" or 'rood':
            print("Alsjeblieft, complimenten van het huis!")
        else:
            print("Alsjeblieft, je cola kost 1,80 euro.")
    elif drinken == "bier":
        if leeftijd < 21:
            print("Sorry, je mag geen alcohol bestellen onder de 21.")
        elif bandje_kleur == "blauw" or is_vip:
            print(f"Alsjeblieft, je bier, dat is dan €{PRIJS_BIER}.")
        else:
            print("Sorry, je hebt geen geldig bandje of stempel.")
    elif drinken == "champagne":
        if not is_vip:
            print("Sorry, alleen VIP's mogen champagne bestellen.")
        else:
            print(f"Alsjeblieft, je champagne, dat is dan €{PRIJS_CHAMPAGNE}.")
    else:
        print("Sorry, geen idee wat je bedoelt. Hier een glaasje water.")
    print("Einde programma.")
bouncer_program()
