boodschappenlijst = []

while True:
    artikel = input("Welk artikel wilt u toevoegen?: ").lower() 
    artikel2 = int(input(f"Hoeveel {artikel} wilt u toevoegen?: "))

    gevonden = False
    for i in range(len(boodschappenlijst)):
        if boodschappenlijst[i][0] == artikel:
            boodschappenlijst[i] = (boodschappenlijst[i][0], boodschappenlijst[i][1] + artikel2)
            gevonden = True
            break

    if not gevonden:
        boodschappenlijst.append((artikel, artikel2))

    boodschappen = input("Wilt u meer boodschappen doen? (ja/nee): ").lower()

    if boodschappen == 'nee':
        break

print("\n-[ Boodschappenlijst ]-")
for item in boodschappenlijst:
    print(f"{item[1]}x {item[0]}")