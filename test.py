import random
import numpy as np
from PIL import Image

def test():
    print()



    # ------------- oefening 5-------------
    # jouw kameraden hebben een mijnenveld aangelegd om jouw geheime basis maar zijn vergeten om te noteren waar de mijnen precies liggen.
    # om te zorgen dat jullie toch veilig door het gebied kunnen reizen besluit jij om te mijnen op te ruimen. Jouw kameraden hebben in een gebied van 5 bij 5
    # 5 mijnen neergelegd.
    # Maak een array van 25.
    # vul dat veld met de waarde O.
    # maak een random coordinaten generator. die 5 waarde genereerd.
    # vul de 5 coordinaten met een x
    # spreek alle waarde om de coordinaten en verhoog de waarde rondom het coordinaat met 1.
    # let daarbij als het coordinaat de waarde x heeft dan mag dit niet verhoogd worden.
    # schrijf een methode die een waarde neemt en op basis daarvan een coordinaat overzet naar dezelfde plek in een andere array.
    # schrijf de code om deze nieuwe array uit te printen als een mijnenveger veld
    # schrijf een beveiliging in dat je maar x keer mag raden.
    #
    # def printveld(arr):
    #     count = 0
    #
    #     for i in range(5):
    #         print("\n-------------------------")
    #         print("|", end="")
    #         for j in range(5):
    #             print(" " + str(arr[count]), end=" | ")
    #             count += 1
    #     print("\n-------------------------")
    #
    #
    #
    # arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # printveld(arr)


    # ------------- oefening 5-------------
    # schrijf een oneindige loop



    # ------------- oefening 5-------------
    # schrijf code die een array maakt van 0 tot 100. schrijf vervolgens code om te berekenen hoeveel nullen er voorkomen in de array.




    #-----bonus opdracht
    #///////////////////////////////// DEEL 1
    # we hebben in de ruimte een sataliet onderschept deze sataliet bevatte een gouden disk.
    # We hebben het vermoeden dat er informatie van de afzenders verborgen ligt in deze disk.
    # ook staan er verschillende blokken met tekenreeksen.  Deze hebben de wetenschappers allemaal genoteerd en in een bestanden gezet
    # schrijf een functie die de bestanden inleest en in een array zet.
    # -            §
    # --           ¶
    # ---          †
    # ----         ‡
    # -----         Ω
    # -Ω            ∞
    # --Ω           ≈
    # ---Ω          ≠
    # ----Ω         ≤
    # ΩΩ            ≥
    # schrijf code die de bovenste tekens kan ontcijferen. in menselijke tekens.
    symbols = ["§", "¶", "†", "‡", "Ω", "∞", "≈", "≠", "≤", "≥", "⊕", "⊗", "⊖", "⊘", "⊛", "⊜", "⊝", "⊞", "⊟"]
    # ///////////////////////////////// DEEL 2
    # door jouw slimme code oplossing hebben de wetenschappers de rest van tekens ook kunnen ontcijferen en hebben deze in een array neergzet.
    # ontcijfer nu de teken-blokken.
    #
    # zet hier een teken blok neer &^$*&*&*(^&$*(^%@@#!@^%$*&*&%^&*&(%%
    #
    # wetenschappers hebben al ondekt dat deze disk geluiden afspeelt als je er een naald opzet en deze op de juiste snelheid afspeelt.

    # ///////////////////////////////// DEEL 3
    # controleer of de ararys plaatjes weergeven
    # het eerste plaatje is een cirkel


    def makeAnImage(array):
        name = input("vul een naam in:")
        # Convert the NumPy array to a Pillow Image object
        img = Image.fromarray(array)
        # Save the image to a file
        img.save(f"images/{name}.png")
        img.show()



    def image_to_array(file_path):
        # Open the image file
        img = Image.open(file_path)
        # Resize the image to 256x256 pixels
        img = img.resize((256, 256))
        # Convert the image to a NumPy array
        arr = np.array(img)
        # Return the array return arr
        return arr

    arr = image_to_array("images/circle.png")
    print(arr)
    makeAnImage(arr)


    # shootoutgame ala maffia
    # Maak een game klasse zet in de game klasse rondes,
    #



    #  het land van geen id raadsel.
    # het land van geen idee ze hebben er geen koffie wel thee. Dit is een magisch land als je er geweest bent dan weet je voortaan wat ze er wel en niet hebben
    # deelnemers mogen raden of iets er is. en deelnemers mogen raden heo het land werkt. (er is niks met de letter i of d)
    # schrijf een functie
    # in deze functie maak je een while loop die test of het juiste eindantwoord is ingegeven.
    # als dat niet het geval is moet je als antwoord geven of dat woord er wel of niet is.

    def LandVanGeenId():
        print("het land van geen idee ze hebben er geen koffie wel thee. "
              "Dit is een magisch land als je er geweest bent dan weet je voortaan wat ze er wel en niet hebben"
              " je mag raden of iets specifieks er is. ook mag je raden raden hoe het land werkt wat er is. ")
        gewonnen = False
        while not gewonnen:
            string = input("geef hier op wat je denkt dat het antwoord is of wat je wilt testen: ")
            if string == "id":
                print("je hebt gelijk id ontbreekt")
                gewonnen = True
            elif "i" in string or "d" in string:
                print(string, "bestaat niet in deze wereld")
            else:
                print(string, "bestaat wel in deze wereld")


    LandVanGeenId()

    # schrijf een beursspel de koersen veranderen na elke beurt
    # in een beurt kan je kopen of verkopen.
    # 1 of meerdere koersen gaan elek beurt omhoog en 1 of meerdere koersen gaan elke beurt omlaag.
    # als je veel koopt gaan de beurzen omhoog als je veel verkoopt gaan de beurzen iets omlaag.

    # hangman battleship rock paper scissor
    # make a rock paper scissor game bonus make it so that it wins more often then not. bonus bonus make it so it cheats (badly in a funny visual way)

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



    def makerandomnumber():
        number1 = str(random.randint(1, 9))
        number2 = str(random.randint(1, 9))
        number3 = str(random.randint(1, 9))
        number4 = str(random.randint(1, 9))
        return number1 + number2 + number3 + number4

    def feedbackguess(guess, randomnumber):
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
        randomnumber = makerandomnumber()
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
                print("Je hebt victory!!")
                victory = True
            else:
                feedbackguess(guess ,randomnumber)
                chances = chances - 1
                print("nog ", chances, "pogingen over")

    play_the_game()

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
