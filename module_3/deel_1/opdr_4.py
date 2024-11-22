import random
from fruitmandd import fruitmand
aantal = int(input("Hoeveel keer wil je een fruitnaam zien? "))
for i in range(aantal):
    print(random.choice([fruit['name'] for fruit in fruitmand]))
