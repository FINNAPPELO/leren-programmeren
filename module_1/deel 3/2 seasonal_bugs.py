print('Welk seizoen vind jij het fijnst?', 
      "A) Lente", 
      "B) Zomer", 
      "C) Herfst", 
      "D) Winter")
weer_type='koud'
gekozen_seizoen = input('? ')
print(gekozen_seizoen)
if gekozen_seizoen == 'b':
    weer_type = 'warm'

elif gekozen_seizoen == 'd':
    weer_type = 'koud'
else:
    print("dus jij houd van het middelsijzoen")
    weer_type= 'gemiddeld weer'
if  gekozen_seizoen == 'b' or "d":
    print(f'Dus jij houd van {weer_type} weer!')
