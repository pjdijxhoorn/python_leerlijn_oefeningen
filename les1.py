import random

def les1():
    # ==========Les1==========

    # //////////Variabelen//////////

    # ------------opdracht1----------
    """
    Maak een variable naam.
    De naam wordt gevuld door een input te gebruiken.
    Maak een variable welkomsgroet.
    Print de welkomsgroet en naam uit.
    """

    naam = input("geef hier je naam in")
    welkomsgroet = "welkom"
    print(welkomsgroet, naam)

    # ------------opdracht2----------
    """ 
    Maak een variabele aan tire.
    geef deze de waarde van "deze band is lek"
    print band.
    overschrijf de waarde met: "nieuwe band op gezet"!
    print band opnieuw.
    """

    band = "deze band is lek"
    print(band)
    band = "nieuwe band op gezet"
    print(band)

    # ------------opdracht3----------
    """
    Haal met behulp van slicing de dieren uit de volgende variablen: 
    En print deze. 
    """

    # Deze variabelen krijg je al!
    var1 = "Hij voelde land onder zijn voeten"
    var2 = "Men brak dat krot terstond af."
    var3 = "Deze weg is lang, zeg."
    var4 = "Gaan we zelf op bezoek of komen zij?"
    var5 = "Geef me vlug die pan terwijl de kast nog open staat.."

    # de eerste krijg je al
    oplossing1 = var1[9:15]
    print(oplossing1)

    #overige oplossingen
    oplossing2 = var2[15:21]
    print(oplossing2)
    oplossing3 = var3[10:16]
    print(oplossing3)
    oplossing4 = var4[6:11]
    print(oplossing4)
    oplossing5 = var5[17:24]
    print(oplossing5)


    # //////////operatoren//////////
    #------------opdracht1 ----------
    """
    Het blok Python Fundamentals is 15 ETCS waard en elk ETCS staat voor 28 studie uren.
    Het python blok bestaat uit 14 weken.
    Maak een variable ETCS aan en wijs daar 15 aan toe.
    Maak een variable Studie uren en wijs daar 28 aan toe.
    bereken hoeveel uren je per week aan deze curcus zou moeten zitten.
    print deze waarde uit
    """

    ETCS = 15
    studieuren = 28
    weken = 14

    totaalstudieuren = ETCS * studieuren
    tijdperweek = totaalstudieuren / weken
    print("het aantal studieuren = ", totaalstudieuren)
    print("het totaal per week = ", tijdperweek)

    # ------------opdracht2----------

    """
    declareer twee variablen voor de leeftijd van 2 van je vrienden.
    bereken en print het verschil in leeftijd van de twee vrienden.
    maak gebruik van een vergelijkingsoperatoren om te bepalen welke vriend het oudst is
    """

    tim = 30
    bas = 33

    leeftijdsverschil = bas - tim
    print(leeftijdsverschil)

    print(bas == tim)
    print(bas > tim)

    # ------------opdracht3----------
    """
    We gaan een euro dollar converter maken. 

    1. Zoek de koers op en sla deze waarde op in variabele (dollarwaarde , euro waarde).
    2. Print deze gegevens uit met behulp van een print()
    3. Maak een gebruikers invoer die vraagt om aantal dollar en print de waarde in euro's en andersom.
    """

    dollar_euro = 0.94
    euro_dollar = 1.07

    print("1 dollar = ", dollar_euro, "euro. and 1 euro is ", euro_dollar, " dollar")
    conversion_dollar_to_euro = float(input("Give the amount of dollar you want to convert to euro: "))
    conversion_euro_to_dollar = float(input("Give the amount of euro you want to convert to dollar: "))
    print(conversion_dollar_to_euro, "dollar converterd to euro is: ", conversion_dollar_to_euro * dollar_euro)
    print(conversion_euro_to_dollar, "euro converterd to dollar is: ", conversion_euro_to_dollar * euro_dollar)

    # ------------opdracht4----------
    """
    OPDRACHT: 
        We gaan een Rekenkundig spel maken waarbij je twee getallen moet 
        raden op basis van de berekeningen die hierop gedaan zijn.
 
    STAPPENPLAN: 
         1. Maak 2 int variabelen maximum en minimum en vul deze met een userinput zorg dat je de gebruker de juiste feedback 
         geeft zodat deze weet wat deze moet doen. 
         2. Maak 2 int variabelen en geef deze de waarde van een random nummer met maximum en minimum om het bereik te bepalen. 
         3. Maak een Boolean variabele en vul deze met de uitkomst van randomnummer1 == randomnummer2. 
         Print de boolean met de tekst "randomnummer1 is gelijk aan randomnummer2". 
         4. Maak een boolean variable en vul deze met de uitkomst van randomnummer1 > randomnummer2. 
         Print de boolean met de tekst "randomnummer1 is groter dan randomnummer2". 
         5. Maak een variabele plus met de waarde van de twee random nummers bij elkaar opgeteld. 
         Print deze uit met de tekst "randomnummer1 + randomnummer2 = "+ variable 
         6. Maak een variabele min met de waarde van de twee random nummers van elkaar afgetrokken. 
         Print deze uit met de tekst "randomnummer1 - randomnummer2 = "+ variable 
         7. Maak een variabele keer met de waarde van de twee random nummers van elkaar vermenigvuldigd. 
         Print deze uit met de tekst "randomnummer1 * randomnummer2 = "+ variable 
         8. Maak een variabele keer met de waarde van de twee random nummers van elkaar gedeeld. 
         Print deze uit met de tekst "randomnummer1 / randomnummer2 = "+ variable 
         9. Print gok het eerste getal. 
         10. Maak een int variabele gokgetal1 en vul deze met een userinput. 
         11. Vergelijk gokgetal1 met randomnummer1 en print dit uit met goede feedback voor de user 
         12. Print gok het eerste getal. 
         13. Maak een int variabele gokgetal2 en vul deze met een userinput. 
         14. Vergelijk gokgetal2 met randomnummer2 en print dit uit met goede feedback voor de user 
         15. Test je rekenspel! 
    """

    max = int(input("geef een max getal"))
    minimaal = int(input("geef een minimaal getal"))
    randomNumber1 = random.randint(minimaal, max)
    randomNumber2 = random.randint(minimaal, max)

    gelijk = randomNumber1 == randomNumber2
    print("getal1 en getal2 zijn gelijk", gelijk)
    groter = randomNumber1 > randomNumber2
    print("getal1 is groter dan getal2", groter)
    vermenigvuldig = randomNumber1 * randomNumber2
    print("getal1 X getal2 = ", vermenigvuldig)
    plus = randomNumber1 + randomNumber2
    print("getal1 + getal2 = ", plus)
    aftrekken = randomNumber1 - randomNumber2
    print("getal1 - getal2 = ", aftrekken)
    delen = randomNumber1 / randomNumber2
    print("getal1 / getal2 = ", delen)

    gokgetal1 = int(input("wat denk je dat getal1 is"))
    gok1 = gokgetal1 == randomNumber1
    print(gokgetal1, "is", gok1)
    gokgetal2 = int(input("wat denk je dat getal2 is"))
    gok2 = gokgetal2 == randomNumber2
    print(gokgetal2, "is", gok2)

    # //////////If-elif-else statements//////////
    # ------------opdracht1----------
    """
    maak een if-else statement om te checken of een getal groter of kleiner is dan 0.
    1. maak een variable number aan en geef deze waarde door een input.
    2. maak een if statement die checkt of number groter is dan 0.
    3. in de if statement zet je een print met "number groter dan 0."
    4. maak nu een else Deze moet number is is kleiner dan 0.
    5. als je de code nu draait zul je kunnen testen of het werkt.
    6. voer eens 0 in klopt de uitkomst?
    7. maak de code zo dat hij bij 0 zegt dit is 0.
    """
    number = int(input("geef een nummer om te checken of groter of kleiner is dan 0 :"))

    # check if number is greater than 0
    if number > 0:
        print('Number is groter dan 0.')
    elif number == 0:
        print("number is 0")
    else:
        print('Number is kleiner dan 0.')


    # ------------opdracht2----------
    """
    In Nederland mag je alcoholische dranken kopen vanaf je 18e. 
    Je moet echter tot je 25ste een ID kunnen tonen.    
    Hieronder heeft de gebruiker al zijn leeftijd ingevoerd. 
    
    Het is aan jou om de volgende berichten af te drukken:    
    Wanneer de gebruiker onder 18 is: Jij mag geen alcohol kopen.    
    Wanneer de gebruiker 25 jaar of ouder is: Jij mag zonder restricties alcohol kopen.    
    Wanneer de gebruiker tussen 18 en 25 is: Jij mag alcohol kopen, maar jij moet je ID tonen.
    test of je code werkt met alle drie de groepen    
    """

    givenAge = int(input("Wat is uw leeftijd?"))

    if givenAge < 18:
        print("je mag geen achol")
    elif givenAge > 25:
        print("jij mag zonder restrictie achol kopen")
    else:
        print("jij mag achol maar toon id")


    # ------------opdracht3----------
    """
    BMI Calculator  

    Maak een programma dat het Body Mass Index (BMI) van een persoon berekent op basis van hun lengte en hun gewicht. 
    Dit programma moet vervolgens een bericht printen dat zegt of de gerbuiker ondergewicht, 
    normaal gewicht, overgewicht of obesitas heeft.  
    
    Stappenplan:
    1. Maak een variable aan voor zowel  gewicht als lengte en wijs de waarde hieraan toe met een input() voor float. 
    2. Deze moet natuurlijk ook duidelijk aan de gebruiker vragen om gewicht en lengte.  
    3. Gebruik de formule BMI = gewicht/ lengte**2 om de bmi score van de gebruiker te berekenen 
    4. Maak een if elif else statement. 
    5. De if checkt of bmi is onder 18.5 en print u heeft ondergewicht. 
    6. De elif checkt of bmi onder de 25 is en print u heeft normaal gewicht 
    7. De volgende elif  checkt of bmi onder de 30 is en print u heeft overgewicht 
    8. De else statement print u heeft obesitas. 
    9. Print “uw BMI is: ” en vervolgens het bmi  
    
    * Bonus rond de bmi bij de laaste print af zoek op het internet op hoe dat zou kunnen. 
    """

    # vraag de gebruiker om hun gewicht (in kg) en lengte (in meter)
    gewicht = float(input("Voer uw gewicht in kilogram in: "))
    lengte = float(input("Voer uw lengte in meter in: "))

    # bereken de BMI van de gebruiker
    bmi = gewicht / lengte ** 2

    # controleer de BMI van de gebruiker en geef feedback
    if bmi < 18.5:
        print("U heeft ondergewicht.")
    elif bmi < 25:
        print("U heeft een normaal gewicht.")
    elif bmi < 30:
        print("U heeft overgewicht.")
    else:
        print("U heeft obesitas.")

    # print de BMI van de gebruiker
    print("Uw BMI is:", round(bmi, 2))

    # ------------opdracht4----------
    """
    Maak een programma om te bereken wat iemands verschillende trainingszone ’s zijn 
    en wat waarvoor deze het best gebruikt kunnen worden. 
    Dit gebeurd op basis van hartslag hiervoor moet je van de gebruiker weten wat zijn/haar leeftijd is en rusthartslag. 
    De max hartslag wordt uitgerekend met 220 – leeftijd. 
    Geef de gebruiker een keuze voor de verschillende trainingszones en geef na de keuze de betreffende informatie. 
    
    Zone 1 = max (hartslag – rusthartslag) * 50% + rusthartslag  # vetverbranding &uithoudingsvermogen 
    Zone 2 = max (hartslag – rusthartslag) * 60% + rusthartslag  #  Cardiovasculaire fitheid en uithoudingsvermogen 
    Zone 3 = max (hartslag – rusthartslag) * 70% + rusthartslag  # anaerobe en aerobe capiciteit 
    Zone 4 = max (hartslag – rusthartslag) * 80% + rusthartslag # maximale zuurstof opname 
    Zone 5 = max (hartslag – rusthartslag) * 90% + rusthartslag # maximale inspanning en sprintvermogen 
    
    Stappenplan: 
    1. Vraag de gebruiker om zijn/haar leeftijd via de input functie en sla deze op in een variabele. 
    2. Vraag de gebruiker om zijn/haar rusthartslag via de input functie en sla deze op in een variabele. 
    3. Bereken de maximale hartslag van de gebruiker met de formule: 220 - leeftijd en sla deze op in een variabele. 
    4. Bereken de hartslagreserve van de gebruiker met de formule: maximale hartslag - rusthartslag 
       en sla deze op in een variabele. 
    5. Bereken de verschillende trainingszones van de gebruiker op basis van de hartslagreserve 
       en sla deze op in verschillende variabelen. 
    6. Vraag de gebruiker welke hartslagzone hij/zij wilt weten en sla deze op in een variabele. 
    7. Geef de gebruiker de trainingsbenefits van de gekozen hartslagzone weer door middel van if-else statements. 
    8. Print de verschillende trainingszones en de trainingsbenefits van de gekozen hartslagzone aan de gebruiker. 
    """

    zone = ""
    # Vraag gebruiker naar leeftijd en rusthartslag
    leeftijd = int(input("Wat is uw leeftijd? "))
    rusthartslag = int(input("Wat is uw rusthartslag? "))

    # Bereken maximum hartslag op basis van leeftijd
    max_hartslag = 220 - leeftijd

    # Bereken trainingszones op basis van rusthartslag en max hartslag
    zone_1 = int((max_hartslag - rusthartslag) * 0.5 + rusthartslag)
    zone_2 = int((max_hartslag - rusthartslag) * 0.6 + rusthartslag)
    zone_3 = int((max_hartslag - rusthartslag) * 0.7 + rusthartslag)
    zone_4 = int((max_hartslag - rusthartslag) * 0.8 + rusthartslag)
    zone_5 = int((max_hartslag - rusthartslag) * 0.9 + rusthartslag)

    # Vraag gebruiker naar gewenste trainingszone en trainingsvoordelen
    gewenste_zone = int(input("Welke trainingszone wilt u weten (1-5)? "))
    if gewenste_zone == 1:
        voordelen = "Vetverbranding en uithoudingsvermogen"
        zone = zone_1
    elif gewenste_zone == 2:
        voordelen = "Cardiovasculaire fitheid en uithoudingsvermogen"
        zone = zone_2
    elif gewenste_zone == 3:
        voordelen = "Aerobe en anaerobe capaciteit"
        zone = zone_3
    elif gewenste_zone == 4:
        voordelen = "Maximale zuurstofopname en anaerobe capaciteit"
        zone = zone_4
    elif gewenste_zone == 5:
        voordelen = "Maximale inspanning en sprintvermogen"
        zone = zone_5
    else:
        voordelen = "Ongeldige trainingszone"

    # Print trainingszone en trainingsvoordelen
    print("Uw trainingszone is:", zone)
    print("Trainingsvoordelen:", voordelen)

    # ------------opdracht5----------
    """
    Maak met behulp van if-elif-else statements, input, variabelen en print een quiz over de lesstof van deze week. 
    De quiz heeft minimaal 5 meer keuze vragen waarbij bij het goede antwoord de score verhoogt wordt.
    aan het eind van de toets moet je de score printen en weergeven of iemand geslaagd is of niet.  
    geef je quiz aan een klasgenoot en geef feedback op elkaars quiz!
    """



