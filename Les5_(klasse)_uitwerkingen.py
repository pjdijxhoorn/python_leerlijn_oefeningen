"""
Oefening 1: Eenvoudige klasse en object

Maak een klasse genaamd Person met de volgende eigenschappen: name en age.
Maak vervolgens een object van deze klasse met de naam person1
en stel de naam in op "Alice" en de leeftijd op 30. Print ten slotte de naam
en leeftijd van het object.
Breid de klasse Person uit met een methode genaamd greet,
die een begroeting afdrukt met de naam van de persoon.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hallo, ik ben {self.name}!")


person1 = Person("Alice", 30)
print("Naam:", person1.name)
print("Leeftijd:", person1.age)
person1.greet()
"""
Oefening 2: Bankrekeningklasse

Maak een klasse genaamd BankAccount met de volgende eigenschappen: 
account_number, account_holder en balance. V
oeg methoden toe om geld op te nemen en geld te storten in de rekening. 
Schrijf vervolgens code om een object van BankAccount te maken, 
geld te storten en op te nemen, en het saldo af te drukken.
"""


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Onvoldoende saldo.")

    def print_balance(self):
        print(f"Saldo van rekening {self.account_number} van {self.account_holder}: {self.balance}")


account1 = BankAccount("12345", "Alice")
account1.deposit(1000)
account1.withdraw(500)
account1.print_balance()
"""
Oefening 3: Dierenklasse met overerving

Maak een klasse genaamd Animal met de eigenschappen name en sound. 
Maak vervolgens twee subklassen genaamd Dog en Cat, 
die van de Animal-klasse erven. Voeg aan elke subklasse een methode 
make_sound toe om het geluid van het dier af te drukken. 
Maak objecten van zowel Dog als Cat en roep de make_sound-methode aan.

"""


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} zegt: Woof!")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} zegt: Meow!")


dog = Dog("Buddy", "Woof")
cat = Cat("Whiskers", "Meow")

dog.make_sound()
cat.make_sound()

"""
OPDRACHT BESCHRIJVING:
Jij als getalenteerde mountainbiker wil graag ervoor zorgen dat jouw fiets(en) altijd goed onderhouden zijn
en klaar om te gebruiken voor de volgende race. Daarom besluit je om een kleine applicatie
te schrijven om de status van je fietsen bij te houden. Je wilt kunnen zien wanneer een onderdeel vervangen moet worden.
Je wilt km kunnen toevoegen aan de huidige afstand van alle onderdelen. En als deze over de max afstand zijn gegaan wil
je waarschuwing krijgen en deze vervolgens kunnen vervangen.

STAPPEN:
1. Bedenk een plan voor de applicatie die de status van de fietsen bijhoudt.
2. Maak een class genaamd "Onderdeel" met de volgende attributen: naam, max_afstand, huidige_afstand, merk.
3. Maak een class genaamd "Fiets" met de volgende attributen: type_fiets, framemaat, kleur,
   merk, andere_variabele en een lege lijst voor onderdelen.
4. Voeg aan de "Fiets" class methodes toe voor het toevoegen, verwijderen en vervangen
   van onderdelen. Gebruik hiervoor de Onderdeel class.
5. Maak een methode "print_onderdelen" aan die alle onderdelen van een fiets print.
6. Maak een methode "fietstocht" aan die de huidige afstand van alle onderdelen van een fiets verhoogt met een gegeven
   afstand. Als een onderdeel de maximale afstand overschrijdt, geef dan een waarschuwing.
7. Maak een object van de "Fiets" class genaamd "mijn_fiets".
8. Maak objecten van de "Onderdeel" class voor elk onderdeel van de fiets en geef deze de juiste waardes.
9. Voeg de onderdelen toe aan de "mijn_fiets" object.
10. Print de onderdelen van "mijn_fiets".
11. Verhoog de huidige afstand van alle onderdelen van "mijn_fiets" met 3000 km.
12. Vervang het onderdeel "banden" door een nieuw onderdeel met de naam "reserveband".
13. Verwijder het onderdeel "remmen" uit de lijst met onderdelen van "mijn_fiets".
"""


class Onderdeel:
    def __init__(self, naam, max_afstand, huidige_afstand, merk):
        self.naam = naam
        self.max_afstand = max_afstand
        self.huidige_afstand = huidige_afstand
        self.merk = merk


class Fiets:
    def __init__(self, type_fiets, framemaat, kleur, merk, andere_variabele):
        self.type_fiets = type_fiets
        self.framemaat = framemaat
        self.kleur = kleur
        self.merk = merk
        self.andere_variabele = andere_variabele
        self.onderdelen = []

    def print_onderdelen(self):
        for onderdeel in self.onderdelen:
            print("Onderdeel:", onderdeel.naam)
            print("Maximale afstand:", onderdeel.max_afstand)
            print("Huidige afstand:", onderdeel.huidige_afstand)
            print("Merk:", onderdeel.merk)
            print("---------------------")

    def fietstocht(self, afstand):
        for onderdeel in self.onderdelen:
            onderdeel.huidige_afstand += afstand
            if onderdeel.huidige_afstand >= onderdeel.max_afstand:
                print("Waarschuwing: het onderdeel", onderdeel.naam,
                      "heeft de maximale afstand van ", onderdeel.max_afstand, " overschreden met",
                      onderdeel.huidige_afstand - onderdeel.max_afstand, " km en moet worden vervangen.")
        print("------------------------")

    def vervang_onderdeel(self, onderdeel):
        for fietsonderdeel in self.onderdelen:
            if fietsonderdeel.naam == onderdeel.naam:
                fietsonderdeel.huidige_afstand = onderdeel.huidige_afstand
                fietsonderdeel.max_afstand = onderdeel.max_afstand
                fietsonderdeel.merk = onderdeel.merk
                break
        else:
            print("Fout: het onderdeel", onderdeel.naam, "is niet gevonden in de lijst met")

    def voeg_onderdeel_toe(self, Onderdeel):
        self.onderdelen.append(Onderdeel)

    def verwijder_onderdeel(self, naam):
        for i, onderdeel in enumerate(self.onderdelen):
            if onderdeel.naam == naam:
                del self.onderdelen[i]
                break


# Aanmaak van de onderdelen
pedalen = Onderdeel('pedalen', 4000, 0, 'Shimano')
banden = Onderdeel('banden', 5000, 0, 'Continental')
ketting = Onderdeel('ketting', 2000, 0, 'Shimano')
remmen = Onderdeel('remmen', 3000, 0, 'Magura')
zadel = Onderdeel('zadel', 8000, 0, 'Selle Royal')
reserveband = Onderdeel('banden', 8000, 0, 'lekkerbanje')
# Aanmaak van een fiets
mijn_fiets = Fiets('racefiets', 54, 'rood', 'Giant', 'nog een variabele')

# Voeg onderdelen toe aan fiets
mijn_fiets.voeg_onderdeel_toe(pedalen)
mijn_fiets.voeg_onderdeel_toe(banden)
mijn_fiets.voeg_onderdeel_toe(ketting)
mijn_fiets.voeg_onderdeel_toe(remmen)
mijn_fiets.voeg_onderdeel_toe(zadel)

# Print onderdelen uit
mijn_fiets.print_onderdelen()
# verhoogt de huidige afstand van alle onderdelen met 3000
mijn_fiets.fietstocht(3000)
# vervangt de huidige afstand van het onderdeel door nieuwe onderdeel
mijn_fiets.vervang_onderdeel(reserveband)
# voegt een nieuw onderdeel toe aan de lijst met onderdelen
mijn_fiets.verwijder_onderdeel('remmen')  # verwijdert het onderdeel 'remmen' uit de lijst met onderdelen
