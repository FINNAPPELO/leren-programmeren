from time import sleep
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'
print(OPTIES)
s1=int(input(COMPETENTIE_STELLING_1))
print(OPTIES)
s2=int(input(COMPETENTIE_STELLING_2))
print(OPTIES)
s3=int(input(COMPETENTIE_STELLING_3))
print(OPTIES)
s4=int(input(COMPETENTIE_STELLING_4))
print(OPTIES)
s5=int(input(COMPETENTIE_STELLING_5))
print(OPTIES)
s6=int(input(COMPETENTIE_STELLING_6))
print(OPTIES)
s7=int(input(COMPETENTIE_STELLING_7))
punten = s1+s2+s3+s4+s5+s6+s7
for i in range (3):
    print("we zijn je advies aan het berekenen...")
    sleep(1)
if punten <= 2:
    print('''
    Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
    in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
    op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
    ''')
elif punten <= 3:
     print('''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
''')
else:
    print('''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
''')