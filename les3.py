import random

def les3():
    # ==========Les1==========

    # ------------opdracht1----------


    # ------------opdracht1----------
    # Zet alles van les 1 in een functie genaamd les1
    # Zet alles van les 2 in een functie genaamd les2
    # Zet alles van les 3 in een functie genaamd les3
    # maak in je main een  keuze menu waarbij je de de verschillende lessen kan aanroepen.

    # ------------opdracht2----------
    # Er is een poort en daarbij een poortwachter als je hierdoorheen wilt dan zegt de poortwachter een getal en jij moet een getal terug zeggen.
    # als jouw antwoord correct is mag je erdoorheen. Paul wilt door de poort de poortwachter zegt acht. paul antwoord met 4 en mag doorlopen.
    # Bas wil ook door de poort de poortwachter zegt twaalf en bas zegt 6.
    # jij wilt er ook doorheen de poortwachter zegt elf. wat moet je antwoorden?
    # jouw antwoord zou moeten zijn 3 want elf bestaat uit 3 letters.
    # maak een digitale versie van de poortwachter die alarm slaat bij het verkeerde antwoord. en je toegang geeft bij het juiste.
    # maak een aparte functie waarbij de poortwachter eerst een random getal opgeeft.
    # bonus bouw een while loop in om meerdere pogingen te kunnen doen
    # bonus verbeter de code door een array te gebruiken en hierin de woorden uitgespeld op te halen op basis van de random en dan de lenght te lezen opdracht bij arrays?

    def poortwachter():
        randomNumber = random.randint(1, 12)
        print("de poortwachter roept ", randomNumber)
        print("de poortwachter vraagt: wat is het antwoord?")
        keuze = int(input("kies een getal: "))
        print(keuze)
        correcteAntwoord = None
        if randomNumber == 1:
            correcteAntwoord = 3
        elif randomNumber == 2:
            correcteAntwoord = 4
        elif randomNumber == 3:
            correcteAntwoord = 4
        elif randomNumber == 4:
            correcteAntwoord = 4
        elif randomNumber == 5:
            correcteAntwoord = 4
        elif randomNumber == 6:
            correcteAntwoord = 3
        elif randomNumber == 7:
            correcteAntwoord = 5
        elif randomNumber == 8:
            correcteAntwoord = 4
        elif randomNumber == 9:
            correcteAntwoord = 5
        elif randomNumber == 10:
            correcteAntwoord = 4
        elif randomNumber == 11:
            correcteAntwoord = 3
        elif randomNumber == 12:
            correcteAntwoord = 6

        if correcteAntwoord == keuze:
            print("welkom dat is correct")
        else:
            print("alarm we hebben en indringer!!!")


    poortwachter()

    # ------------- oefening 5-------------
    # kraken van de kluis / mastermind maken
    # maak een random number generator in deze functie wil je 4maal een randomnumer maken
    # en deze omzetten naar string en dan aan elkaar vast maken.
    # maak een variable chances wijs daar 12 aan toe.
    # maak een variable victory en zet deze op false
    # maak een while loop die test of chances meer is dan 0 en victory 12 is.
    # maak in de while loop een input voor string noem deze guess
    # maak een if else statement het if pad test of guess en random nummer overeen komen. en print een overwinningsbericht en zet victory op true.
    # het else pad haalt 1 van chances af. print hoeveel chances je nog hebt en roept een nieuwe functie aan feedback.
    # maak een nieuwe functie aan feedback die guess als parameter heeft.
    # maak in feedback een variable aan genaamd attempt
    # maak een for loop met een range van 4.
    # maak in de forloop een if elif else statement aan.
    # in de if test je of getal  x van guess overeenkomt met getal x van randomnumber. zo ja dan voeg je een + toe aan attempt
    # in de elif test of getal x sowieso voorkomt in randomnummer zo ja dan voeg je een O toe aan attempt.
    # in de else voeg je een X toe aan attempt.
    # print attempt.

    # bouw een beveiliging in dat er alleen maar 4 nummers ingevoerd kunnen worden.

    print("Welkom bij mastermind. \n"
          "je krijgt een 4 nummer reeks en je moet binnen 12 pogingen de juiste reeks hebben ingevuld\n"
          " + is dit nummer klopt en staat op de juiste plek.\n"
          " O is dit nummer klopt maar staat niet op de juiste plek.\n"
          " X betekent dit nummer komt niet voor in deze nummerreeks\n")

    def makerandomnumber():
        number1 = str(random.randint(1, 9))
        number2 = str(random.randint(1, 9))
        number3 = str(random.randint(1, 9))
        number4 = str(random.randint(1, 9))
        return number1 + number2 + number3 + number4

    def feedbackguess(guess):
        attempt = ""
        for x in range(4):
            if guess[x] == randomnumber[x]:
                attempt = attempt + "+"
            elif guess[x] in randomnumber:
                attempt = attempt + "O"
            else:
                attempt = attempt + "X"
        print(attempt)

    randomnumber = makerandomnumber()
    chances = 12
    victory = False

    while chances > 0 and victory == False:
        guess = str(input("voer hier je antwoord in: "))

        if guess == randomnumber:
            print("Je hebt victory!!")
            victory = True
        else:
            feedbackguess(guess)
            chances = chances - 1
            print("nog ", chances, "pogingen over")


        # ------------- oefening 2-------------
        # je hebt gemerkt dat niet alle verzetstrijder even goed zijn in basis rekenen en dat is best wel onhadig als je met bijvoorbeeld explosieven werkt.
        # hierom besluit je om een kleine rekenoefening programma te schrijven die rekensommen maakt en om een input vraagt en de input checkt met het correcte antwoord.
        # tja het leven van een verzetsheld is niet altijd actie en glamour.
        # bouw een applicatie die twee random nummers uit print.
        # en hier een som van maakt
        # vervolgens moet deze om een invoer vragen en checken of de invoer klopt met de gegeven som.
        # Bonus : maak de functie zo dat er een random operator wordt gebrukt van de soort + - * of /. en hier dus een som van maakt.
        # Bonus bouw in dat je van te voren kan opgeven hoeveel vragen je wilt beantwoorden.
        # Bonus: bouw een punten systeem erbij voor goede antwoorden en foute antwoorden.
        # Bonus: bij het aftrekken kom je soms negatief uit. als dit het geval is draai dan de nummers om.
        # Bonus: bij het delen kom je soms op decimalen uit. maak de functie zo dat dit niet meer het geval is.
        # Tip modulo uitkomst van het grooste getal zetten en deze voorin in de berekening zetten
        # Bonus: schrijf de functie zo dat je zelf kan ingeven hoe hoog de getalen mogen zijn

        print("-----rekenmachine-----")

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

        # ------------- oefening 5-------------
        print(
            "\n Het verhaal gaat als volgt er is een boer die naar de markt gaat en hij verkoopt de helft van zijn eieren plus een half ei aan de eerste klant. \n"
            "Vervolgens verkoopt hij aan de volgende klant ook de helft van zijn eieren plus een half ei. \n"
            "Ook de derde klant tevens de laaste klant koopt ook weer de helft van zijn eieren plus een half ei. de boer gaat zonder eieren naar huis. Met hoeveel eieren ging de boer naar de markt? hij breekt door de dag heen geen enkel ei.")

        # maak een functie die een getal inneemt en test of dat het correcte getal is voor het raadsel antwoord.

        def hoeveelEierenNamDeBoerMee(eieren):
            for i in range(3):
                eieren = (eieren / 2) - 0.5
            return eieren == 0

        keuze = int(input("voer hier je antwoord in: "))
        print(hoeveelEierenNamDeBoerMee(keuze), keuze)

        # for i in range(12):
        # print(i, hoeveelEierenNamDeBoerMee(i))