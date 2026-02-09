import random
import string

def genereer_wachtwoord():
    H = random.randint(2, 6)
    D = random.randint(4, 7)
    L = 24 - H - 3 - D

    wachtwoord = [None] * 24

    if random.choice([True, False]):
        wachtwoord[23] = str(random.randint(0, 9))
        D -= 1
    else:
        wachtwoord[23] = random.choice(string.ascii_uppercase)
        H -= 1

    speciale_tekens = ['@', '#', '$', '%', '&', '_', '?']
    speciale_plaats = random.sample(range(1, 23), 3)
    for plaats in speciale_plaats:
        wachtwoord[plaats] = random.choice(speciale_tekens)

    beschikbare_plaats_voor_cijfers = [i for i in range(3, 23) if wachtwoord[i] is None]
    cijfer_plaats = random.sample(beschikbare_plaats_voor_cijfers, D)
    for plaats in cijfer_plaats:
        wachtwoord[plaats] = str(random.randint(0, 9))

    beschikbare_plaats_voor_hoofd = [i for i in range(24) if wachtwoord[i] is None and i not in [11, 12, 23]]
    hoofd_plaats = random.sample(beschikbare_plaats_voor_hoofd, H)
    for plaats in hoofd_plaats:
        wachtwoord[plaats] = random.choice(string.ascii_uppercase)

    for i in range(24):
        if wachtwoord[i] is None:
            wachtwoord[i] = random.choice(string.ascii_lowercase)

    wachtwoord_string = ''.join(wachtwoord)
    return wachtwoord_string

print(genereer_wachtwoord())