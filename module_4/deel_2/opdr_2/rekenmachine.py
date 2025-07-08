# rekenmachine.py

from calculations import calculations

def calculator():
    print("Wat wilt u doen?")
    print("A) getallen optellen")
    print("B) getallen aftrekken")
    print("C) getallen vermenigvuldigen")
    print("D) getallen delen")
    print("E) getal ophogen")
    print("F) getal verlagen")
    print("G) getal verdubbelen")
    print("H) getal halveren")

    choice_map = {
        'a': "addition",
        'b': "subtraction",
        'c': "multiplication",
        'd': "division",
        'e': "addition",
        'f': "subtraction",
        'g': "multiplication",
        'h': "division"
    }

    choice = input("Kies: ").strip().lower()

    if choice in ['a', 'b', 'c', 'd']:
        n1 = float(input("Welk getal? "))
        n2 = float(input("Welk getal erbij? "))
    elif choice in ['e', 'f']:
        n1 = float(input("Welk getal? "))
        n2 = 1
    elif choice in ['g', 'h']:
        n1 = float(input("Welk getal? "))
        n2 = 2
    else:
        print("Ongeldige keuze, probeer opnieuw.")
        return calculator()

    result = calculations[choice_map[choice]](n1, n2)
    print(f"Uitkomst: {result}")

    while True:
        print("\nWat wilt u doen met de uitkomst?")
        print("A) iets optellen")
        print("B) iets aftrekken")
        print("C) met iets vermenigvuldigen")
        print("D) ergens door delen")
        print("E) ophogen")
        print("F) verlagen")
        print("G) verdubbelen")
        print("H) halveren")
        print("I) niets (stoppen)")

        next_choice = input("Kies: ").strip().lower()

        if next_choice == 'i':
            print("Rekenmachine gestopt.")
            break

        if next_choice in ['a', 'b', 'c', 'd']:
            n2 = float(input("Welk getal? "))
        elif next_choice in ['e', 'f']:
            n2 = 1
        elif next_choice in ['g', 'h']:
            n2 = 2
        else:
            print("Ongeldige keuze, probeer opnieuw.")
            continue

        result = calculations[choice_map[next_choice]](result, n2)
        print(f"Nieuwe uitkomst: {result}")

if __name__ == "__main__":
    calculator()
