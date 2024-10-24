wachtwoord = 'kaasjes'
i=0
while i < 5:
    raden=input('wat is het wachtwoord:   ')
    if  raden == wachtwoord:
        print('goed gedaan je hebt het wachtwoord geraden')
        exit()
    else:
        print('helaas  het wachtwoord is niet goed, probeer het nog eens')
        i += 1
print('je hebt  het wachtwoord niet geraden, het wachtwoord is kaasjes')





