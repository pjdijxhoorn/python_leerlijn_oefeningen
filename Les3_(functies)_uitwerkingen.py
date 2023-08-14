import random

# ==========Les3==========

# voeg hier nog een aantal basis opdrachten toe


# ------------opdracht1----------
"""
Een functie die bij projecten handig is, is een functie waarmee je random getallen kan genereren. Dat gaan we in deze opdracht doen!
A. 
Maak een functie met de naam random_number_generator.
Geef deze minimal en maximal als parameters.
Maak een variabel getal en vul deze met random.randint(minimal, maximal)
Roep 10 keer de methode aan en print de waarde direct.
Je output komt er ongeveer zo uit te zien (met andere waarden): 
Random getal 1: 4
Random getal 2: 8
Random getal 3: 5
Random getal 4: 3
Random getal 5: 9
Random getal 6: 6
Random getal 7: 7
Random getal 8: 2
Random getal 9: 1
Random getal 10: 10

B.
Je kan de print statement met de aanroep natuurlijk 10 maal uittikken, maar hoe zou je dit efficienter kunnen doen?
"""

def random_number_generator(minimal, maximal):
    getal = random.randint(minimal, maximal)
    return getal

for x in range(1,10):
    print(random_number_generator(1, 10))

# ------------opdracht2----------

"""
Stel je voor dat je op verschillende plekken in je code de gebruiker om een cijfer wilt vragen. 
Dan kan je natuurlijk de volgende code gebruiken: 

getal = int(input("geef een cijfer onder de 5 op: "))
print(getal)

Maar als de gebruiker nu de string "drie" invoert krijg je een error. Probeer het maar eens.
Dit is natuurlijk niet handig want nu stopt je programma. 
Wat we eigenlijk willen is dat de gebruiker ook bij een verkeerde invoer nog in het programma blijft.
Hoe zou je dit kunnen oplossen?  

Stappenplan
1. Maak een functie met de naam check_if_number en een invoer van getal.
2. In de functie maak je een whileloop met de voorwaarde True.
3. Maak een try-except statement.
4. In de try zet je een return van getal gecast naar een int.
5. In de except zet je achter de except: ValueError, voor een speciefiekere error.
6. Vervolgens kan je onder de except deze regel zetten:
    getal = int(input("Dit was incorrect, voer een nummerriek getal in:"))
7. Maak de variabele getal en geef deze waarde door een input zonder int casting.
8. Declareer nogmaals getal maar geef hem nu de waarde van de functie met getal als parameter.

Je output komt er ongeveer als volgt uit te zien: 
Vul een getal in: abc
Dit was incorrect, voer een nummerriek getal in: 456
Je hebt 456 ingevoerd.

*Bonusvraag: Kan je de functie zo maken zodat deze alleen een invoer van 3 cijfers neemt?

"""
def check_if_number(number):
    while True:
        try:
            return int(number)
        except ValueError:
            number = int(input("Dit was incorrect, voer een nummerriek getal in:"))

getal = input("voer een getal in: ")
getal = check_if_number(getal)
print(getal)




# ------------opdracht4----------

"""
Herinner je nog die leuke rekenverhalen? 
In deze opdracht ga je een programma schrijven dat de oplossing vindt van een verhaal over een boer, kippen en een markt. 
Lees het verhaal en de opdracht om met Python op het juiste antwoord te komen! 

VERHAAL:
Een boer met een kleine boerderij heeft een paar kippen.
Vroeg in de ochtend pakt hij een mandje en verzamelt hij alle eieren die zijn kippen hebben gelegd
en gaat naar de markt om deze te verkopen.
Het is een gekke dag op de markt; de eerste klant komt bij de boer en vraagt:
Ik wil graag de helft van alle eieren die je hebt en een half ei.

Zo gevraagd, zo verkocht. De klant is immers koning.
Na een paar minuten komt de tweede klant en vraagt vreemd genoeg hetzelfde;
de helft van alle eieren die hij heeft en een half ei. Opnieuw is dit geen probleem.

Nou, gekker kan het niet worden, maar ook de derde en laatste klant vraagt hetzelfde als zijn twee voorgangers.
De boer heeft alle eieren verkocht en heeft geen ei kapot hoeven te maken.

Hoe kan dat en met hoeveel eieren ging de boer naar de markt?

OPDRACHT:
Jij kan dit natuurlijk oplossen door te rekenen. Maar als Programeur is het belangrijk om lui te zijn en
programma's te schrijven die het werk voor jou kunnen doen!
(Dat dit soms juist meer werk kost is een ander verhaal) Hoe kan je dat doen? 
1. Maak een functie die een getal inneemt in de parameters.
2. Test of dit getal na de berekeningen uitkomt op het antwoord 0. Nu kan je kijken of je gelijk had.
BONUS1: Kan je de code in de functie zo schrijven zodat je geen herhaling krijgt? (tip: gebruik een for loop)
BONUS2: Schrijf code die meerdere keren je methode aanroept en meerder cijfers tegelijkertijd kan testen.

Een voorbeeld van Je output kan er als volgt uitzien (met andere waarden):
Voer hier je antwoord in:10
False: 10
"""
def hoeveelEierenNamDeBoerMee(eieren):
    """ Deze methode berekent of het aantal eieren na de berekening op 0 uitkomt"""
    for i in range(3):
        eieren = (eieren / 2) - 0.5
    return eieren == 0

keuze = int(input("voer hier je antwoord in: "))
print(hoeveelEierenNamDeBoerMee(keuze), keuze)

# for i in range(12):
# print(i, hoeveelEierenNamDeBoerMee(i))

# ------------opdracht5----------


""" 
OPDRACHT:
Wij gaan een mastermind spel maken. Bij mastermind krijgt de speler een x aantal 
pogingen om een geheime cijfercode van 4 cijfers te raden. bij elke poging krijgt de speler feedback.
een + betekent dat het nummer klopt en op de juiste plek staat. een O betekent dat het nummer voorkomt in
de geheime cijfercode maar niet op de juiste plek staat en een X betekent dat dit nummer 
niet voorkomt in de geheime cijfercode. De output komt er straks zo uit te zien:

voer hier je antwoord in: 
5678
+oXX        
nog  11 pogingen over
voer hier je antwoord in: 

dit betekend dus dat 5 goed is 6 goed maar op de vekeerde plek en 7 en 8 niet voorkomen.

STAPPENPLAN:
1.  Begin met het maken van een functie genaamd make_random_number(). Deze functie moet 
    4 random getallen tussen de 1 en 9 genereren en deze teruggeven als een string.
2.  Creëer een functie genaamd feedback_guess() die twee parameters heeft: guess (een string van 4 cijfers) 
    en randomnumber (ook een string van 4 cijfers). 
    De functie moet de feedback geven in de vorm van +, O en X.
3.  Creëer een functie genaamd play_the_game() en zet hier de volgende dingen in:
a.  Print een korte introductie van het spel.
    print("Welkom bij mastermind. \n"
          "je krijgt een 4 nummer reeks en je moet binnen 12 pogingen de juiste reeks hebben ingevuld\n"
          " + is dit nummer klopt en staat op de juiste plek.\n"
          " O is dit nummer klopt maar staat niet op de juiste plek.\n"
          " X betekent dit nummer komt niet voor in deze nummerreeks\n")
b.  Roep vervolgens de functie make_random_number() aan en sla deze op in een variabele binnen de functie.
c.  Maak een while loop waarin de speler wordt gevraagd om een gok te doen totdat het aantal kansen op is of de 
    speler de juiste nummerreeks heeft geraden. Maak hiervoor een variabele int chances en boolean victory.
d.  Binnen de while loop, vraag je de speler om een gok te doen. Sla deze op in de variabele "guess".
e.  Controleer of de gok van de speler overeenkomt met de willekeurige nummerreeks die is gegenereerd. 
    Als dat het geval is, zet "victory" op "True" en geef de speler een felicitatiebericht.  
f.  Als de gok van de speler niet overeenkomt met de willekeurige nummerreeks, gebruik dan de functie 
    "feedback_guess" om feedback te geven over de gok van de speler en verminder het aantal kansen met 1.
g.  Geef de speler informatie over hoeveel pogingen er nog over zijn. 
h.  Vraag de speler of hij/zij verder wil spelen. Als het antwoord "ja" is, 
    roep dan de functie "play_the_game" aan om het spel opnieuw te spelen.
4   Voer de functie "play_the_game" uit om het spel te starten.      
"""

def make_random_number():
    number1 = str(random.randint(1, 9))
    number2 = str(random.randint(1, 9))
    number3 = str(random.randint(1, 9))
    number4 = str(random.randint(1, 9))
    return number1 + number2 + number3 + number4

def feedback_guess(guess, randomnumber):
    attempt = ""
    for x in range(4):
        if guess[x] == randomnumber[x]:
            attempt = attempt + "+"
        elif guess[x] in randomnumber:
            attempt = attempt + "O"
        else:
            attempt = attempt + "X"
    print(attempt)

def play_the_game():
    print("Welkom bij mastermind. \n"
          "je krijgt een 4 nummer reeks en je moet binnen 12 pogingen de juiste reeks hebben ingevuld\n"
          " + is dit nummer klopt en staat op de juiste plek.\n"
          " O is dit nummer klopt maar staat niet op de juiste plek.\n"
          " X betekent dit nummer komt niet voor in deze nummerreeks\n")
    randomnumber = make_random_number()
    chances = 12
    victory = False

    while chances > 0 and victory == False:
        guess = str(input("voer hier je antwoord in: "))

        if guess == randomnumber:
            print("Je hebt gewonnen!!")
            victory = True
        else:
            feedback_guess(guess, randomnumber)
            chances = chances - 1
            print("nog ", chances, "pogingen over")
    userinput = input("wil je blijven spelen type ja om te blijven spelen: ")
    if userinput == "ja":
        play_the_game()

play_the_game()

# ------------opdracht6----------
"""
OPDRACHT:
Rekenvaardigheden op basisscholen zijn niet zo goed als gewild door het ministerie van onderwijs.
zie de link hieronder
https://www.onderwijsinspectie.nl/actueel/nieuws/2021/04/09/veel-leerlingen-leren-niet-zo-goed-rekenen-als-ze-zouden-kunnen

om te zorgen dat rekenvaardigheden verbeteren op basisscholen heb jij opdracht gekregen om een mini-applicatie te 
schrijven die rekensommen maakt van twee random nummers en deze vervolgens print.
Hierna kan de user een input geven. De applicatie moet vervolgens de input controleren en de user 
hierop feedback geven of de som correct beantwoord is. Let op dit is een applicatie voor basisschool leerlingen dus 
geen decimalen en of negatieve getallen. Probeer het eerst te maken zonder het stappen plan.

1.  Importeer de vereiste module:
    Voeg aan het begin van de code de importverklaring voor de random module toe, zodat je random getallen kunt genereren.
2.  Definieer de functie randomNummerGenerator:
    Schrijf een functie genaamd randomNummerGenerator die twee parameters startnummer en eindnummer accepteert. 
    In de functie genereer je een random getal tussen startnummer en eindnummer met behulp van de random.randint() 
    functie en retourneer je dit getal.
3.  Definieer de functie rekenSomGenerator:
    Schrijf een functie genaamd rekenSomGenerator die twee parameters aantalvragen en maxgetal accepteert. 
    In deze functie initialiseer je de variabelen goedeantwoorden en fouteantwoorden met 0.
4.  Schrijf een while-lus om de vragen te genereren:
    Gebruik een while-lus om het aantal vragen bij te houden. De lus blijft doorgaan totdat het aantal vragen 0 is.
5.  Genereer random getallen en selecteer een operator:
    Binnen de while-lus roep je de functie randomNummerGenerator aan om twee random getallen te genereren.
     Gebruik ook randomNummerGenerator om een random getal te genereren tussen 1 en 4 om de operator te selecteren. 
     Sla het antwoord van de som op in de variabele antwoord.
6.  Gebruik de operator om de som te genereren:
    Implementeer een reeks if-elif-else verklaringen om de som te genereren op basis van de geselecteerde operator. 
    Gebruik de random getallen en de operator om de som op de juiste manier af te drukken.
7.  Ontvang de input van de gebruiker:
    Gebruik de input() functie om de gebruiker een antwoord op de som te laten invoeren. 
    Sla het antwoord op in de variabele keuze.
8.  Controleer het antwoord:
    Vergelijk het ingevoerde antwoord (keuze) met het juiste antwoord (antwoord) en geef de gebruiker feedback op basis 
    van de vergelijking. Houd het aantal goede en foute antwoorden bij.
9.  Druk de scores af:
    Na elke vraag druk je de huidige scores af, dwz het aantal goede en foute antwoorden.
10. Verminder het aantal vragen:
    Verminder het aantal vragen met 1 aan het einde van elke lusiteratie.
11. Vraag de gebruiker naar het maximumgetal en het aantal vragen:
    Vraag de gebruiker om het maximumgetal en het aantal vragen in te voeren voordat je de 
    rekenSomGenerator functie aanroept.
12. Roep de functie rekenSomGenerator aan:
    Roep de functie rekenSomGenerator aan met de ingevoerde waarden voor het maximumgetal en het aantal vragen.

Bonus : maak de functie zo dat er een random operator wordt gebrukt van de soort + - * of /. en hier dus een som van maakt.
Bonus bouw in dat je van te voren kan opgeven hoeveel vragen je wilt beantwoorden.
Bonus: bouw een punten systeem erbij voor goede antwoorden en foute antwoorden.
Tip: bij het aftrekken kom je soms negatief uit. als dit het geval is draai dan de nummers om.
Tip: bij het delen kom je soms op decimalen uit. maak de functie zo dat dit niet meer het geval is.
Tip modulo uitkomst van het grooste getal zetten en deze voorin in de berekening zetten
Bonus: schrijf de functie zo dat je zelf kan ingeven hoe hoog de getalen mogen zijn

"""



def randomNummerGenerator(startnummer, eindnummer):
    getal = random.randint(startnummer, eindnummer)
    return getal


def rekenSomGenerator(aantalvragen, maxgetal):
    aantalvragen = aantalvragen
    goedeantwoorden = 0
    fouteantwoorden = 0
    while aantalvragen != 0:

        randomnumber = randomNummerGenerator(1, maxgetal)
        randomnumber2 = randomNummerGenerator(1, maxgetal)
        randomoperatornummer = randomNummerGenerator(1, 4)
        antwoord = 0

        if randomoperatornummer == 1:
            if randomnumber > randomnumber2:
                antwoord = randomnumber - randomnumber2
                print(randomnumber, "-", randomnumber2, "=")
            else:
                antwoord = randomnumber2 - randomnumber
                print(randomnumber2, "-", randomnumber, "=")
        elif randomoperatornummer == 2:
            antwoord = randomnumber + randomnumber2
            print(randomnumber, "+", randomnumber2, "=")
        elif randomoperatornummer == 3:
            antwoord = randomnumber * randomnumber2
            print(randomnumber, "*", randomnumber2, "=")
        elif randomoperatornummer == 4:
            if randomnumber > randomnumber2:
                over = randomnumber % randomnumber2
                randomnumber = randomnumber - over
                antwoord = randomnumber / randomnumber2
                print(randomnumber, "/", randomnumber2, "=")
            else:
                over = randomnumber2 % randomnumber
                randomnumber2 = randomnumber2 - over
                antwoord = randomnumber2 / randomnumber
                print(randomnumber2, "/", randomnumber, "=")

        keuze = int(input("voer hier je antwoord in: "))
        print(keuze)

        if keuze == antwoord:
            print(keuze, "is het goede antwoord")
            goedeantwoorden = goedeantwoorden + 1
        else:
            print(keuze, "was fout het goede antwoord was ", antwoord)
            fouteantwoorden = fouteantwoorden + 1
        print("je hebt ", goedeantwoorden, "goed beantwoord", "en je hebt ", fouteantwoorden,
              "foutief beantwoord")
        aantalvragen = aantalvragen - 1


maxgetal = int(input("Voer hier het max getal in: "))
aantalvragen = int(input("Voer hier het aantal vragen in : "))
rekenSomGenerator(aantalvragen, maxgetal)

