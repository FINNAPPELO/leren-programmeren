from fruitmandd import fruitmand

def gewicht_fruit(fruit):
    return fruit['weight']

gesorteerd_fruit = sorted(fruitmand, key=gewicht_fruit, reverse=True)

for fruit in gesorteerd_fruit:
    print(f"{fruit['name']} - {fruit['weight'] / 1000} kg")
