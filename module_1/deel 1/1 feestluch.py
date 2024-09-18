from termcolor import colored, cprint, COLORS
croissantjes  =(17*0.39)
stokbroden = (2*2.78)
korting = (3*0.50)
totaal = (croissantjes+stokbroden)
totaal_minkorting = (totaal - korting)
print (f'De feestlunch kost je bij de bakker {colored (totaal_minkorting, 'magenta', attrs=['bold'])} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
