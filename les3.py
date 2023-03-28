import random
def les3():
    # ==========Les3==========

  # voeg hier nog een aantal basis opdrachten toe


    # ------------opdracht1----------
    """
    Een functie die bij projecten handig is een functie waarmee je random getallen kan genereren.
    Maak een functie met de naam random_number_generator.
    Geef deze minimal en maximal als parameters.
    Maak een variabel getal en vul deze met random.randint(minimal, maximal)
    roep 10 keer de methode aan en print de waarde direct.
    Je kan de print statement met de aanroep natuurlijk 10 maal uittikken, maar hoe zou je dit efficienter kunnen doen?
    """

    def random_number_generator(minimal, maximal):
        getal = random.randint(minimal, maximal)
        return getal

    print(random_number_generator(1, 10))
    print(random_number_generator(1, 10))
    print(random_number_generator(1, 10))

    # ------------opdracht2----------

    """
    Stel voor je wilt in verschillende plekken in je code de gebruiker om een cijfer vragen. 
    nu kan je natuurlijk de volgende code gebruiken: 
    
    getal = int(input("geef een cijfer onder de 5 op: "))
    print(getal)
    
    maar als de gebruiker nu de string "drie" invoert krijg je een error probeer het maar.
    Dit is natuurlijk niet handig want nu stopt je programma. 
    wat we eigenlijk willen is dat de gebruiker ook als hij iets verkeerds invoert nog in het programma blijft.
    hoe zou je dit kunnen oplossen? 
    
    Stappenplan
    1. Maak een functie met de naam check_if_number en een invoer van getal.
    2. In de functie maak je een whileloop met de voorwaarde True.
    3. maak een try-except statement.
    4. In de try zet je een return van getal gecast naar een int.
    5. In de except zet je achter de except ValueError voor een speciefiekere error.
    6. Vervolgens kan je onder de except deze regel zetten:
    getal = int(input("Dit was incorrect, voer een nummeriek getal in:"))
    7. Maak de variabele getal en geef deze waarde door een input zonder int casting.
    8. Declareer nogmaals getal maar geef hem nu de waarde van de functie met getal als parameter.
    9. Bonus kan je de functie zo maken zodat deze alleen een invoer van 3 cijfers neemt?
    
    """
    def check_if_number(getal):
        while True:
            try:
                return int(getal)
            except ValueError:
                getal = int(input("Dit was incorrect, voer een nummeriek getal in:"))

    getal = input("voer een getal in: ")
    getal = check_if_number(getal)
    print(getal)






    # ------------opdracht4----------

    """
    VERHAAL:
    Een boer met een kleine boerderij heeft een paar kippen.
    Vroeg in de ochtend pakt een mandje en verzamelt hij alle eieren die zijn kippen hebben gelegd
    en gaat naar de markt om deze te verkopen.
    Het is een gekke dag op de markt; de eerste klant komt bij de boer en vraagt:
    Ik wil graag de helft van alle eieren die je hebt en een half ei.

    Zo gevraagd zo verkocht. De klant is koning immers.
    Na een paar minuten komt de tweede klant en vraagt vreemd genoeg hetzelfde;
    de helft van alle eieren die hij heeft en een half ei. Opnieuw is dit geen probleem.

    Nou gekker kan het niet worden, maar ook de derde en laatste klant vraagt hetzelfde als zijn twee voorgangers.
    De boer heeft alle eieren verkocht en heeft geen ei kapot hoeven te maken.

    Hoe kan dat en met hoeveel eieren ging de boer naar de markt?

    OPDRACHT:
    Jij kan dit natuurlijk oplossen door te rekenen Maar als Programeur is het belangrijk om lui te zijn en
    programma's te schrijven die het werk voor jou kunnen doen!
    (Dat dit soms juist meer werk kost is een ander verhaal)
    Maak een functie die een getal inneemt in de parameters en test of dit getal na de berekeningen
    uit komt op het antwoord 0. nu kan je kijken of je gelijk had.
    BONUS1: kan je de code in de functie zo schrijven zodat je geen herhaling krijgt tip gebruik een for loop.
    BONUS2: schrijf code die meerdere keren je methode aanroept en meerder cijfers tegelijkertijd kan testen."""
    def hoeveelEierenNamDeBoerMee(eieren):
        """ Deze methode berekend of het aantal eieren na de berekening op 0 uitkomt"""
        for i in range(3):
            eieren = (eieren / 2) - 0.5
        return eieren == 0


    keuze = int(input("voer hier je antwoord in: "))
    print(hoeveelEierenNamDeBoerMee(keuze), keuze)

    # for i in range(12):
    # print(i, hoeveelEierenNamDeBoerMee(i))

    # ------------opdracht5----------


    """ Stappenplan code hieronder"""

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
        randomnumber = make_random_number()
        chances = 12
        victory = False
        print("Welkom bij mastermind. \n"
              "je krijgt een 4 nummer reeks en je moet binnen 12 pogingen de juiste reeks hebben ingevuld\n"
              " + is dit nummer klopt en staat op de juiste plek.\n"
              " O is dit nummer klopt maar staat niet op de juiste plek.\n"
              " X betekent dit nummer komt niet voor in deze nummerreeks\n")
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



