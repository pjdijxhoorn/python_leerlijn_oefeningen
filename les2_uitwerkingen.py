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

vriezen = True
regen = False

if regen == True and vriezen == True:
    print("pas op het sneeuwt")
elif regen == True and vriezen == False:
    print("het regent")
elif regen == False and vriezen == True:
    print("pas op er zou ijzel kunnen zijn")
else:
    print("je kan veilig rijden")

# ------------opdracht2----------
"""
Maak de variabelen i_am_a_child, i_am_rich, i_am_a_cat geef deze allen een boolean waarde.
maak een if-else statement.
de if test of je rijk bent, een kind bent of een kat bent.
Als dat zo is print je :"lucky je hoeft niet te werken" 
anders print je: "pech je moet werken."
"""

i_am_rich = False
i_am_a_cat = True
i_am_a_child = False

if i_am_rich == True or i_am_a_child == True or i_am_a_cat == True:
    print("lucky je hoeft niet te werken")
else:
    print("pech je moet werken.")

# //////////While Statements/////////
# ------------opdracht1----------
"""
maak een variabele counter zet de waarde op 0.
maak een while lus die elke lus 1 bij de counter zet en stopt als de counter op 10 staat.
elke keer als de counter opgehoogd wordt moet deze geprint worden.
"""

counter = 0

while counter > 11:
    print(counter)
    counter += 1

# ------------opdracht2----------
"""
Maak een while lus.
Deze while lus moet net zo lang lopen todat de teller op 10 staat.
print alleen de even getallen uit.
"""

teller = 0

while teller < 10:
    teller += 1
    if teller % 2 == 0:
        print(teller)
    else:
        print("")

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

candy = 10
hungry = True

while candy != 0 and hungry == True:
    print("er zijn nog ", candy, " snoepjes over tijd om er nog een te eten.")
    candy -= 1
print("de snoepjes zijn op!")

# //////////For statement//////////
# ------------opdracht1----------
"""
Maak een forloop die tot 10 telt en de nummers print.
Bonus in plaats van optellen maak een forloop die aftelt.
deze moet na 1 Boom!! printen
"""

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)
    if i == 1:
        print("Boom!!")

# ------------opdracht2----------
"""
1. maak een for loop die de getallen 1 tot 100 print.
2. voeg een if statement toe die checkt of een getal even is,
   als dat het geval is gebruik je een continu statement.
3. maak nog een if statement aan die checkt of het getal onder de 30 ligt en boven de 25,
   als dat zo is stop dan met de loop.
"""

for i in range(1, 100):
    if i % 2 == 0:
        continue
    if i < 30 and i > 25:
        break
    print(i)

# ------------opdracht3----------
"""
maak een forloop met een range van 1 tot 11 met item naam number1.
maak binnen deze forloop nog een forloop met een range van 1 tot 11 deze heeft als item naam number2.
print in de binnenste for loop  number1, "X", number2, " = ", number1 * number2
Voordat je de code test schrijf een comment wat je denkt dat er gebeurd.
had je gelijk? Leg uit wat er gebeurd.
"""

for number1 in range(1, 11):
    for number2 in range(1, 11):
        print(number1, "X", number2, " = ", number1 * number2)

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

totalpoints = 0

while True:

    maximaal = int(input("Give a max number for the game: "))
    minimaal = int(input("Give a minimum number for the game: "))
    randomNumber1 = random.randint(minimaal, maximaal)
    randomNumber2 = random.randint(minimaal, maximaal)
    punten = 6

    while True:

        if punten == 6:
            print("Welcome to the calculation guessing game!")
            vermenigvuldig = randomNumber1 * randomNumber2
            print("Tip 3: number 1  X  number 2  = ", vermenigvuldig)

        userinput = input("Do you want a tip fill in tip, or do you want to guess the fill in guess: ")
        if userinput == "tip":
            punten -= 1
            if punten == 5:
                groter = randomNumber1 > randomNumber2
                print("Tip 2: number 1 is bigger then number 2 = ", groter)
            elif punten == 4:
                gelijk = randomNumber1 == randomNumber2
                print("Tip 1: number 1 and number are equal = ", gelijk)
            elif punten == 3:
                plus = randomNumber1 + randomNumber2
                print("Tip 4: number 1 + number 2 = ", plus)
            elif punten == 2:
                aftrekken = randomNumber1 - randomNumber2
                print("Tip 5: number 1 - number 2 = ", aftrekken)
            elif punten == 1:
                delen = randomNumber1 / randomNumber2
                print("Tip 6: number 1 / number 2 = ", delen)
            else:
                punten += 1
                print("No tips left sorry!")


        elif userinput == "guess":
            guessNumber1 = int(input("What do you think number 1 is: "))
            guessNumber2 = int(input("What do you think number 2 is: "))
            if guessNumber1 == randomNumber1 and guessNumber2 == randomNumber2:
                totalpoints = totalpoints + punten
                print("Yeah you won!! you got", punten, "points and your total is now", totalpoints)
                break
            else:
                print("sorry that was incorrect try again or ask for another tip!")
        else:
            print("incorrect input please fill in guess or tip")

    anothergame = input("Do you want another game? y / n ")
    if anothergame == "n":
        break

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

dollar_euro = 0.94
euro_dollar = 1.07

while True:
    print("1 dollar = ", dollar_euro, "euro. and 1 euro is ", euro_dollar, " dollar")

    userchoice = input("for dollerconversion type dollar, for euro conversion type euro")

    if userchoice == "dollar":
        while True:
            try:
                conversion_dollar_to_euro = float(input("Give the amount of dollar you want to convert to euro: "))
                print(conversion_dollar_to_euro, "dollar converterd to euro is: ",
                      conversion_dollar_to_euro * dollar_euro)
            except:
                print("That is not a valid amount")
    elif userchoice == "euro":
        while True:
            try:
                conversion_euro_to_dollar = float(input("Give the amount of euro you want to convert to dollar: "))
                print(conversion_euro_to_dollar, "euro converterd to dollar is: ",
                      conversion_euro_to_dollar * euro_dollar)
            except:
                print("That is not a valid amount")
    else:
        print("that was not a valid choice! please type dollar or euro")

    userchoice = input("want to do another conversion? y = yes, n = no")
    if userchoice == "n":
        print("thank you for using our service, goodbye!")
        break
