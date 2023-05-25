"""
------------- oefening 1-------------
Opdracht ontcijferen van de vijandelijke code

Je hebt een bericht onderschept van de vijand en door goede inlichtingen ben je erachter gekomen hoe de vijand zijn berichten versleuteld.
Dit doen ze met een ceasar cipher. dit betekent dat ze elke letter in hun bericht vervangen door een letter x aantal plekken verder in het aflabet.
ontcijfer het bericht.

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
    for x in text:
        if x == " " or x == ".":
            decodedmessages += x
        else:
            ciphernumber = alphabet.index(x.upper())
            ciphernumber += shiftnumber
            if ciphernumber >= 26:
                ciphernumber = ciphernumber % 26
            x = alphabet[ciphernumber]
        decodedmessages += x
    return decodedmessages

decodedmessage = decoder("eju jt ffo uftu", 25)
print(decodedmessage)

extrasecretmessages = "DLDTNIYIHYDJGNIFYFUMJZXIATDXCMNCYUNN"
decodedmessage = decoder(extrasecretmessages, 20)

def grid_to_string(s):
     row1 = s[0]+s[6]+s[12]+s[18]+s[24]+s[30]
     row2 = s[1]+s[7]+s[13]+s[19]+s[25]+s[31]
     row3 = s[2]+s[8]+s[14]+s[20]+s[26]+s[32]
     row4 = s[3]+s[9]+s[15]+s[21]+s[27]+s[33]
     row5 = s[4]+s[10]+s[16]+s[22]+s[28]+s[34]
     row6 = s[5]+s[11]+s[17]+s[23]+s[29]+s[35]
     newstring =row1+row2+row3+row4+row5+row6
     return newstring

def decodegrid(message):
    decodetext = []
    for x in range(6):
        row = ""
        for j in range(6):
            letter = x+j*6
            row += message[letter]
        decodetext.append(row)
    decodetext = "".join(decodetext)
    return decodetext

inputstring ="OWOEYTJTSJOURYTQJQFXUKITLEOINXYNJFYY"
input_str = decoder(inputstring, -5)

# output_str = grid_to_string(input_str)
output_str = decodegrid(input_str)
print(output_str)  # Output: jemagtrotszijnopjezelfdatjeditoplost

"""
------------- oefening 2-------------
Jij bent onderdeel van het verzet en je hebt een vergadering met alle leden hoe je het beste te werk kan gaan.
Een van de leden zegt terecht dat hij de meeting niet wil bijwonen als zijn naam op de notulen komt want dan kan hij opgepakt worden.
Om dat te verkomen dat een van de leden ontmaskerd wordt belsuit je een versleuteling te schrijven voor de namen.
natuurlijk moeten de namen ook weer ontcijferd worden.


lijst met namen
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

encryptedname ='116-1-21-12-104-5-120-1-14-11'
decryptedname = decrypt(encryptedname)
print(decryptedname)