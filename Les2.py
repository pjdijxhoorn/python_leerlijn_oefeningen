from les1 import les1

def les2():
    print("")
    # ==========Les2==========
    # //////////if-elif-else//////////
    # ------------opdracht1----------

    """ 
    maak twee variabele aan regen en vriezen en geef deze een boolean waarde.
    maak een if statement aan die test of het geregend en gevroren heeft. Als dat zo is dan print je:
     "pas op het sneeuwt".
    Maak een elif die test of het regent maar niet vriest. deze print "het regent"
    maak een elif aan die test of het vriest maar niet regent. deze print "pas op er zou ijzel kunnen zijn" 
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
    Maak de variabelen child, rich, cat geef deze allen een boolean waarde.
    maaf een if-else statement.
    de if test of je rijk bent, een kind bent of een kat bent.
    Als dat zo is print je :"lucky je hoeft niet te werken" 
    anders print je: "pech je moet werken."
    """

    rich = False
    cat = True
    child = False

    if rich == True or child == True or cat == True:
        print("lucky je hoeft niet te werken" )
    else:
        print("pech je moet werken.")

    # //////////While Statements/////////
    # ------------opdracht1----------
    """
    maak een variabele counter zet de waarde op 0.
    maak een while lus die elke lus 1 bij de counter zet en stopt als de counter op 10 staat.
    elke keer als de counter opgehoogt wordt moet deze geprint worden.
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

