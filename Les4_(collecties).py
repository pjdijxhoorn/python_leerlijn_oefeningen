"""
------------- oefening 1-------------
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
