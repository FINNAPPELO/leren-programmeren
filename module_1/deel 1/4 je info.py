naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht  = input("Ben je een A) een jonge of B) een meisje? ").lower()
kleur = input("Wat is je favoriete kleur? ")
getal = int(input("Wat is je favoriete getal? "))
verschil = abs(leeftijd-getal)
geslacht_a = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{geslacht_a.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", kleur)
print(f"Het verschil tussen {geslacht_a} leeftijd en {getal} is:", verschil)
