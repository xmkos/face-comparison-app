import math
import random
from collections import deque
from abc import ABC, abstractmethod

#got errors so I had to put all imports at the top, even tho it's not the best practice

'''
Lista 1, Lista 2, Lista 3
1. Przypisz do zmiennej dowolną liczbę całkowitą i wypisz ją na ekran.
2. Poproś użytkownika o podanie swojego imienia i wypisz je na ekranie. Przy pisaniu kodu źródłowego wykorzystaj komentarze.
3. Napisz program, który sprawdzi czy podany wiek kwalifikuje osobę do emerytury (czyli czy ma więcej niż 60 lat dla kobiet i więcej niż 65 lat dla mężczyzn).
4. Napisz program, który sprawdzi czy podane trzy liczby mogą być bokami trójkąta.
'''
class first_task:
    def first():
        #1. Przypisz do zmiennej dowolną liczbę całkowitą i wypisz ją na ekran.
        number = 10
        print(number)
    def second():
        #2. Poproś użytkownika o podanie swojego imienia i wypisz je na ekranie. Przy pisaniu kodu źródłowego wykorzystaj komentarze.
        name = input("Podaj swoje imię: ")
        print(name)
    def third():
        #3. Napisz program, który sprawdzi czy podany wiek kwalifikuje osobę do emerytury (czyli czy ma więcej niż 60 lat dla kobiet i więcej niż 65 lat dla mężczyzn).
        age = int(input("Podaj swój wiek: "))
        gender = input("Podaj swoją płeć (k/m): ").lower()
        if age > 60 and gender == "k":
            print("Jesteś emerytem")
        elif age > 65 and gender == "m":
            print("Jesteś emerytem")
        else:
            print("Nie jesteś emerytem")
    def fourth():
        #4. Napisz program, który sprawdzi czy podane trzy liczby mogą być bokami trójkąta.
        a = int(input("Podaj długość boku a: "))
        b = int(input("Podaj długość boku b: "))
        c = int(input("Podaj długość boku c: "))
        if a + b > c and a + c > b and b + c > a:
            print("Można zbudować trójkąt")
        else:
            print("Nie można zbudować trójkąta")

'''
Ćw. 4, Ćw. 5
1. Stwórz słownik zawierający informacje o kilku studentach (imię, nazwisko, wiek). Następnie wyświetl dane jednego z studentów.
2. Stwórz krotkę zawierającą imiona "Anna", "Jan" i "Maria".  Czy jest możliwe dodanie nowego imiona do nowo utworzonej krotki?
3. Posortuj listę liczb [5, 2, 8, 1, 3] rosnąco. Usuń drugi element z listy. Wypisz nowo utworzoną posortowaną listę.
4. Stwórz zagnieżdżoną listę zawierającą informacje o pracownikach firmy (imię, nazwisko, stanowisko, pensja). Napisz program, który wyświetli wszystkich pracowników z pensją powyżej 5000 zł.
5. Stwórz zagnieżdżony słownik zawierający informacje o dwóch osobach. Każda osoba powinna mieć przypisane imię, nazwisko i wiek. Następnie wyświetl imię pierwszej osoby.
6. Stwórz zagnieżdżoną krotkę zawierającą dwie krotki: (1, 2, 3) oraz (4, 5, 6). Następnie wyświetl trzeci element pierwszej krotki.
'''

class second_task:
    def first():
        #1. Stwórz słownik zawierający informacje o kilku studentach (imię, nazwisko, wiek). Następnie wyświetl dane jednego z studentów.
        students = {
            "student1": {
                "name": "Jan",
                "surname": "Kowalski",
                "age": 20
            },
            "student2": {
                "name": "Anna",
                "surname": "Nowak",
                "age": 22
            }
        }
        print(students["student1"])

    def second():
        #2. Stwórz krotkę zawierającą imiona "Anna", "Jan" i "Maria".  Czy jest możliwe dodanie nowego imiona do nowo utworzonej krotki?
        names = ("Anna", "Jan", "Maria")
        #names.append("Piotr") #Nie można dodawać elementów do krotki
        print(names)

    def third():
        #3. Posortuj listę liczb [5, 2, 8, 1, 3] rosnąco. Usuń drugi element z listy. Wypisz nowo utworzoną posortowaną listę.
        numbers = [5, 2, 8, 1, 3]
        numbers.sort()
        numbers.pop(1)
        print(numbers)

    def fourth():
        #4. Stwórz zagnieżdżoną listę zawierającą informacje o pracownikach firmy (imię, nazwisko, stanowisko, pensja). Napisz program, który wyświetli wszystkich pracowników z pensją powyżej 5000 zł.
        employees = [["Jan", "Kowalski", "Programista", 6000],
                     ["Anna", "Nowak", "Kierownik", 7000],
                     ["Piotr", "Nowak", "Kierownik", 4000]]
        for employee in employees:
            if employee[3] > 5000:
                print(employee)

    def fifth():
        #5. Stwórz zagnieżdżony słownik zawierający informacje o dwóch osobach. Każda osoba powinna mieć przypisane imię, nazwisko i wiek. Następnie wyświetl imię pierwszej osoby.
        people = {
            "person1": {
                "name": "Jan",
                "surname": "Kowalski",
                "age": 20
            },
            "person2": {
                "name": "Anna",
                "surname": "Nowak",
                "age": 22
            }
        }
        print(people["person1"]["name"])

    def sixth():
        #6. Stwórz zagnieżdżoną krotkę zawierającą dwie krotki: (1, 2, 3) oraz (4, 5, 6). Następnie wyświetl trzeci element pierwszej krotki.
        tuples = ((1, 2, 3), (4, 5, 6))
        print(tuples[0][2])

'''
Cw. 6
1.Napisz program, która przyjmuje listę imion i listę nazwisk oraz zwraca listę zawierającą pełne imiona i nazwiska. Wykorzystaj funkcję zip().
Przykładowe dane wejściowe:
imiona = ['Anna', 'Jan', 'Maria']
nazwiska = ['Kowalska', 'Nowak', 'Wiśniewska']
Oczekiwany wynik:
['Anna Kowalska', 'Jan Nowak', 'Maria Wiśniewska']
2. Utwórz listę zawierającą oceny z egzaminów studentów. Następnie użyj funkcji enumerate() do wyświetlenia indeksów oraz odpowiadających im ocen na ekranie.
3. Stwórz program, który przy użyciu funkcji len() sprawdzi długość słownika zawierającego nazwy przedmiotów i wyświetli tę długość na ekranie.
4. Napisz program w Pythonie, który będzie symulował działanie kolejki za pomocą wbudowanej struktury danych `deque` z modułu `collections`. Program powinien umożliwiać dodawanie elementów do kolejki, usuwanie elementów z kolejki oraz wyświetlanie zawartości kolejki.
'''

class third_task:
    def first():
        #1.Napisz program, która przyjmuje listę imion i listę nazwisk oraz zwraca listę zawierającą pełne imiona i nazwiska. Wykorzystaj funkcję zip().
        names = ['Anna', 'Jan', 'Maria']
        surnames = ['Kowalska', 'Nowak', 'Wiśniewska']
        full_names = [name + " " + surname for name, surname in zip(names, surnames)]
        print(full_names)
    def second():
        #2. Utwórz listę zawierającą oceny z egzaminów studentów. Następnie użyj funkcji enumerate() do wyświetlenia indeksów oraz odpowiadających im ocen na ekranie.
        grades = [3, 4, 5, 2, 3]
        for index, grade in enumerate(grades):
            print(index, grade)
    def third():
        #3. Stwórz program, który przy użyciu funkcji len() sprawdzi długość słownika zawierającego nazwy przedmiotów i wyświetli tę długość na ekranie.
        subjects = {
            "math": "matematyka",
            "english": "angielski",
            "polish": "polski"
        }
        print(len(subjects))
    def fourth():
        #4. Napisz program w Pythonie, który będzie symulował działanie kolejki za pomocą wbudowanej struktury danych `deque` z modułu `collections`. Program powinien umożliwiać dodawanie elementów do kolejki, usuwanie elementów z kolejki oraz wyświetlanie zawartości kolejki.
        from collections import deque
        queue = deque()
        while True:
            print("1. Dodaj element do kolejki")
            print("2. Usuń element z kolejki")
            print("3. Wyświetl zawartość kolejki")
            print("4. Zakończ program")
            choice = int(input("Wybierz opcję: "))
            if choice == 1:
                element = input("Podaj element do dodania: ")
                queue.append(element)
            elif choice == 2:
                if len(queue) > 0:
                    queue.popleft()
                else:
                    print("Kolejka jest pusta")
            elif choice == 3:
                print(queue)
            elif choice == 4:
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")

'''
Ćw. 7
1. Napisz program w Pythonie, która przyjmuje dwa napisy jako argumenty i zwraca informację czy są one anagramami (czy składają się z tych samych liter).
2. Napisz program, który obliczy pole powierzchni koła o zadanym promieniu, korzystając z modułu math.
3. Napisz program, który będzie generować losową liczbę z przedziału od 1 do 100 i sprawdzi, czy jest ona liczbą pierwszą.
'''

class fourth_task:

    def first():
        #1. Napisz program w Pythonie, która przyjmuje dwa napisy jako argumenty i zwraca informację czy są one anagramami (czy składają się z tych samych liter).
        def is_anagram(word1, word2):
            return sorted(word1) == sorted(word2)

        print(is_anagram("kot", "tok"))

    def second():
        #2. Napisz program, który obliczy pole powierzchni koła o zadanym promieniu, korzystając z modułu math.
        import math
        radius = 5
        area = math.pi * radius**2
        print(area)

    def third():
        #3. Napisz program, który będzie generować losową liczbę z przedziału od 1 do 100 i sprawdzi, czy jest ona liczbą pierwszą.
        import random
        number = random.randint(1, 100)
        if number < 2:
            print("Liczba nie jest pierwsza")
            return
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Liczba jest pierwsza")
        else:
            print("Liczba nie jest pierwsza")

'''
Ćw. 8
1. Napisz funkcję w Python, która przyjmuje jako argument listę napisów i zwraca listę zawierającą tylko te napisy, które zawierają literę 'a'.
2. Napisz funkcję w Python, która przyjmuje jako argument listę liczb całkowitych i zwraca listę zawierającą tylko te liczby, które są kwadratami innych liczb z listy.
3. Stwórz funkcję, która przyjmuje słownik zawierający nazwy produktów i ich ceny, a następnie zwraca nazwę produktu o najwyższej cenie.
'''

class fifth_task:

    def first():
        #1. Napisz funkcję w Python, która przyjmuje jako argument listę napisów i zwraca listę zawierającą tylko te napisy, które zawierają literę 'a'.
        def words_with_a(words):
            return [word for word in words if 'a' in word]

        print(words_with_a(["kot", "pies", "kawa"]))

    def second():
        #2. Napisz funkcję w Python, która przyjmuje jako argument listę liczb całkowitych i zwraca listę zawierającą tylko te liczby, które są kwadratami innych liczb z listy.
        def squares(numbers):
            return [number for number in numbers if number**0.5 in numbers]

        print(squares([1, 4, 9, 16, 25]))

    def third():
        #3. Stwórz funkcję, która przyjmuje słownik zawierający nazwy produktów i ich ceny, a następnie zwraca nazwę produktu o najwyższej cenie.
        def max_price(products):
            return max(products, key=products.get)

        print(max_price({"jabłko": 2, "banan": 3, "pomarańcza": 4}))

'''
Ćw. 9
1. Stwórz klasę "Książka" z atrybutami: tytuł, autor, rok_wydania. Napisz metodę, która wyświetli informacje o książce oraz metodę, która sprawdzi czy książka została wydana przed 2000 rokiem.
2. Stwórz klasę "Produkt" z atrybutami: nazwa, cena, ilość. Napisz metody, które umożliwią dodanie produktu do koszyka, zmniejszenie ilości produktu w koszyku oraz obliczenie całkowitej wartości koszyka.
3. Stwórz klasę "Trójkąt" dziedziczącą po klasie "FiguraGeometryczna", która będzie miała dodatkowy atrybut długości boków oraz metodę obliczającą pole i obwód trójkąta.
4. Stwórz klasę "Pojazd" z atrybutami marka, model i rok_produkcji. Następnie stwórz klasy "Samochod" i "Motocykl", które dziedziczą po klasie "Pojazd" i dodają atrybuty specyficzne dla danego typu pojazdu.
'''

class sixth_task:
    #1. Stwórz klasę "Książka" z atrybutami: tytuł, autor, rok_wydania. Napisz metodę, która wyświetli informacje o książce oraz metodę, która sprawdzi czy książka została wydana przed 2000 rokiem.
    class Book:

        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year

        def info(self):
            print(
                f"Tytuł: {self.title}, autor: {self.author}, rok wydania: {self.year}"
            )

        def is_old(self):
            return self.year < 2000

    #2. Stwórz klasę "Produkt" z atrybutami: nazwa, cena, ilość. Napisz metody, które umożliwią dodanie produktu do koszyka, zmniejszenie ilości produktu w koszyku oraz obliczenie całkowitej wartości koszyka.
    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def add_to_cart(self, cart):
            cart.append(self)

        def reduce_quantity(self, amount):
            if self.quantity >= amount:
                self.quantity -= amount
            else:
                print("Niewystarczająca ilość produktu")

        @staticmethod  #this method does not depend on the instance of the class so I used staticmethod
        def total_cart_value(cart):
            return sum(product.price * product.quantity for product in cart)

    #3. Stwórz klasę "Trójkąt" dziedziczącą po klasie "FiguraGeometryczna", która będzie miała dodatkowy atrybut długości boków oraz metodę obliczającą pole i obwód trójkąta.
    class FiguraGeometryczna:
        def __init__(self):
            pass

    class Trojkat(FiguraGeometryczna):
        def __init__(self, a, b, c):
            super().__init__()
            self.a = a
            self.b = b
            self.c = c

        def obwod(self):
            return self.a + self.b + self.c

        def pole(self):
            s = self.obwod() / 2
            if s * (s - self.a) * (s - self.b) * (s - self.c) < 0:
                return "Nieprawidłowe długości boków"
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    #4. Stwórz klasę "Pojazd" z atrybutami marka, model i rok_produkcji. Następnie stwórz klasy "Samochod" i "Motocykl", które dziedziczą po klasie "Pojazd" i dodają atrybuty specyficzne dla danego typu pojazdu.
    class Pojazd:
        def __init__(self, marka, model, rok_produkcji):
            self.marka = marka
            self.model = model
            self.rok_produkcji = rok_produkcji

    class Samochod(Pojazd):
        def __init__(self, marka, model, rok_produkcji, ilosc_drzwi):
            super().__init__(marka, model, rok_produkcji)
            self.ilosc_drzwi = ilosc_drzwi

    class Motocykl(Pojazd):
        def __init__(self, marka, model, rok_produkcji, typ):
            super().__init__(marka, model, rok_produkcji)
            self.typ = typ


'''
Ćw. 10
1. Polimorfizm:
Stwórz dwie klasy: Kwadrat i Kolo. Obie klasy powinny mieć metodę obliczająca pole powierzchni (np. oblicz_pole()). Następnie stwórz listę obiektów tych klas i wywołaj dla każdego z nich metodę oblicz_pole().
2. Hermetyzacja:
Stwórz klasę Osoba z atrybutami imie, nazwisko i wiek. Zabezpiecz atrybuty imie i nazwisko przed bezpośrednim dostępem z zewnątrz klasy.
3. Abstrakcja:
Stwórz klasę Zwierze z metodą abstrakcyjną daj_glos(). Następnie stwórz dwie klasy dziedziczące po klasie Zwierze: Pies i Kot. Każda z tych klas powinna zaimplementować metodę daj_glos() w sposób odpowiedni dla danego zwierzęcia.
4.
Napisz dekorator, który będzie mnożył wynik funkcji przez 2.
'''

class seventh_task:
    #1. Polimorfizm:
    # Stwórz dwie klasy: Kwadrat i Kolo. Obie klasy powinny mieć metodę obliczająca pole powierzchni (np. oblicz_pole()). Następnie stwórz listę obiektów tych klas i wywołaj dla każdego z nich metodę oblicz_pole().
    class Kwadrat:
        def __init__(self, bok):
            self.bok = bok

        def oblicz_pole(self):
            return self.bok**2  #pole kwadratu

    class Kolo:
        def __init__(self, promien):
            self.promien = promien

        def oblicz_pole(self):
            import math
            return math.pi * self.promien**2  #pole koła

    def first():
        kwadrat = seventh_task.Kwadrat(4)
        kolo = seventh_task.Kolo(3)
        figury = [kwadrat, kolo]
        for figura in figury:
            print(figura.oblicz_pole())

    #2. Hermetyzacja:
    # Stwórz klasę Osoba z atrybutami imie, nazwisko i wiek. Zabezpiecz atrybuty imie i nazwisko przed bezpośrednim dostępem z zewnątrz klasy.
    class Osoba:
        def __init__(self, imie, nazwisko, wiek):
            self.__imie = imie
            self.__nazwisko = nazwisko
            self.wiek = wiek

        def get_imie(self):
            return self.__imie

        def get_nazwisko(self):
            return self.__nazwisko

    def second():
        osoba = seventh_task.Osoba("Jan", "Kowalski", 30)
        print(osoba.get_imie(), osoba.get_nazwisko(), osoba.wiek)

    #3. Abstrakcja:
    # Stwórz klasę Zwierze z metodą abstrakcyjną daj_glos(). Następnie stwórz dwie klasy dziedziczące po klasie Zwierze: Pies i Kot. Każda z tych klas powinna zaimplementować metodę daj_glos() w sposób odpowiedni dla danego zwierzęcia.
    from abc import ABC, abstractmethod

    class Zwierze(ABC):
        @abstractmethod
        def daj_glos(self):
            pass

    class Pies(Zwierze):
        def daj_glos(self):
            return "Hau hau"

    class Kot(Zwierze):
        def daj_glos(self):
            return "Miau miau"

    def third():
        zwierzeta = [seventh_task.Pies(), seventh_task.Kot()]
        for zwierze in zwierzeta:
            print(zwierze.daj_glos())

    #4. Napisz dekorator, który będzie mnożył wynik funkcji przez 2.
    def multiply_by_2(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * 2
        return wrapper

    @multiply_by_2
    def fourth():
        return 5

    def run_fourth():
        print(seventh_task.fourth())

def main():
    tasks = [
        first_task.first,
        first_task.second,
        first_task.third,
        first_task.fourth,
        second_task.first,
        second_task.second,
        second_task.third,
        second_task.fourth,
        second_task.fifth,
        second_task.sixth,
        third_task.first,
        third_task.second,
        third_task.third,
        third_task.fourth,
        fourth_task.first,
        fourth_task.second,
        fourth_task.third,
        fifth_task.first,
        fifth_task.second,
        fifth_task.third,
        lambda: sixth_task.Book("Title", "Author", 1999).info(),
        lambda: sixth_task.Product("Product", 10, 5).add_to_cart([]),
        lambda: sixth_task.Trojkat(3, 4, 5).pole(),
        lambda: sixth_task.Samochod("Brand", "Model", 2020, 4),
        lambda: sixth_task.Motocykl("Brand", "Model", 2020, "Type"),
        seventh_task.first,
        seventh_task.second,
        seventh_task.third,
        seventh_task.run_fourth
    ]

    for task in tasks:
        try:
            task()
        except Exception as e:
            print(f"An error occurred while executing {task.__name__}: {e}")

if __name__ == "__main__":
    main()