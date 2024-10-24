# Naam van student: finn appelo
# Studentnummer: 99080583
# Doel van het programma: berekent wisselgeld
# Structuur van het programma: eerst totaale wisselgeld en daarna van groot muntgeld en dan naar klijn 

coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # de muntwaarden die gebruikt worden 500 als 5 euro 200 als 2 euro 100 als 1 euro 50 als 50 cent enzov

toPay = int(float(input('Te betalen bedrag: ')) * 100)  # zet het euro bedrag naar cent
paid = int(float(input('Betaald bedrag: ')) * 100)  # Zet het betaalde bedrag naar cent 
change = paid - toPay  # totale wisselgeld dat teruggegeven moet worden 

coinsReturned = {}  # houd het aantal gegeven munten bij

while change > 0 and len(coinValues) > 0:  # Blijft vragen tot de mundwaarden op is of de centen op zijn
    coinValue = coinValues.pop(0)  # na het gebruiken van een mundwaarden worden ze hier verwijdert
    nrCoins = change // coinValue  # Bereken het maximale aantal munten dat gegeven kan worden 
    
    if nrCoins > 0:  # Gaat verder aals er nog mintens een munt over is 
        print('Geef maximaal ', nrCoins, ' munten van ', coinValue, ' cent terug!')  # zegt de max aantal munten
        nrCoinsReturned = int(input('Hoeveel munten van ' + str(coinValue) + ' cent heb je teruggegeven? '))  # Vraag hoeveel  munten er teruggegeven zijn

        change -= nrCoinsReturned * coinValue  # haalt het geld van het wisselgeld af 
        coinsReturned[coinValue] = nrCoinsReturned  # slaaat de teruggegevn munten op in de lijst

if change > 0:  # als er aan het einde geld over is wort dat aan gegeven 
    print('Niet teruggegeven wisselgeld: ', str(change) + ' cent')
else:
    print('Alles is teruggegeven.')

# Print een overzicht
print("\nOverzicht van teruggegeven munten:")
for coin, count in coinsReturned.items():  # print aantal  munten van elke munt

    print(f"{count} munt(en) van {coin} cent")
