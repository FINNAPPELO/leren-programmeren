import time, math
import random
from random import randint
player_attack = 1
player_defense = 0
player_health = 3
sleutel =0
operators = ["+","-","*"]

oparator = random.choice(operators)
som_1  = randint(10, 25)
som_2 = randint(-5,75)
if oparator == '+': 
    result = som_1 + som_2
elif oparator == '-':
    result = som_1 - som_2
else:
    result  = som_1 * som_2


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(2)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {som_1} {oparator} {som_2} =?')
antwoord = int(input('Wat toest je in? '))

if antwoord == result:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel=1
else:
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(2)

# === [kamer 3] === #
defence = ["schild","zwaard"]
defence_item = random.choice(defence)

if defence_item == 'schild':
    player_defense += 1
else:
    player_attack += 2


print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {defence_item}.')
print(f'Je pakt het {defence_item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(2)

# === [kamer 4] === #
zombie_attack = randint(-30,7)
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {defence_item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)


    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        player_health1=player_health-zombie_hit_damage
        print(f'Je health is nu {player_health1}.')

    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(2)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print(' ')
if sleutel==1:
    print('Je pakt de sleutel uit je zak en steekt hem in het slot')
    print('Je draait de sleutel om en de kist opent zich.')
    print(' ')
    print('je wint het spel')
else:
    print("je hebt geen sleutel")
    print('dus je kan de kist niet openen')
    print('')
    print('je hebt het spel verlooren ')