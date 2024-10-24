import random
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
nummers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']

kaarten_1 = [f"{kleuren_1} {nummers_1}" for kleuren_1 in kleuren for nummers_1 in nummers] + ['joker', 'joker']

random.shuffle(kaarten_1)
weggehaald = [kaarten_1.pop(0) for i in range(7)]
for kaart in weggehaald:
    print(f"kaart: {kaart}")
print(f"\ndeck ({len(kaarten_1)} kaarten): {kaarten_1}")