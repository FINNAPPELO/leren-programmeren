from opdr_3 import verzamel_gegevens
def toon_gegevens():
    resultaten = verzamel_gegevens()
    for persoon in resultaten:
        stad = (persoon['city'])  
        naam = (persoon['name']) 
        leeftijd = int(persoon['age']) 

        if leeftijd >= 18:
            print(f"In {stad} woont {naam}, die al {(leeftijd)} jaar volwassen is")


        else:
            print(f"In {stad} woont {naam}, die nog niet volwassen is")

toon_gegevens()