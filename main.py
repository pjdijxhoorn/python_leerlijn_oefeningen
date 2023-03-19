from les1 import les1
from Les2 import les2
from les3 import les3
from les4 import les4

from test import test

number = int(input("geef een nummer om te checken voor positief negatief"))

# check if number is greater than 0
if number > 0:
    print('Number is groter dan 0.')
else:
    print('Number is kleiner dan 0.')



stoppen = 1
while stoppen == 1:
    keuze = int(input("geef een cijfer voor welke les je wilt printen : "))
    if keuze == 1:
        les1()
    elif keuze == 2:
        les2()
    elif keuze == 3:
        les3()
    elif keuze == 4:
        les4()


    elif keuze == 10:
        test()
    else:
        print("je hebt geen correcte keuze ingevoerd")
        stoppen = int(input("\nWil je stoppen of nog 1 een les printen?"
                            "\nType 1 om door te gaan elke ander toets zal het programma stoppen. \n"))
