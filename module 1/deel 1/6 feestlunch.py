aantalc = int(input("hoeveel croissantjes heb je genomen : "))
croissantjes  =(aantalc*0.39)
aantals = int(input("hoeveel stokbroden heb je genomen : "))
stokbroden = (aantals*2.78)
kortingb = float(input("hoeveel kortingsbonnen had je nog  : "))
korting = kortingb*0.5
totaal = (croissantjes+stokbroden)
totaal_minkorting = (totaal - korting)
print (f'De feestlunch kost je bij de bakker {totaal_minkorting} euro voor de {aantalc} croissantjes en de {aantals} stokbroden als de {kortingb} kortingsbonnen nog geldig zijn!')
