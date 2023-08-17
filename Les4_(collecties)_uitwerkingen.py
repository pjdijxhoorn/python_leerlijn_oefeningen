import random

# ==========Les4==========
# //////////LIST//////////
"""
Oefening 1: Optellen van Lijstelementen
Schrijf een functie die een lijst van getallen als invoer neemt
en het totaal van alle elementen in de lijst berekent en retourneert.
"""


def calculate_total(numbers):
    total = sum(numbers)
    return total


numbers = [5, 10, 15, 20]
result = calculate_total(numbers)
print("Total:", result)

"""
oefening 2
Maak de lijst ‘getallen’ aan: getallen = [2, 4, 7, 11, 19]

Voer de volgende opdrachten uit:

Voeg het getal 22 toe aan (het einde van) de lijst 
Voeg het getal 6 toe tussen 4 en 7
Vervang het getal 4 door het getal 5

"""
getallen = [2, 4, 7, 11, 19]
getallen.insert(2, 6)
getallen.remove(4)
getallen.insert(1, 5)
print(getallen)


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
# Definieer de functie 'fibonacci' met parameters 'fibonaccireeks' en 'aantal'.
def fibonacci(fibonaccireeks, aantal):
    for _ in range(aantal - 2):  # Verminder met 2 omdat we al de eerste twee getallen hebben.
        fibonaccireeks.append(fibonaccireeks[-1] + fibonaccireeks[-2])

# Vraag de gebruiker om het gewenste aantal getallen voor de fibonacci-reeks.
aantal = int(input("Voer het aantal getallen in dat je wilt hebben voor de fibonacci_reeks: "))
fibonaccireeks = [1, 1]  # Initialiseer de fibonacci-reeks met de eerste twee getallen.

# Roep de 'fibonacci'-functie aan met de gegeven fibonacci-reeks en het gewenste aantal getallen.
fibonacci(fibonaccireeks, aantal)

# Toon de uiteindelijke fibonacci-reeks na de functieaanroep.
print(fibonaccireeks)

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

text = "eju jt ffo uftu"


def decoder(text, shiftnumber):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    decodedmessages = ""
    for letter in text:
        if letter.upper() not in alphabet:
            decodedmessages += letter
        else:
            ciphernumber = alphabet.index(letter.upper())
            ciphernumber += shiftnumber
            if ciphernumber >= 26:
                ciphernumber = ciphernumber % 26
            letter = alphabet[ciphernumber]
        decodedmessages += letter
    return decodedmessages


decodedmessage = decoder("eju jt ffo uftu", 25)
print(decodedmessage)

extrasecretmessages = "DLDTNIYIHYDJGNIFYFUMJZXIATDXCMNCYUNN"
decodedmessage = decoder(extrasecretmessages, 20)


def grid_to_string(s):
    row1 = s[0] + s[6] + s[12] + s[18] + s[24] + s[30]
    row2 = s[1] + s[7] + s[13] + s[19] + s[25] + s[31]
    row3 = s[2] + s[8] + s[14] + s[20] + s[26] + s[32]
    row4 = s[3] + s[9] + s[15] + s[21] + s[27] + s[33]
    row5 = s[4] + s[10] + s[16] + s[22] + s[28] + s[34]
    row6 = s[5] + s[11] + s[17] + s[23] + s[29] + s[35]
    newstring = row1 + row2 + row3 + row4 + row5 + row6
    return newstring


def decodegrid(message):
    decodetext = []
    for x in range(6):
        row = ""
        for j in range(6):
            letter = x + j * 6
            row += message[letter]
        decodetext.append(row)
    decodetext = "".join(decodetext)
    return decodetext


def decodegrid2(text):
    empty_string = ''
    for i in range(6):
        for x in range(6):
            letter = i + x * 6
            empty_string += (text[letter])
    print(empty_string)


inputstring = "OWOEYTJTSJOURYTQJQFXUKITLEOINXYNJFYY"
input_str = decoder(inputstring, -5)

# output_str = grid_to_string(input_str)
output_str = decodegrid(input_str)
print(output_str)  # Output: jemagtrotszijnopjezelfdatjeditoplost

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
Bonus gebruik een dictionary voor het maken van het alphabet als je dit niet al gedaan had
Bonus als de naam al voorkomt in de lijst print dan een bericht dat de naam er al in staat
"""

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
caseAlfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
members = []


def addMembers(members, name):
    namecoded = ""
    for i in range(len(name)):
        x = name[i]
        if x.isupper():
            for b in range(len(caseAlfabet)):
                if caseAlfabet[b] == x:
                    if i + 1 == len(name):
                        namecoded += str(b + 101)
                    else:
                        namecoded += str(b + 101) + "-"
        else:
            for j in range(len(alfabet)):
                if alfabet[j] == x:
                    if i + 1 == len(name):
                        namecoded += str(j + 1)
                    else:
                        namecoded += str(j + 1) + "-"
    if namecoded in members:
        print("this is already in here")
    else:
        members.append(namecoded)
        print("member added")
        return members


addMembers(members, "Paul De Tank")
addMembers(members, "Nova de spion")
addMembers(members, "Mark de sniper")
addMembers(members, "Sam de material man")
addMembers(members, "Tessa de Black knight")
print(members)


def decrypt(name):
    nameDecrypted = ""
    name = name.split("-")
    for i in range(len(name)):
        x = int(name[i])
        if x >= 101:
            nameDecrypted += caseAlfabet[x - 101]
        else:
            nameDecrypted += alfabet[x - 1]
    return nameDecrypted


encryptedname = '116-1-21-12-104-5-120-1-14-11'
decryptedname = decrypt(encryptedname)
print(decryptedname)

# ------------------------- bonus oplossing! ----------------------------------------
Verzetsleden = []

alphabet_dict = {chr(97 + i): str(i + 1) for i in range(26)}
alphabet_dict.update({chr(65 + i): str(101 + i) for i in range(26)})
alphabet_dict.update({' ': '000'})
reverse_alphabet_dict = {value: key for key, value in alphabet_dict.items()}


def encryption(nameinput):
    encrypted_name = "-".join(alphabet_dict.get(char, "") for char in nameinput)
    if encrypted_name in Verzetsleden:
        print("the name is already in here")
    else:
        Verzetsleden.append(encrypted_name)
    print(encrypted_name)


def decryption(verzetsleden):
    for name in verzetsleden:
        split_name = name.split("-")
        decrypted_name = "".join(reverse_alphabet_dict.get(char, "") for char in split_name)
        print(decrypted_name)


encryption(input('vul hier de naam in die je wilt versleutelen:\n'))
encryption(input('vul hier de naam in die je wilt versleutelen:\n'))
decryption(Verzetsleden)

# //////////TUPLE//////////
"""
oefening 1
Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 
1 tot en met 5 waarin elk element bestaat uit een tuple 
die het getal en het bijbehorende kwadraat bevat. 
Gebruik een list comprehension.
"""

getal_kwadraat_paar = [(getal, getal*getal)for getal in range(1, 6)]
print(getal_kwadraat_paar)

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


def spel():
    game_status = True
    while game_status:
        uitkomst = dobbelen()
        if uitkomst in (5, 6):
            print(f"Gefeliciteerd! Je hebt gewonnen met {uitkomst}.")
        elif uitkomst in (1, 2):
            print(f"Helaas, je hebt verloren met {uitkomst}. Probeer het opnieuw.")
            game_status = False
        else:
            print(f"Je hebt {uitkomst} gegooid. Gooi nog een keer!")


def dobbelen():
    return random.randrange(1, 7)


spel()

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

De opdracht heeft verschillende stappen
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

# Test Patients
test_patient = ('1', '987654321', 'John', 'Doe')
test_patient_values = ['70', '30', '180', '120/80']
patient_database[test_patient] = test_patient_values

test_patient = ('2', '1234567', 'John', 'Doe')
test_patient_values = ['70', '30', '180', '120/80']
patient_database[test_patient] = test_patient_values

test_patient = ('3', '1234567', 'John', 'Doe')
test_patient_values = ['70', '30', '180', '120/80']
patient_database[test_patient] = test_patient_values


def main_menu():
    while True:
        print("Menu:")
        print("1. Zoek patiënt op")
        print("2. toon alle patienten")
        print("3. Maak nieuwe patiënt")
        print("4. Pas waardes van patiënt aan")
        print("5. Exit")

        choice = input("Maak een keuze: ")

        if choice == '1':
            zoek_patient_op()
        elif choice == '2':
            display_all_patients()
        elif choice == '3':
            create_patient_dossier()
        elif choice == '4':
            pas_waardes_aan()
        elif choice == '5':
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")


def zoek_patient_op():
    patientnummer = input("Voer het patiëntnummer in: ")
    for key, value in patient_database.items():
        if key[0] == patientnummer:
            print("Patiëntendossier:")
            display_dossier(key, value)
            print("")
            return
    print("Patiënt niet gevonden.\n")


def display_all_patients():
    print("+", "=" * 128, "+")
    print(
        "||", " " * 55, "PatientDossiers", " " * 55, "||")
    print("+", "=" * 128, "+")
    print("|{:<15} | {:<15} | {:<15} | {:<15} | {:<10} | {:<10} | {:<10} | {:<19}|".format(
        "BSN", "Patiëntnummer", "Voornaam", "Achternaam", "Gewicht", "Leeftijd", "Lengte", "Bloeddruk"))
    x = 0
    for key, value in patient_database.items():
        x += 1
        print("+", "-" * 128, "+")
        print("|{:<15} | {:<15} | {:<15} | {:<15} | {:<10} | {:<10} | {:<10} | {:<19}|".format(
            key[1], key[0], key[2], key[3], value[0], value[1], value[2], value[3]))
        if len(patient_database) == x:
            print("+", "-" * 128, "+", "\n")


def display_dossier(key, values):
    print("+", "=" * 128, "+")
    print(
        "||", " " * 30, "PatientDossier", " " * 30, "||")
    print("+", "=" * 128, "+")
    print("|{:<15} | {:<15} | {:<15} | {:<15} | {:<10} | {:<10} | {:<10} | {:<19}|".format(
        "BSN", "Patiëntnummer", "Voornaam", "Achternaam", "Gewicht", "Leeftijd", "Lengte", "Bloeddruk"))
    print("+", "-" * 128, "+")
    print("|{:<15} | {:<15} | {:<15} | {:<15} | {:<10} | {:<10} | {:<10} | {:<19}|".format(
        key[1], key[0], key[2], key[3], values[0], values[1], values[2], values[3]))
    print("+", "-" * 128, "+")


def create_patient_dossier():
    bsn = input("Voer het BSN in: ")
    patientnummer = input("Voer het patiëntnummer in: ")
    voornaam = input("Voer de voornaam in: ")
    achternaam = input("Voer de achternaam in: ")
    gewicht = input("Voer het gewicht in: ")
    leeftijd = input("Voer de leeftijd in: ")
    lengte = input("Voer de lengte in: ")
    bloeddruk = input("Voer de bloeddruk in: ")
    value = [gewicht, leeftijd, lengte, bloeddruk]
    patient_database[(patientnummer, bsn, voornaam, achternaam)] = value
    print("De nieuwe patiënt is toegevoegd. \n")


def pas_waardes_aan():
    patientnummer = input("Voer het patiëntnummer in: ")
    if patientnummer in patient_database:
        patient = patient_database[(patientnummer,)]
        print("Patiëntgegevens:")
        display_dossier((patientnummer,) + patient_database[patientnummer], patient)
        field = input("Welke waarde wilt u aanpassen (gewicht/leeftijd/lengte/bloeddruk)? ")
        if field == 'gewicht':
            new_gewicht = input("Voer het nieuwe gewicht in: ")
            patient[0] = new_gewicht
        elif field == 'leeftijd':
            new_leeftijd = input("Voer de nieuwe leeftijd in: ")
            patient[1] = new_leeftijd
        else:
            print("Ongeldige keuze.\n")
    else:
        print("Patiënt niet gevonden.\n")


# Start het hoofdmenu
main_menu()

# //////////SET//////////
"""
Oefening 1

Gegeven de verzameling {3, 44, 17, 23, 58, 9, 36}
Voer de volgende opdrachten uit:
Voeg de waarde 27 aan de verzameling toe.
Verwijder de waarde 23 uit de verzameling’.
Druk alle waarden in de verzameling tussen 20 en 50 af.
"""

nummers = {3, 44, 17, 23, 58, 9, 36}
nummers.add(27)
print(nummers)
nummers.remove(23)
print(nummers)
for nummer in nummers:
    if 50> nummer> 20:
        print(nummer)

"""
Oefening2
Gegeven de verzamelingen {11, 22, 33} en {5, 11, 16, 22}

Gebruik alleen set functies om de volgende verzamelingen te creëren:

{33}
{5, 16, 33}
{5, 11, 16, 22, 33}
{11, 22}

"""
verzameling1 = {11, 22, 33}
verzameling2 = {5, 11, 16, 22}
verzameling3 = verzameling1-verzameling2
print(verzameling3)
verzameling4 = (verzameling2 - verzameling1) | verzameling3
print(verzameling4)
verzameling5= verzameling2|verzameling3
print(verzameling5)
verzameling6 = verzameling1-verzameling3
print(verzameling6)


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
import random

recievers = set()
givers = set()


def add_names():
    number_of_names = int(input(f"voer het aantal namen in dat je wilt: "))
    for x in range(number_of_names):
        name = input(f"Voer naam in: ")
        recievers.add(name)
        givers.add(name)


def create_surprise_pairs():
    pairs = []
    while len(givers) != 0:
        reciever = random.choice(list(recievers))
        giver = random.choice(list(givers))
        if reciever != giver:
            givers.remove(giver)
            recievers.remove(reciever)
            pairs.append(reciever + "-" + giver)
    print("Surprise-paren:")
    for pair in pairs:
        reciever, giver = pair.split("-")
        print(f"{giver} geeft een surprise aan {reciever}")


def main():
    while True:
        print("\n1. Voeg namen toe")
        print("2. Maak surprise-paren")
        print("3. Stop")

        choice = input("Kies een optie: ")

        if choice == "1":
            add_names()
        elif choice == "2":
            if len(recievers) < 2:
                print("Voeg minimaal twee namen toe voordat je surprise-paren maakt.")
            else:
                create_surprise_pairs()
                break
        elif choice == "3":
            break
        else:
            print("Ongeldige keuze. Kies 1, 2 of 3.")


main()

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
tlds = {'Nederland': 'nl', 'Verenigde Staten': 'us', 'Duitsland': 'de'}
print('Duitsland', 'Duitsland' in tlds)
print('Frankrijk', 'Frankrijk' in tlds)
for land, afkorting in tlds.items():
        print(land, "\t->\t", afkorting)
tlds['Zweden'] = "sw"
tlds['zweden'] = "se"
for afkorting, land in tlds.items():
    print(land, "\t->\t", afkorting)
for afkorting, land in tlds.items():
    print(afkorting.upper(), land)

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
name_counter = {}

while True:
    name = input("Enter a name (or 'quit' to exit): ")

    if name.lower() == 'quit':
        break

    if name in name_counter:
        name_counter[name] += 1
    else:
        name_counter[name] = 1

    print("Name counts:")
    for name, count in name_counter.items():
        print(f"{name}: {count}")
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
vrienden = {'Bas': 32, 'Michelle': 28, 'Richard': 29, 'Bartho': 24, 'Tim': 30, 'Jitze': 32}
vrienden_sorted = sorted(vrienden.items())
print(vrienden_sorted)

for vriend, leeftijd in vrienden.items():
    if leeftijd >= 30:
        print(vriend, '->', leeftijd)

for vriend, leeftijd in vrienden.items():
    leeftijd = leeftijd+1
    print(vriend, leeftijd)

for key in list(vrienden.keys()):
    if key.startswith('B'):
        del vrienden[key]
print(vrienden)
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

engels_frans = {}

# stap 1
x = 0
for key in nederlands_frans:
    engels_frans[english_words[x]] = nederlands_frans.get(key)
    x += 1
print(engels_frans)

# stap 2
frans_engels = {}
for key, value in engels_frans.items():
    frans_engels[value] = key

print(frans_engels)

# stap 3

vertaler = {"nederlands_frans": nederlands_frans, "engels_frans": engels_frans, "frans_engels": frans_engels}


# stap 4

def vraag_vertaling(vertaler, taal, woord):
    if taal in vertaler:
        woordenboek = vertaler[taal]
        if woord in woordenboek:
            return woordenboek[woord]
        else:
            nieuwe_vertaling = input(f"Vertaling voor '{woord}' in {taal} niet gevonden. Voeg een vertaling toe: ")
            woordenboek[woord] = nieuwe_vertaling
            return f"Vertaling '{nieuwe_vertaling}' voor '{woord}' is toegevoegd in {taal}."
    else:
        return f"De opgegeven taal '{taal}' is niet beschikbaar in de vertaler."


# Testen van de methode
while True:
    print("Beschikbare talen: nederlands_frans, engels_frans, frans_engels")
    taal = input("Voer de gewenste taal in: ")
    woord = input("Voer het woord in waarvan je de vertaling wilt weten: ")
    vertaling = vraag_vertaling(vertaler, taal, woord)
    print(vertaling)
