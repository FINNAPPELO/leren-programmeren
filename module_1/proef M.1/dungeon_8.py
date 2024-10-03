import time, math
import random
from random import randint
player_attack = 1
player_defense = 0
player_health = 3
sleutelS=0
k3_k8=8
ruby = 0
operators = ["+","-","*"]
item=0
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
time.sleep(3)
# === [kamer 7] === #
print('je doet de deur open....')
ruby_j =randint(1,10)
if ruby_j >1:
    ruby+=1
    print('je vind een ruby op de grond van de kamer.')
    print("je neemt de ruby mee ")
    print(' ')
else:
    print('')
print ('je wilt de deur openmaken maar dan zie aan de rechterkant nog een deur ')
kr7=input('welke deur wil je in rechtdoor of naar rechts?  ')
kr7.lower
if kr7  == 'rechtdoor':

    print(' ')
    time.sleep(3)
    # === [kamer 2] === #
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print(f'Daarboven zie je een som staan {som_1} {oparator} {som_2} =?')
    antwoord = int(input('Wat toest je in? '))

    if antwoord == result:
        print('Het stadbeeld laat een ruby vallen en je pakt het op')
        ruby+=1
    else:
        print('Er gebeurt niets....')

    print('Je ziet twee deuren achter het standbeeld.')
    print('')
    time.sleep(3)
    nr_kamer=int(input("wil je kamer 8 of kamer 6 in  gaan? type 8 of 6? "))
    if nr_kamer == 6:
        print('je hebt kamer 6 gekozen ')
        time.sleep(3)
        # === [kamer 6] === #
        zombie_attack = randint(-30,7)
        zombie_defense = 0
        zombie_health = 2
        print(f'Dapper loop je de kamer binnen.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage = (zombie_attack - player_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
            k3_k8=int(input('welke kamer wil je naartoe kamer 3 of 8? 3 of 8 '))
        else:
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
            player_hit_damage = (player_attack - zombie_defense)
            player_attack_amount = math.ceil(zombie_health / player_hit_damage)


            if player_attack_amount < zombie_attack_amount:
                print(f'In {player_attack_amount} rondes versla je de zombie.')
                player_health1=player_health-zombie_hit_damage
                print(f'Je health is nu {player_health1}.')
                k3_k8=int(input('welke kamer wil je naartoe kamer 3 of 8? 3 of 8  '))

            else:
                print('Helaas is de zombie te sterk voor je.')
                print('Game over.')
                exit()
        print('')
        time.sleep(3)
if  k3_k8 == 8:
# === [kamer 8] === #
        print(' ')
        print('je komt een lannge kamer binnen  ')
        print('in het miden van de kamer staat een gokkast')
        print('')
        print("de gok kast werkt als volgt er worden 2 dobbelstenen gegooit mat allebij 6 zijden ")
        print('als de dobbelstenen in totaal hooger als 7 zijn dan verdubel jij je rubys ')
        print('aleen als ze laager zijn als 7 dan verlies jij 1 health ')
        print('als die gelijk is aan 7 dan krijg je 1 ruby en 4 health ')
        goken_1= input("wil je gokken ja of nee? ")
        goken_1.lower
        while goken_1 ==  "ja":
            if  goken_1 == "ja":
                getal_gokken1 =randint(0,6)
                getal_gokken2 =randint(0,6) 
                gokken= getal_gokken1+getal_gokken2
                if  gokken > 7:
                    print(f'je hebt {gokken} gegooid en hebt je rubys verdubbeld')
                    ruby+=ruby
                    print(f'aantal rubbys  {ruby}')
                    print(' ')
                elif  gokken < 7:
                    print(f'je hebt {gokken} gegooid  en hebt 1 health verloren')
                    player_health-=1
                    if player_health==0:
                        print('al je  health is verdwenen je bent af')
                        print('game over')
                        exit()
                    else:
                        print(f'je  health is nu {player_health}')
                        print(' ')

                else:
                    print(f'je hebt {gokken} gegooid dus je krijgt  1 ruby en 4 health')
                    player_health+=4
                    ruby+=1
                    print(' ')
                goken_1=input('wil je nog een keer gokken ja of nee ?  ')
        time.sleep(3)
        k3_k9=int(input( 'je hebt weer 2 opties wil je naar kamer 3 of wil je naar kamer 9    3 of 9'))
        # === [kamer 9] === #
        if k3_k9 == 9:
            print(' ')
            print('je loopt de volgende kamer in maar deze kamer is vervloekt ')
            print('je krijgt of 1 defense  of 2 health als je deze kamer inloopt ')
            print(' ')
            kr_9 =randint(1,2)
            if kr_9  == 1:
                player_defense +=1
                print('je hebt 1 defense gekregen')
            else:
                player_health +=2
                print("je hebt 2 health gekregen  ")
                print(' ')
                 # === [kamer 3] === #
print(' ')
time.sleep(3)
print('Je duwt de deur open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een merchant met een schild een zwaard en een sleutel.')

print('zwaard == 1 ruby')
print('schild == 1 ruby')
print('sleutel == 1 ruby')
print(f'aantal  rubbys {ruby}')
time.sleep(3)
print(' ')
if ruby >= 1:
    kopen_1=input('wil je iets kopen van de merchant  ja of nee ? ')
    kopen_1.lower
    if kopen_1 =='ja':
        print(" ")
        zwaard=input('wil je een zwaard kopen  ja of nee ? ')
        zwaard.lower
        if  zwaard == 'ja':
            print('je hebt een zwaard gekocht')
            player_attack+=2
            print(f'je hebt nu {ruby} rubys')
            item+=1
            ruby-=1
            print(' ')
        else: 
            print('je hebt geen zwaard gekocht')
        if ruby>=1:
            schild=input('wil je een schild kopen  ja of nee ? ')
            schild.lower
            if schild == 'ja':
                print("je  hebt een schild gekocht")
                player_defense+=2
                print(f'je  hebt nu {ruby} rubys')
                item+=1
                ruby-=1
                print(' ')
            else:
                print('je hebt geen schild gekocht')
            if ruby >=1:
                sleutel=input('wil je een sleutel kopen  ja of nee ?')
                sleutel.lower
                if sleutel == 'ja':
                    print('je hebt een sleutel gekocht')
                    ruby-=1
                    print(f'je hebt nu {ruby} rubys')
                    sleutel=1
                    item+=1  
                    print(' ') 
                else:
                    print("je hebt geen sleutel gekocht")  
            else:
                print("je hebt geen rubys om iets te kopen")
        else:
            print('je hebt niet genog rubys voor nog iets ')
    else:
        print('je hebt niks gekocht ')
else:
    print('je hebt niet genoeg rubys om iets te kopen ')
if item >=2:
    item= 'items'
else:
    item= 'item'
# === [kamer 4] === #
beast_attack = 2
beast_defense = 0
beast_health = 3
time.sleep(3)
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een beast aan.')

beast_hit_damage = (beast_attack - player_defense)
if beast_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de beast, hij kan je geen schade doen.')
else:
    beast_attack_amount = math.ceil(player_health / beast_hit_damage)
    
    player_hit_damage = (player_attack - beast_defense)
    player_attack_amount = math.ceil(beast_health / player_hit_damage)


    if player_attack_amount < beast_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de beast.')
        player_health1=player_health-beast_hit_damage
        print(f'Je health is nu {player_health1}.')

    else:
        print('Helaas is de beast te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(3)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een beast tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print(' ')
time.sleep(4)
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