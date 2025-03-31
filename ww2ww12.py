# Funkcje dla operacji matematycznych
def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def mnoz(x, y):
    return x * y

def dziel(x, y):
    if y != 0:
        return x / y
    else:
        return "Błąd: dzielenie przez 0!"

# Funkcja główna
def kalkulator():
    print("Witaj w kalkulatorze!")
    print("Wybierz operację:")
    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Mnożenie")
    print("4. Dzielenie")

    # Pobranie wyboru użytkownika
    wybor = input("Wybierz opcję (1/2/3/4): ")

    # Sprawdzenie poprawności wyboru
    if wybor in ['1', '2', '3', '4']:
        num1 = float(input("Wprowadź pierwszą liczbę: "))
        num2 = float(input("Wprowadź drugą liczbę: "))

        if wybor == '1':
            print(f"{num1} + {num2} = {dodaj(num1, num2)}")
        elif wybor == '2':
            print(f"{num1} - {num2} = {odejmij(num1, num2)}")
        elif wybor == '3':
            print(f"{num1} * {num2} = {mnoz(num1, num2)}")
        elif wybor == '4':
            print(f"{num1} / {num2} = {dziel(num1, num2)}")
    else:
        print("Niepoprawny wybór! Spróbuj ponownie.")

# Uruchomienie kalkulatora
kalkulator()
