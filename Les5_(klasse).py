"""
Oefening 1: Eenvoudige klasse en object

Maak een klasse genaamd Person met de volgende eigenschappen: name en age.
Maak vervolgens een object van deze klasse met de naam person1
en stel de naam in op "Alice" en de leeftijd op 30. Print ten slotte de naam
en leeftijd van het object.
Breid de klasse Person uit met een methode genaamd greet,
die een begroeting afdrukt met de naam van de persoon.
"""

"""
Oefening 2: Bankrekeningklasse

Maak een klasse genaamd BankAccount met de volgende eigenschappen: 
account_number, account_holder en balance. V
oeg methoden toe om geld op te nemen en geld te storten in de rekening. 
Schrijf vervolgens code om een object van BankAccount te maken, 
geld te storten en op te nemen, en het saldo af te drukken.
"""

"""
Oefening 3: Dierenklasse met overerving

Maak een klasse genaamd Animal met de eigenschappen name en sound. 
Maak vervolgens twee subklassen genaamd Dog en Cat, 
die van de Animal-klasse erven. Voeg aan elke subklasse een methode 
make_sound toe om het geluid van het dier af te drukken. 
Maak objecten van zowel Dog als Cat en roep de make_sound-methode aan.

"""


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
