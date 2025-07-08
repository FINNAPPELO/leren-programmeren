from opdr_3 import verzamel_gegevens
from termcolor import colored

def toon_gegevens():
    resultaten = verzamel_gegevens()
    for persoon in resultaten:
        stad = colored(persoon['city'], 'yellow')  
        naam = colored(persoon['name'], 'green') 
        leeftijd = int(persoon['age']) 

        if leeftijd >= 18:
            print(f"In {stad} woont {naam}, die {colored('al', 'red')} {colored(leeftijd - 18, 'red')} {colored('jaar', 'red')} volwassen is")


        else:
            print(f"In {stad} woont {naam}, die {colored('nog niet', 'red')} volwassen is")
toon_gegevens()