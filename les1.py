import random

# ==========Les1==========
# //////////Variabelen//////////

# ------------opdracht 1----------
""" 
We gaan een welkomstgroet maken, waarbij je iemand verwelkomt. Als je de volgende stappen volgt zie 
je bijvoorbeeld het volgende: Welkom, Larissa  
Maak een variabele voor een naam. 
De naam wordt gevuld door een input te gebruiken. 
Maak een variable welkomsgroet (bijvoorbeeld welkom)  
Print de welkomsgroet en naam uit. 
"""


# ------------opdracht 2----------
"""  
In deze opdracht gaan we de waarde voor een variabele overschrijven. 
1. Maak een variabele genaamd: band. 
2. Geef het de waarde  "deze band is lek" 
3. Print band. 
4. Overschrijf de waarde met: "nieuwe band op gezet"! 
5. Print band opnieuw. 
6. Overschrijf de band nu opnieuw met : 404
7. Print band opnieuw.
"""



# ------------opdracht 3----------
""" 
Je kan door middel van slicing een deel van de string eruit halen. Dit doe je door in een index 
aan te geven waar de slice (onderdeel van de string die je eruit haalt) moet beginnen en waar die moet eindigen. 
Haal met behulp van slicing de dieren uit de volgende variabelen:  
En print deze.   
"""

# Deze variabelen krijg je al!
variabele1 = "Hij voelde land onder zijn voeten"
variabele2 = "Men brak dat krot terstond af."
variabele3 = "Deze weg is lang, zeg."
variabele4 = "Gaan we zelf op bezoek of komen zij?"
variabele5 = "Geef me vlug die pan terwijl de kast nog open staat.."

# de eerste krijg je al als je het goed hebt gedaan komt hier het volgende dier uit: Eland
oplossing1 = variabele1[9:15]
print(oplossing1)

# Tip! De volgende dieren komen voor in de variabelen: Ezel, Panter, Slang, Otter, Eland



# //////////operatoren//////////
# ------------opdracht1 ----------
""" 

In deze opdracht gaan we berekenen hoeveel uur jij aan Python fundamentals moet besteden. 
Het blok Python Fundamentals bestaat uit 12 weken en is 15 ETCS waard. Elk ETC staat voor 28 studie uren. 
Het antwoord berekenen we natuurlijk niet met rekenmachine maar gewoon via Python. Volg daarvoor de volgende stappen:  
1. Maak een variabele ETCS aan en wijs daar 15 aan toe. 
2. Maak een variabele studie_uren_per_ETCS en wijs daar 28 aan toe. 
3. Maak een variabele studie_duur_in_weken aan en wijs daar 12 aan toe.
4. Bereken Hoeveel uren je in totaal aan de studie zou moeten zitten en sla dit op in een variabele.
4. Bereken hoeveel uren je per week aan deze cursus zou moeten zitten. 
5. print het totaal aantal studieuren en studieuren per week uit. 
Als je deze goed uitvoert zou je een soortgelijk antwoord moeten zien(wel met andere waarden):   

Het totaal aantal studie_uren =  x 
Het totaal studie uren per week =  x 
"""


# ------------opdracht2----------

""" 
We gaan nu in Python het verschil berekenen tussen 2 leeftijden. Kies hiervoor 2 vrienden met een andere leeftijd 
en volg de volgende stappen: 

1. Maak (declareer) twee variabelen voor de leeftijden van je vrienden. 
2.Bereken en print het verschil in leeftijd van de twee vrienden. 
3. Maak gebruik van een vergelijkingsoperator om te bepalen welke vriend het oudst is. 
Bij een goede uitvoering kan een antwoord er ongeveer zo uit zien:  

7 
False 
True 
"""


# ------------opdracht3----------
""" 
We gaan een euro dollar converter maken. Hoe? Volg de onderstaande stappen: 

1. Zoek de koers op en sla deze waarde op in variabele (dollarwaarde naar eurowaarde , euro waarde naar dollarwaarde). 
2. Print deze gegevens uit met behulp van een print() 
3. Maak een gebruikers invoer (input) die vraagt om aantal dollar en print de waarde in euro's en andersom. 

Tip: een input geeft een string terug je wilt een float hebben dus gebruik typecasting
om de waarde om te zetten naar een float. 
"""



# ------------opdracht4----------
""" 
OPDRACHT:  
We gaan een rekenspel maken waarin je twee getallen moet raden op basis van berekeningen die daarop gedaan worden. 
We gaan twee int variabelen maken, random nummers genereren, verschillende berekeningen uitvoeren en twee variabelen
maken voor de geschatte getallen. Wanneer deze geschatte getallen overeenkomen met de random nummers, printen we de 
juiste feedback voor de gebruiker uit. Laten we beginnen met deze opdracht! 

STAPPENPLAN:  

1. Maak 2 int (integer) variabelen aan: maximum en minimum 
2. Vul deze met een userinput (zorg dat je de gebruiker de juiste feedback geeft zodat deze weet wat deze moet doen). 
3. Maak 2 int variabelen en geef deze de waarde van een random nummer met maximum en minimum om het bereik te bepalen. 
4. Maak een Boolean variabele en vul deze met de uitkomst van randomnummer1 == randomnummer2.  
5. Print de Boolean met de tekst "randomnummer1 is gelijk aan randomnummer2".  
6. Maak een Boolean variabele en vul deze met de uitkomst van randomnummer1 > randomnummer2.  
7. Print de Boolean met de tekst "randomnummer1 is groter dan randomnummer2". 
8. Maak een variabele plus met de waarde van de twee random nummers bij elkaar opgeteld. 
9. Print deze uit met de tekst "randomnummer1 + randomnummer2 = "+ variabele  
10. Maak een variabele min met de waarde van de twee random nummers van elkaar afgetrokken.  
11. Print deze uit met de tekst "randomnummer1 - randomnummer2 = "+ variabele  
12. Maak een variabele keer met de waarde van de twee random nummers van elkaar vermenigvuldigd.  
13. Print deze uit met de tekst "randomnummer1 * randomnummer2 = "+ variabele  
14. Maak een variabele keer met de waarde van de twee random nummers van elkaar gedeeld. 
15. Print deze uit met de tekst "randomnummer1 / randomnummer2 = "+ variabele  
16. Print gok het eerste getal.  
17. Maak een int variabele gokgetal1 en vul deze met een userinput.  
18. Vergelijk gokgetal1 met randomnummer1 en print dit uit met goede feedback voor de user 
19. Print gok het eerste getal.  
20. Maak een int variabele gokgetal2 en vul deze met een userinput.  
21. Vergelijk gokgetal2 met randomnummer2 en print dit uit met goede feedback voor de user 

Test je rekenspel!  

Je output kan er als volgt uit komen te zien (met andere random waarden) 

Geef een max getal3 
Geef een minimaal getal3 
Getal1 en getal2 zijn gelijk True 
Getal1 is groter dan getal2 False 
Getal1 X getal2 = 9 
Getal 1+ getal 2 = 6 
Getal1 – getal2 = 0 
Getal 1 / getal 2 = 1.0 
Wat denk je dat getal1 is3 
2 is True 
Wat denk je dat getal2 is4 
4 is False  

"""




# //////////If-elif-else statements//////////
# ------------opdracht1----------
""" 
In deze opdracht maak je een if-else statement om te checken of een gegeven getal groter of kleiner is dan 0 
1.Maak een variable number aan en geef deze waarde door een input. 
2.Maak een if statement die checkt of number groter is dan 0. 
3.In de if statement zet je een print met "number groter dan 0." 
4.Maak nu een else Deze moet number is is kleiner dan 0. 
5. als je de code nu draait zul je kunnen testen of het werkt. 
6. Voer eens 0 in klopt de uitkomst? Maak de code zo dat hij bij 0 zegt dit is 0. 
7. Je output zou er als volgt uit kunnen zien (met andere waarden):  

Geef een nummer om te checken of het groter of kleiner is dan 0 : 3 
Nummer is groter dan 0 


"""



# ------------opdracht2----------
""" 
In Nederland mag je alcoholische dranken kopen vanaf je 18e.  
Je moet echter tot je 25ste een ID kunnen tonen. Op basis van de leeftijd dien jij voor deze opdracht verschillende 
berichten af te drukken met print(). Dit doe je door de if, elif en else statement toe te passen. 
Het is aan jou om de volgende berichten af te drukken:  

* Wanneer de gebruiker onder 18 is: Jij mag geen alcohol kopen.     
* Wanneer de gebruiker 25 jaar of ouder is: Jij mag zonder restricties alcohol kopen.  
* Wanneer de gebruiker tussen 18 en 25 is: Jij mag alcohol kopen, maar jij moet je ID tonen. 

Test of je code werkt met alle drie de groepen    
De output kan er als volgt uitzien:  

Wat is uw leeftijd? 80 
Jij mag zonder restrictie alcohol kopen
"""



# ------------opdracht3----------
""" 
BMI Calculator   

Maak een programma dat het Body Mass Index (BMI) van een persoon berekent op basis van hun lengte en hun gewicht.  
Dit programma moet vervolgens een bericht printen dat zegt of de gebruiker ondergewicht, normaal gewicht, 
overgewicht of obesitas heeft.   

Stappenplan: 
1. Maak een variabele aan voor zowel  gewicht als lengte en wijs de waarde hieraan toe met een input() voor float.  
2. Deze moet natuurlijk ook duidelijk aan de gebruiker vragen om gewicht en lengte.   
3. Gebruik de formule BMI = gewicht/ lengte**2 om de bmi score van de gebruiker te berekenen  
4. Maak een if elif else statement.  
5. De if checkt of bmi is onder 18.5 en print u heeft ondergewicht.  
6. De elif checkt of bmi onder de 25 is en print u heeft normaal gewicht  
7. De volgende elif  checkt of bmi onder de 30 is en print u heeft overgewicht  
8. De else statement print u heeft obesitas.  
9. Print “uw BMI is: ” en vervolgens het bmi   

* Bonusstap: Zoek op het internet (google is your best friend) hoe je de BMI bij de laatste print
 kan afronden en pas dit toe.   

Je output kan er als volgt uitzien: 

Voer uw gewicht in Kilogram in: 210 
Voer uw lengte in centimeter in: 153 
U heeft obesitas 
Uw BMI is: 89.7 
"""



# ------------opdracht4----------
""" 
Bij het trainen is het mogelijk om je hartslag aan te houden om de voortgang te zien. 
Door je hartslag te monitoren kunnen trainingen effectiever en efficiënter gemaakt worden. 
et behulp van Python kunnen we eenvoudig verschillende training zones berekenen en aangeven waar 
die het beste voor gebruikt worden.  

Maak een programma om te bereken wat iemands verschillende trainingszone ’s zijn en 
waarvoor deze het best gebruikt kunnen worden.  
Dit gebeurt op basis van hartslag en leeftijd van een gebruiker. 
De max hartslag wordt uitgerekend met 220 – leeftijd.  
Geef de gebruiker een keuze voor de verschillende trainingszones en geef na de keuze de betreffende informatie.  

Zone 1 = 	max (hartslag – rusthartslag) * 50% + rusthartslag  # vetverbranding & uithoudingsvermogen  
Zone 2 = 	max (hartslag – rusthartslag) * 60% + rusthartslag  #  Cardiovasculaire  fitheid en uithoudingsvermogen  
Zone 3 = 	max (hartslag – rusthartslag) * 70% + rusthartslag  # anaerobe en aerobe capaciteit  
Zone 4 = 	max (hartslag – rusthartslag) * 80% + rusthartslag # maximale zuurstof opname  
Zone 5 = 	max (hartslag – rusthartslag) * 90% + rusthartslag # maximale inspanning en sprintvermogen  

Stappenplan:  

1. Vraag de gebruiker om zijn/haar leeftijd via de input functie en sla deze op in een variabele genaamd "leeftijd".  
2. Vraag de gebruiker om zijn/haar rusthartslag via de input functie en sla deze op in een variabele genaamd 
"rusthartslag".  
3. Bereken de maximale hartslag van de gebruiker met de formule: 220 - leeftijd en sla deze op in een variabele genaamd 
"maximale_hartslag".  
4. Bereken de hartslagreserve van de gebruiker met de formule: maximale hartslag - rusthartslag en sla deze op in een 
variabele genaamd "hartslagreserve".  
5. Bereken de verschillende trainingszones van de gebruiker op basis van de hartslagreserve en sla deze op in 
verschillende variabelen genaamd "zone1", "zone2", "zone3", "zone4" en "zone5".  
6. Geef de gebruiker een keuze voor de verschillende trainingzones en vraag de gebruiker welke hartslagzone hij/zij wilt
 weten. Sla deze op in een variabele genaamd "keuze". 
7. Geef de gebruiker de trainingsbenefits van de gekozen hartslagzone weer door middel van if-else statements.  
8. Print de verschillende trainingszones en de trainingsbenefits van de gekozen hartslagzone aan de gebruiker. 
"""



# ------------opdracht5----------
"""
Maak een quiz over de lesstof van deze week met behulp van if-elif-else statements, input, variabelen en print.
De quiz moet minimaal 5 meerkeuze vragen hebben. Bij het goede antwoord moet de score verhoogd worden.
Aan het einde van de toets moet je de score printen en weergeven of iemand geslaagd is of niet.
Deel je quiz met studiegenoten, kijk wie het hoogst scoort en geef feedback op elkaars quiz!
"""

