import timeit

import numpy as np


"""
Opdracht1
Maak het array {3 8 2 5} en wijzig vervolgens de waarde van het tweede element in 7.


"""
array = np.array([3, 8, 2, 5])
array[1] = 7
print(array)


"""
Opdracht 2

Gebruik de arange-functie om een array van 20 even getallen te maken van 2 tot en met 40
en wijzig de vorm vervolgens naar een 2-dimensionaal array van 4 bij 5.
"""
stappen = np.arange(2, 42, 2)
stappen = stappen.reshape(4, 5)
print(stappen)


"""
Opdracht 3

Maak een numpy array met 50 willekeurige gehele getallen tussen 1 en 6 (inclusief 1 en 6). 
Bepaal de index van het eerste 
getal 3 in het array. Als 3 niet voorkomt moet er een passende boodschap worden 
afgedrukt.

"""

# Maak een numpy array met 50 willekeurige gehele getallen tussen 1 en 6 (inclusief 1 en 6)
random_array = np.random.randint(1, 7, size=50)
print(random_array)
# Zoek de index van het eerste getal 3 in het array
index_3 = np.where(random_array == 3)[0]

print(index_3)
# Controleer of het getal 3 is gevonden en druk de boodschap af
if index_3.size > 0:
    print(f"Index van het eerste getal 3: {index_3[0]}")
else:
    print("Het getal 3 komt niet voor in het array.")

"""
Opdracht 4
We gaan de snelheid van optelling in een lijst en een array vergelijken.
 Maak eerst met behulp van respectievelijk list comprehension en de arange-functie een lijst en een array 
 met de waarden 0, 1, 2, …, 999999 aan.

Gebruik vervolgens de methode default_timer() uit de module timeit om te meten hoe snel 
alle getallen uit de lijst en het array worden opgeteld.
Hierbij gebruik je de ingebouwde som-functie voor de lijst en de methode som() 
uit module numpy voor het array.
"""

# Maak een lijst met waarden 0, 1, 2, ..., 999999 met behulp van list comprehension
lijst = [i for i in range(1000000)]

# Maak een NumPy-array met waarden 0, 1, 2, ..., 999999 met behulp van de arange-functie
array = np.arange(1000000)

# Definieer een functie om de optelling uit te voeren voor de lijst met behulp van de ingebouwde sum-functie
def optel_lijst():
    return sum(lijst)

# Definieer een functie om de optelling uit te voeren voor het array met behulp van de numpy sum() methode
def optel_array():
    return np.sum(array)

# Meet de tijd voor de optelling van de lijst
lijst_tijd = timeit.timeit(optel_lijst, number=10)

# Meet de tijd voor de optelling van het array
array_tijd = timeit.timeit(optel_array, number=10)

# Druk de gemeten tijden af
print(f"Tijd voor optelling in de lijst: {lijst_tijd:.5f} seconden")
print(f"Tijd voor optelling in het array: {array_tijd:.5f} seconden")