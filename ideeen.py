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
    # 1 of meerdere koersen gaan elke beurt omhoog en 1 of meerdere koersen gaan elke beurt omlaag.
    # als je veel koopt gaan de beurzen omhoog als je veel verkoopt gaan de beurzen iets omlaag.

    # hangman
    # battleship
    # rock paper scissor
    # make a rock paper scissor game bonus make it so that it wins more often then not.
    # bonus bonus make it so it cheats (badly in a funny visual way)



    # ------------- oefening 5-------------
    # prisoners dilema
    # monty hall problem
    #