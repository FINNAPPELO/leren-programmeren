import time, string
import random

def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    
    upper_count = sum(1 for L in ww if L in string.ascii_uppercase)
    if not 1 < upper_count < 7:
        print('aantal hoofdletters klopt niet!')
        return False
    
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    
    lower_count = sum(1 for L in ww if L in string.ascii_lowercase)
    if lower_count < 8:
        print('te weinig kleine letters')
        return False
    
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    
    special_count = sum(1 for L in ww if L in '@#$%&_?')
    if special_count != 3:
        print('te weinig specials')
        return False
    
    if ww[0] in '@#$%&_?' or ww[-1] in '@#$%&_?':
        print('special op end')
        return False
    digit_count = sum(1 for L in ww if L.isdigit())
    if not 3 < digit_count < 8:
        print('te weinig getallen')
        return False
    
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True

def get_wachtwoord():
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
    


# plaats hier de code om minimaal 500 wachtwoorden te testen.
for _ in range(500):
    ww = get_wachtwoord()
    if not test_wachtwoord(ww):
        print(ww)