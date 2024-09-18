import random

#selecteer 2 nummers
num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

#vraag om een antwoord

number = str(input(f'Weet jij wat {num1} + {num2} is? ') )
if number.isdigit() is True:
        number=int(number)
else: 
     print('Dat is geen nummer!')
#geef reactie op het antwoord
try:
    if int(number == num1+num2):
        print('Dat is juist')
    elif int(number != num1+num2):
        print('Nee dat klopt niet')
except:
        print('')
