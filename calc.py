import sys

def calculate(liczba_1, operacja, liczba_2):
    if operacja == '+':
        wynik = liczba_1 + liczba_2
    elif operacja == '-':
        wynik = liczba_1 - liczba_2
    else:
        print("Niepoprawna operacja. Obsługiwane operacje to '+' i '-'.")
        sys.exit(1)

    with open('/tmp/wynik.txt', 'w') as file:
        file.write(str(wynik))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Użycie: calc.py <liczba_1> <operacja +-> <liczba_2>")
        sys.exit(1)

    try:
        liczba_1 = float(sys.argv[1])
        operacja = sys.argv[2]
        liczba_2 = float(sys.argv[3])
    except ValueError:
        print("Nieprawidłowe argumenty. Wprowadź poprawne liczby.")
        sys.exit(1)

    calculate(liczba_1, operacja, liczba_2)
    print(f"Wynik został zapisany do pliku /tmp/wynik.txt.")
