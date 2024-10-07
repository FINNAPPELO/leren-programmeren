def generate_lists():
    A_lijsten = int(input("Hoeveel lijstjes wilt u zien? "))
    alle_lijsten = []
    for i in range(A_lijsten):
        lengte = int(input(f"Hoelang moet lijst {i + 1} zijn? "))
        stap = i + 1
        start = i + 1
        current_list = [start + stap * j for j in range(lengte)]
        alle_lijsten.append(current_list)

    print(alle_lijsten)
generate_lists()
