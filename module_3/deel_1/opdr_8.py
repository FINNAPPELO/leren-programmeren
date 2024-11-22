from fruitmandd import fruitmand


fruitmand.append({"name": "watermeloen", "weight": 1200})

totaal_gewicht = sum(fruit["weight"] for fruit in fruitmand)
print(totaal_gewicht)