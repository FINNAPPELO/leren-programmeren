def generate_lists():
    A_lijsten = int(input("Hoeveel lijstjes wilt u zien? "))
    alle_lijsten = []
    for i in range(A_lijsten):
        lengte = int(input(f"Hoelang moet lijst {i + 1} zijn? "))
        stap_groote = i + 1
        start_waarde = i + 1
        current_list = [start_waarde + stap_groote * rest_van for rest_van in range(lengte)]
        alle_lijsten.append(current_list)

    print(alle_lijsten)
generate_lists()
