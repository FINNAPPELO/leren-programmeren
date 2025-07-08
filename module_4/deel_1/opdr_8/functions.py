def is_prime(number:int) -> bool:
    #Controleert of het getal kleiner of gelijk is aan 1, want deze zijn geen priemgetallen.
    if number <= 1:
        return False
    
    #Getal 2 is een speciaal geval: het enige even priemgetal.
    if number == 2:
        return True
    
    #Alle andere even getallen (groter dan 2) zijn geen priemgetallen.
    if number % 2 == 0:
        return False
    
    #We checken alleen oneven delers tot de wortel van het getal.
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    #Als geen enkele deling nul opleverde, is het een priemgetal.
    return True



def priemgetallen_tot(eindgetal: int) -> list:
    priemgetallen = []

    for i in range(2, eindgetal + 1):
        if is_prime(i):
            priemgetallen.append(i)

    return priemgetallen


def eerste_priemgetallen(aantal: int) -> list:
    priemgetallen = []
    getal = 2

    while len(priemgetallen) < aantal:
        if is_prime(getal):
            priemgetallen.append(getal)
        getal += 1

    return priemgetallen


def priemgetallen_in_bereik(start: int, einde: int) -> list:
    priemgetallen = []

    for i in range(start, einde + 1):
        if is_prime(i):
            priemgetallen.append(i)

    return priemgetallen
