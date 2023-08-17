# ==========Les4==========
# //////////LIST//////////
"""
Oefening 1: Optellen van Lijstelementen
Schrijf een functie die een lijst van getallen als invoer neemt
en het totaal van alle elementen in de lijst berekent en retourneert.
"""

"""
oefening 2
Maak de lijst ‘getallen’ aan: getallen = [2, 4, 7, 11, 19]

Voer de volgende opdrachten uit:

Voeg het getal 22 toe aan (het einde van) de lijst 
Voeg het getal 6 toe tussen 4 en 7
Vervang het getal 4 door het getal 5

"""
"""
oefening 3
In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen:
1, 1, 2, 3, 5… De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. 
Implementeer de functie ‘fibon-acci’ die als parameter de lijst 
‘fibonacci_reeks = [1, 1]’ krijgt aangeleverd, 
en een element toe-voegt aan de lijst,
bestaande uit de vorige twee elementen.
Roep de functie meerdere keren aan (Bijvoorbeeld met een for-loop).
"""

"""
------------- oefening 4-------------
Opdracht ontcijferen van de vijandelijke code

Je hebt het volgende bericht onderschept van de vijand:

nu "eju jt ffo uftu", 25

En door goede inlichtingen ben je erachter gekomen hoe de vijand zijn berichten versleuteld.
Dit doen ze met een ceasar cipher. Dit betekent dat ze elke letter in hun bericht vervangen door een letter x aantal plekken verder in het aflabet.
Ontcijfer het bericht.

Stappenplan
maak een functie decoder deze krijgt als parameter mee text en een cijfer
binnen de functie maak je een string aan decodedmessage en deze krijgt voor de waarde een empty string.
maak een array aan genaamd alphabet. vul deze met de strings van alle letters van het alphabet.
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"
maak nu een forloop. for x in text.
in de forloop maak je een nieuwe variable ciphernumber deze vul je met de index van x in alphabet.
let op dat je x eerst omzet naar een hoofdletter.
tel hierbij cijfer nog op.
nu zoek je de nieuwe letter op in het alfabet door te zoeken in de index met het ciphernumber deze voeg je weer aan x toe.
nu voeg je aan decodedmessage x toe.
net buiten de forloop maak je nu een print met decodedmessage.
test de functie dusver door hem aan te roepen met de volgende waardes: "a",1 je zou B moeten zien in de console.
Test nu "z", 1 wat is de uitkomst en waarom denk je dat dit de uitkomst is?
om dit op te lossen gaan we nog wat extra code schrijven.
maak een if statement die checkt of ciphernumber groter of gelijk is aan 26. als dat het geval is
dan is ciphernumber ciphernumber modelus(%) 26 (je deelt door 26 en alles wat overblijft is het antwoord perfect voor deze situatie)
test "z", 1 opnieuw de uitkomst zou nu A moeten zijn.
test nu "eju jt ffo uftu", 25
waarom werkt dit niet?
bouw een nieuwe if statement in net in de forloop.
in de if statement test je of x een lege string is zo ja dan voeg je deze toe aan decodedmessage.
voeg de rest van de code in de forloop toe aan een else statement.
test test nu "eju jt ffo uftu", 25 opnieuw.
Bonus maak het zo dat je functie alle leestekens gewoon normaal toevoegd aan de decodedmessage.
Bonus ontcijfer de volgende tekst "DLDTNIYIHYDJGNIFYFUMJZXIATDXCMNCYUNN" hierop wordt niet alleen een ceasar cypher toegepast.
maar deze wordt ook nog neergezet in een volgorde van boven naar beneden in een 6 bij 6 grid. 20 verschuivingen
"""

"""
------------- oefening 2-------------
Jij bent onderdeel van het verzet en je hebt een vergadering met alle leden hoe je het beste te werk kan gaan.
Een van de leden zegt terecht dat hij de meeting niet wil bijwonen als zijn naam op de notulen komt want dan kan hij opgepakt worden.
Om dat te verkomen dat een van de leden ontmaskerd wordt besluit je een versleuteling te schrijven voor de namen.
natuurlijk moeten de namen ook weer ontcijferd worden.


lijst met namen:
Paul De Tank
Nova de spion
Mark de sniper
Sam de material man
Tessa de Black knight

maak een functie om namen aan de lijst toe te voegen.
let op schrijf de methode zo dat er geen dubbele namen ingezet worden.

maak een functie die de namen versleuteld aan een lijst toe voegt en daarna print.
1 zet alle letters om naar cijfers van het alphabet voeg na elke letter een - toe.
2 als het een hoofdletter is dan begin je met tellen bij 100. A = 101, B = 102 etc.
3 schrijf een functie die de code kan ontcijferen
Bonus als de naam al voorkomt in de lijst print dan een bericht dat de naam er al in staat
"""
# //////////TUPLE//////////
"""
oefening 1
Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 
1 tot en met 5 waarin elk element bestaat uit een tuple 
die het getal en het bijbehorende kwadraat bevat. 
Gebruik een list comprehension.
"""


"""
oefening2
Schrijf een dobbelspel voor een dobbelsteen met waardes 1 t/m 6. 
Als de speler 5 of 6 gooit, heeft hij gewonnen. 
Als hij 1 of 2 gooit, heeft hij verloren. 
Als hij 3 of 4 gooit, mag hij nog een keer gooien. 
Gebruik de random.randrange functie uit de module random voor 
de dobbelsteenwaarde. 
Hou de game status bij in een variabele die gecheckt wordt door
een while loop.
Gebruik if/elif waarde in tuple om te checken 
of een waarde gegooid is. Print de uitkomst.
"""

"""
------------- oefening *-------------
Wanneer je binnenkomt bij het ziekenhuis wordt jou patientdodossier binnengehaald.
Binnen dat patientdossier zijn er bepaalde dingen die aangepast kunnen worden zoals leeftijd, gewicht, lengte, bloeddruk.
Maar er zijn ook dingen die niet aangepast mogen worden zoals bsn, patientnummer.
Hieronder is een applicatie geschreven maar deze is niet geheel correct
want in dit geval mogen bsn en patientnummer nog steeds aangepast worden.

Vaker dan dat je helemaal van niks begint zal je als codeur code moeten fixen of aanvullen hiervoor is het ook
belangrijk dat je code kan lezen en fouten kan vinden. Let op er staan hier mogelijk dingen in de code die je nog niet
begrijpt dat maakt niet uit. start met te onderzoeken wat de code doet en lees de tips!

De opdracht heeft verschillende stappen:
    1.Maak het zo dat de bsn, naam en patientnummer niet meer overschreven kunnen worden na aanmaak
      maar wel getoont kunnen worden.
    2.bouw de applicatie verder uit dat alle andere waardes wel gewijzigd kunnen worden
      met aparte functies die om een input vragen ipv via de paramaters de waardes zetten.
    3. maak een zoek functie die werkt op basis van patientnummer voor de database. die werkt met een input
    bonus: schrijf een menu voor deze aplicatie.
    met de volgende keuzes:
        keuze1. zoek patient op
        keuze2. maak nieuwe patient
        keuze3. pas waardes van patient aan.
    gebruik hierbij input in de functies

tips:
    1. tuple kunnen gebruikt worden als key voor dictionaries.
    2. tuple kan meerdere waardes bevatten.
    3. dictionary-keys zijn niet overschrijfbaar.
    4. je kan wanneer een tuple tot key gemaakt is itereren over de key-waardes.
    5.

"""
# Create a dictionary to store patient dossiers
patient_database = {}

def display_dossier(dossier):
    print("Patiëntendossier:")
    print("{:<15} | {:<15} | {:<15} | {:<15} | {:<10} | {:<10} | {:<10} | {:<10}".format(
        "BSN", "Patiëntnummer","Voornaam", "Achternaam", "Gewicht", "Leeftijd", "Lengte", "Bloeddruk"))
    print("=" * 130)
    print("{:<15} | {:<15} | {:<15} | {:<15} | {:<10} | {:<10} | {:<10} | {:<10}".format(
        dossier[0], dossier[1], dossier[2], dossier[3], dossier[4], dossier[5], dossier[6], dossier[7]))
    print("=" * 130, "\n")


def create_patient_dossier(bsn, patientnummer,voornaam, achternaam, gewicht, leeftijd, lengte, bloeddruk):
    return [bsn, patientnummer, voornaam, achternaam, gewicht, leeftijd, lengte, bloeddruk]


def pas_waardes_aan(dossier, new_gewicht,new_leeftijd):
    dossier[2] = new_gewicht
    dossier[3] = new_leeftijd
    print("Gewicht bijgewerkt naar", new_gewicht)
    print("Leeftijd bijgewerkt naar", new_leeftijd, "\n")

# Add test-patient dossiers with patient numbers as keys
patient_database['P001'] = create_patient_dossier("123456789", "P001", "John", "Doe", 70, 30, 170, "120/80")

# Display the patient dossier for a specific patient number
display_dossier(patient_database['P001'])

# Probeer BSN en Patiëntnummer te wijzigen (zou niet moeten lukken) lukt nu wel!
patient_database['P001'][0] = "mag niet"
patient_database['P001'][1] = "mag ook niet"

# Update the weight and age for a specific patient number
pas_waardes_aan(patient_database['P001'], 80, 35)

# Display the updated test-patient dossier
display_dossier(patient_database['P001'])

# //////////SET//////////
"""
Oefening 1

Gegeven de verzameling {3, 44, 17, 23, 58, 9, 36}
Voer de volgende opdrachten uit:
Voeg de waarde 27 aan de verzameling toe.
Verwijder de waarde 23 uit de verzameling’.
Druk alle waarden in de verzameling tussen 20 en 50 af.
"""

"""
Oefening2
Gegeven de verzamelingen {11, 22, 33} en {5, 11, 16, 22}

Gebruik wiskundige verzamelingsoperatoren om de volgende verzamelingen te creëren:

{33}
{5, 16, 33}
{5, 11, 16, 22, 33}
{11, 22}

"""

"""
------------- oefening *-------------
opdracht je gaat dit jaar met de hele familie suprises maken voor sinterklaas.
Maar die ene oom had zichzelf vorig jaar ("perongeluk") meerdere keren toegevoegd. daarom besluit je om voor dit jaar een
miniapplicatie te schrijven deze app neemt namen in. Maar elke naam kan slechts eenmaal ingevoerd worden.
vervolgens geeft de app wanneer gevraag twee namen uit. 1 persoon die de suprise maakt en 1 die de suprise ontvangt.
elk persoon moet zowel een 1 suprise maken als ontvangen en je hebt geen gevallen dat iemand voor zichelf een suprise moet maken.

Stappenplan:
Stap 1: Initialisatie van sets
    Er worden twee lege sets recievers en givers aangemaakt. Dit zijn sets om namen van ontvangers en gevers bij te houden.
Stap 2: Definitie van add_names-functie

    Vraag de gebruiker om het aantal namen dat ze willen toevoegen.
    Voer een lus uit voor het opgegeven aantal keren:
    a. Vraag de gebruiker om een naam in te voeren.
    b. Voeg de ingevoerde naam toe aan zowel de recievers-set als de givers-set.
Stap 3: Definitie van create_surprise_pairs-functie

    Maak een lege lijst met de naam pairs om de verrassingsparen bij te houden.
    Blijf doorgaan zolang de givers-set niet leeg is:
    a. Kies willekeurig een ontvanger (reciever) en een gever (giver) uit de sets met behulp van de random.choice-functie.
    b. Controleer of de ontvanger en de gever niet dezelfde zijn.
    c. Verwijder de gekozen ontvanger en gever uit respectievelijk de recievers- en givers-sets.
    d. Voeg het paar in de vorm van "ontvanger-gever" toe aan de pairs-lijst.
    Toon de gemaakte verrassingsparen door door de pairs-lijst te lopen en de ontvanger en gever afzonderlijk weer te geven.
Stap 4: Definitie van main-functie

    Start een oneindige lus met de while True-verklaring.
    Toon een menu met drie opties:
    a. "Voeg namen toe"
    b. "Maak surprise-paren"
    c. "Stop"
    Vraag de gebruiker om een keuze.
    Als de keuze gelijk is aan "1", roep dan de add_names-functie aan om namen toe te voegen.
    Als de keuze gelijk is aan "2":
    a. Controleer of er minstens twee namen in de recievers-set staan.
    b. Als dat het geval is, roep dan de create_surprise_pairs-functie aan om verrassingsparen te maken en weer te geven, en breek dan uit de lus.
    c. Als er minder dan twee namen zijn, geef dan een foutmelding weer.
    Als de keuze gelijk is aan "3", breek dan uit de lus om het programma te beëindigen.
    Als de keuze geen van de bovenstaande opties is, geef dan een foutmelding weer.
Stap 5: Roep de main-functie aan

Roep de main-functie aan om het programma uit te voeren.

"""
# //////////DICTONARY//////////
"""
------------- oefening 1-------------
Gegeven een woordenboek van Internet toplevel domeinen:

In:
tlds = {'Nederland':'nl', 'Verenigde Staten':'us', 'Duitsland':'de'}

Voer de volgende opdrachten uit en toon de resultaten:

1. Controleer of het woordenboek de sleutel ‘Duitsland’ bevat.
2. Controleer of het woordenboek de sleutel ‘Frankrijk’ bevat.
3. Itereer door de sleutel-waarde paren en toon ze in 2-kolommen.
4. Voeg het sleutel-waarde paar ‘Zweden’ : ‘sw’ toe.
5. Wijzig de waarde van de sleutel ‘Zweden’ in ‘se’.
6. Gebruik een dictionary comprehension om sleutels en waarden te verwisselen.
7. Uitgaande van het resultaat van f) gebruik een dictionary comprehension om alle landnamen te converteren naar hoofdletters.
"""
"""
------------- oefening 2-------------
Een naam verzinnen is lastig hierom besluit je om je vrienden, familie en kennissen te vragen om te helpen.
Je besluit om een programma te schrijven om bij te houden welke namen zij noemen. 
Maar je wilt geen dubbele namen. 
Omdat je wel wil weten welke naam het meest populair is moet je wel bij houden welke naam vaker gekozen wordt.
ook wil je dat mensen zoveel namen kunnen doorgeven als ze zelf willen.
probeer eerst zonder hulp een programma hiervoor te schrijven.

Stappenplan:

1. Maak een lege dictonary genaamd name_counter.
2. Maak een oneindige while lus met while true.
3. maak een input die om een naam vraagt en deze aan de variable name toewijst.
    De tekts hiervan bevat "enter a name (or exit to exit)"
4. Maak een if die checkt of name exit is en break bij deze code
5. Maak een if statement die checkt of de name al in de lijst staat. 
    Als dat niet zo is voeg de naam toe met een waarde van 1. 
    Als de naam er wel in staat pas de waarde aan naar de waarde +1.
6. Print de waardes 


"""
"""
------------- oefening 3-------------
Maak een woordenboek van vrienden met hun voornaam als sleutel en hun leeftijd als waarde 
(we nemen even aan dat alle voornamen verschillend zijn).

Voer de volgende opdrachten uit en toon de resultaten:

Druk naam en leeftijd af van al je vrienden, alfabetisch gesorteerd op naam.
Druk de naam af van al je vrienden die 30 jaar of ouder zijn.
Verhoog alle leeftijden in het woordenboek met 1.
Verwijder alle vrienden waarvan de naam begint met de letter ‘B’
"""
"""
------------- oefening 4-------------

Je krijgt hieronder een Dictonary met daarin woorden nederlands en de franse vertaling.

vertaal de fransen woorden naar engels en maak hiervan een nieuwe dictonary nederlands_frans
hier zijn de woorden in het engels in een list.

english_words["head", "shoulders", "knee", "toe", "ears", "eyes", "top of the nose"]

1. maak een dictonary engels _frans vanuit de code die je al hebt.
2. draai nu de waarde om en maak daarvan een dictonary frans_engels.

3. maak een dictonary vertaler aan en vul deze met dictonaries van verschillende vertalingen

4. schrijf een methode waarbij je een vertaling kan opvragen.

Bonus: als deze niet bestaat geef de optie om deze toe te voegen

"""

english_words = ["head", "shoulders", "knee", "toe", "ears", "eyes", "top of the nose"]

nederlands_frans = {
    "hoofd": "diriger",
    "schouders": "epaules",
    "knie": "genou",
    "teen": "doigt de pied",
    "oren": "oreilles",
    "ogen": "yeux",
    "puntje van je neus": "bout de ton nez"
}
print(nederlands_frans)