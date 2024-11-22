from fruitmand import fruitmand
kleuren_dict = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'purple': 'paars',
    'blue': 'blauw',
    'brown': 'bruin'
}
langste_fruit = None
max_naam_lengte = 0
for fruit in fruitmand:
    if len(fruit['name']) > max_naam_lengte:
        langste_fruit = fruit
        max_naam_lengte = len(fruit['name'])
kleur_in_nederlands = kleuren_dict.get(langste_fruit['color'], langste_fruit['color'])
print(f"Naam: {langste_fruit['name']}, Kleur: {kleur_in_nederlands}, Gewicht: {langste_fruit['weight']} gram")
