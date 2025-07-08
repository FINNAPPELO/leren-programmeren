
import functions

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

    if choice == 'a':
        result = functions.addition(n1, n2)
    elif choice == 'b':
        result = functions.subtraction(n1, n2)
    elif choice == 'c':
        result = functions.multiplication(n1, n2)
    elif choice == 'd':
        result = functions.division(n1, n2)
    elif choice == 'e':
        result = functions.addition(n1, n2)
    elif choice == 'f':
        result = functions.subtraction(n1, n2)
    elif choice == 'g':
        result = functions.multiplication(n1, n2)
    elif choice == 'h':
        result = functions.division(n1, n2)

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

        if next_choice == 'a':
            result = functions.addition(result, n2)
        elif next_choice == 'b':
            result = functions.subtraction(result, n2)
        elif next_choice == 'c':
            result = functions.multiplication(result, n2)
        elif next_choice == 'd':
            result = functions.division(result, n2)
        elif next_choice == 'e':
            result = functions.addition(result, n2)
        elif next_choice == 'f':
            result = functions.subtraction(result, n2)
        elif next_choice == 'g':
            result = functions.multiplication(result, n2)
        elif next_choice == 'h':
            result = functions.division(result, n2)

        print(f"Nieuwe uitkomst: {result}")

if __name__ == "__main__":
    calculator()
