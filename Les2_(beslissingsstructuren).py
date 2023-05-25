# ==========Les2==========
# //////////if-elif-else//////////
# ------------opdracht1----------

"""
Maak twee variabele aan regen en vriezen en geef deze een boolean waarde.
Maak een if statement aan die test of het geregend en gevroren heeft. Als dat zo is dan print je:
 "pas op het sneeuwt".
Maak een elif die test of het regent maar niet vriest. Deze print "het regent"
maak een elif aan die test of het vriest maar niet regent. Deze print "pas op er zou ijzel kunnen zijn"
maak een else aan deze print: "je kan veilig rijden"
"""

# ------------opdracht2----------
"""
Maak de variabelen i_am_a_child, i_am_rich, i_am_a_cat geef deze allen een boolean waarde.
maak een if-else statement.
de if test of je rijk bent, een kind bent of een kat bent.
Als dat zo is print je :"lucky je hoeft niet te werken" 
anders print je: "pech je moet werken."
"""

# //////////While Statements/////////
# ------------opdracht1----------
"""
maak een variabele counter zet de waarde op 0.
maak een while lus die elke lus 1 bij de counter zet en stopt als de counter op 10 staat.
elke keer als de counter opgehoogd wordt moet deze geprint worden.
"""

# ------------opdracht2----------
"""
Maak een while lus.
Deze while lus moet net zo lang lopen todat de teller op 10 staat.
print alleen de even getallen uit.
"""


# ------------opdracht3----------
""" 
Maak een variabele candy geef deze de waarde 10 en een variabele hungry met waarde true.
maak een while loop die test of candy niet 0 is en of hungry True is.
in de while loop print je "er zijn nog x snoepjes tijd om er nog een te eten"
waar x het nummer aan snoepjes over is. 
haal elke lus ook 1 snoepje er van af.
print aan het einde de snoepjes zijn op.
BONUS: zorg dat er bij 1 snoepje en niet snoepjes staat.

"""

# //////////For statement//////////
# ------------opdracht1----------
"""
Maak een forloop die tot 10 telt en de nummers print.
Bonus in plaats van optellen maak een forloop die aftelt.
deze moet na 1 Boom!! printen
"""


# ------------opdracht2----------
"""
1. maak een for loop die de getallen 1 tot 100 print.
2. voeg een if statement toe die checkt of een getal even is,
   als dat het geval is gebruik je een continu statement.
3. maak nog een if statement aan die checkt of het getal onder de 30 ligt en boven de 25,
   als dat zo is stop dan met de loop.
"""

# ------------opdracht3----------
"""
maak een forloop met een range van 1 tot 11 met item naam number1.
maak binnen deze forloop nog een forloop met een range van 1 tot 11 deze heeft als item naam number2.
print in de binnenste for loop  number1, "X", number2, " = ", number1 * number2
Voordat je de code test schrijf een comment wat je denkt dat er gebeurd.
had je gelijk? Leg uit wat er gebeurd.
"""

# ------------opdracht4----------
import random

"""
We gaan hier verder met het raadspel van les 1.
we gaan het raadspel zo maken dat het slechts 1 berekening geeft. 
En dat de speler tips kan bij vragen wat de overige berekeningen zijn.
ook gaan we punten bij houden hoe meer tips een speler vraagt des minder punten verdient kunnen worden.

Stap1:  maak twee variabele maximaal en minimaal.
        de waarde van deze variabele is een int (input()) met als tekst "Give a max number for the game: "
        en "Give a minimum number for the game: " .
Stap2:  Maak nog twee variabele randomNumber1 en randomNumber2 en vul deze met random.randint() 
        met de minimaal en maximaal als bereik. hierdoor krijg je een getal tussen minimaal en maximaal.
Stap3:  maak een variabele punten en geef deze de waarde 6.
Stap4:  Maak een while loop met als conditie True
Stap5:  Als het aantal punten gelijk is aan 6 print dan een welkoms bericht 
        en geef de eerste tip (1 van de berekeningen)
Stap6:  Maak een variabele userinput en geef deze de waarde van een input() met als tekst
        "Do you want a tip fill in tip, or do you want to guess the fill in guess: "
Stap7:  Maak een if-elif-else statement. De if statement test voor tip de elif test voor guess. 
        en de else statement bevat een print "incorrect input please fill in guess or tip"
Stap8:  in de if statement met de conditie userinput == "tip" doe je een aantal dingen. 
        Eerst haal je een punt af van punten. vervolgens maak je een if- elif - else statement die test voor
        het aantal punten. omdat dat minder wordt per keer dat tip gekozen wordt kan je dit gebruiken om 
        de overige tips uit te printen. 
        omdat we niet onder de 1 willen komen is de else statement een 1+ voor punten en een print 
        "No tips left sorry!" 
Stap9:  Nu gaan we de Elif met de conditie userinput == "guess" afmaken.
        maak hierin twee variabele aan guessNumber1 en guessNumber2 deze worden gevuld 
        met een int waarde gegeven door de user. geef deze de tekst: What do you think number 1 is:
        en hetzelfde voor het tweede nummer. Maak vervolgens een if -else statement die test of 
        guessnumber1 gelijk is aan randomnumber 1 en guessnumber2 gelijk is aan randomnumber2.
        als dat zo is dan krijg je een print met een overwinnings-bericht en het punten aantal dat gescoord is.
        maak hier ook een break.
        anders maak je een print met "sorry that was incorrect try again or ask for another tip!"

 BONUS: Breid het spel zo uit dat je meerdere rondes kan spelen en hierbij je score steeds verder kan uitbreiden.
 """

# ------------opdracht5----------

"""
We gaan verder werken aan de dollar-euro converter.
Maak het zo dat de gebruiker vaker dan een maal een currency kan converteren.
zorg dat de gebruiker kan kiezen tussen dollar-euro of euro-dollar
pas een while too om te checken of een invoer van de strings goed is 
en blijf in de loop totdat de juiste invoer is gedaan.
zorg ervoor dat je een try except bouwt om de float input van amount.

BONUS voeg meer valuta's toe bijvoorbeeld: pond, yen, bitcoin

"""
